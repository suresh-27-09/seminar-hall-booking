from django.shortcuts import render,redirect
from .models import *
import sweetify
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if 'uname' in request.session:
        the=halls.objects.all()
        th=len(the)
        eve=booking.objects.all()
        ev=len(eve)
        return render (request,'index.html',{'session':request.session['uname'],'th':th,'ev':ev})
    else:
        return render (request,'index.html',{'session':None})

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']  
        name=Register.objects.all()
        usern='nouser'
        for i in name:
            if i.uname==username:
                usern='user'
                print(i.uname)
        if usern=='user':
            user = Register.objects.get(uname=username)
            if password==user.password:
               request.session ['uname'] = username
               sweetify.success(request,title="success",text="logged in successfully..",button="close" )
               return render(request,'index.html',{'session':request.session['uname']} )
            else:
               sweetify.error(request,title='invalid password',text='please enter correct password',button='close')
               return render(request,'login.html')
        else:
            sweetify.error(request,title='No User Found',text='please enter correct User',button='close')
            return render(request,'login.html')

    else:
        return render(request,'login.html')
    

    

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            id=Register.objects.all()
            user=[]
            for i in id:
                user.append(i.uname)
                print(user)
            if username not in user:
                obj=Register()
                obj.uname=username
                obj.password=password
                obj.save()
                sweetify.success(request,title='Success',text='Successfully Registered' ,button="ok")
                return redirect('index')
            else:
                sweetify.warning(request,title='Error',text='username already taken',button='close')
                return render(request,'register.html')

        else:
            sweetify.error(request,title='Error',text='password does not match' ,button="ok")
            return render(request,'register.html')

    else:
        return render(request,'register.html')
    
def logout(request):
    del request.session['uname']
    return redirect('index')

def error(request):
    return render (request,'error.html')


def total_hall(request):
    if 'uname' in request.session:
        hall=halls.objects.all().order_by('hall_id')
        return render (request,'halls.html',{'hall':hall,'session':request.session['uname']})
    else:
        return render (request,'error.html',{'session':None})
    
def hall_book(request,id):
    if 'uname' in request.session:
        booked=booking.objects.all()
        if request.method=="POST":
            hallname=request.POST['hallname']
            seatcap=int(request.POST['noseats'])
            dept=request.POST['dept']
            ename=request.POST['eventname']
            coname=request.POST['coordinatename']
            coid=request.POST['coordinateid']
            totmem=int(request.POST['totmembers'])
            date=request.POST['date']
            time=request.POST['time']
            email=request.POST['email']
            print("Email : ",email)
            if len(booked)==0:
                book=booking()
                book.uname=request.session ['uname']
                book.hall_name=hallname
                book.hall_mem=seatcap
                book.dept=dept
                book.eventname=ename
                book.coordinatename=coname
                book.coordinateid=coid
                book.totalmember=totmem
                book.date=date
                book.time=time
                book.save()
                print("database stored")
                subject = 'Seminar Hall booked successfully..'
                message = (f'Hi {coname},Seminar hall booked Successfully,Thanks for choosing us \n Your Hall Name :{hallname} \n Your function is :{ename} \n Members: {totmem} \n date and time is : {date},{time}..')
               
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )
                sweetify.success(request,title='Success',text='Seminar hall booked successfully,Thank you..' ,button="ok")
                return redirect("index")
            else:
                booked=booking.objects.all()
                if (seatcap >= totmem):
                        de='notnone'
                        for j in booked:
                            print(j.hall_name,j.date,j.time)
                            d=str(j.date)
                            
                            if(j.hall_name==hallname and d==date and j.time==time):
                                de='none'
                                print("condition satisfied")
                                # break
                                
                        if de=='none':
                            print("already happen")
                            sweetify.error(request,title='Error',text='Time slot already booked try something else' ,button="ok")
                            return redirect('hall_book',id=id)
                        elif de=='notnone':
                            book=booking()
                            book.uname=request.session ['uname']
                            book.hall_name=hallname
                            book.hall_mem=seatcap
                            book.dept=dept
                            book.eventname=ename
                            book.coordinatename=coname
                            book.coordinateid=coid
                            book.totalmember=totmem
                            book.date=date
                            book.time=time
                            book.save()
                            subject = 'Seminar Hall booked successfully..'
                            message = (f'Hi {coname},Seminar hall booked Successfully,Thanks for choosing us'
                            f'\n Your Hall Name :{hallname} '
                            f'\n Coordinate Name : {coname}'
                            f'\n Your function is :{ename}'
                            f'\n Members: {totmem}'
                            f'\n date and time is : {date},{time}..')
                            email_from = settings.EMAIL_HOST_USER
                            recipient_list = [email, ]
                            send_mail( subject, message, email_from, recipient_list )
                            sweetify.success(request,title='Success',text='Seminar hall booked successfully,Thank you..' ,button="ok")
                            return redirect("index")
                    
                else:
                    print("un executed")
                    sweetify.warning(request,title='Warning',text='Members are too much than hall capacity , try another hall.' ,button="ok")
                    return redirect('hall_book',id=id)
                
                
        else:
            hal=halls.objects.all()
            for i in hal:
                if i.hall_id == id:
                    return render(request,'hallbook.html',{'session':request.session['uname'],'hallname':i.hall_name,'hallmem':i.hall_mem,'hallimg':i.hall_img,'hallimg':i.hall_img})
 

    else:
        return render (request,'error.html',{'session':None})
    
def list(request):
    if 'uname' in request.session: 
        booked=booking.objects.all().filter(uname=request.session ['uname'])
        return render(request,'list.html',{'booked':booked,'session':request.session['uname']})
    else:
        return render (request,'error.html',{'session':None})
    
def edit(request,id):
    if 'uname' in request.session: 
        user=booking.objects.get(id=id)
        print(user)
        de = booking.objects.get(id=id)
        de.delete()
        return render(request,'demo.html',{'user':user,'session':request.session['uname']})
    else:
        return render (request,'error.html',{'session':None})

def delete(request,id):
    de = booking.objects.get(id=id)
    de.delete()
    return redirect ('list')

def view_hall(request):
    booked=booking.objects.all()
    if 'uname' in request.session: 
        return render(request,'list1.html',{'booked':booked,'session':request.session['uname']})
    else:
        return render (request,'error.html',{'session':None})

    