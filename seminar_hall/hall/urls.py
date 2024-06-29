from django.urls import path
from hall import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
       path('',views.index,name='index'),
       path('halls/',views.total_hall,name='halls'),
       path('ha',views.login,name='login'),
       path('register/',views.register,name='register'),
       path('error',views.error,name='error' ),
       path('logout',views.logout,name='logout'),
       path('hall_book/<int:id>/',views.hall_book,name='hall_book'),
       path('list',views.list,name='list'),
       path('delete/<int:id>',views.delete,name='delete'),
       path('edit/<int:id>',views.edit,name='edit'),
       path('view_hall',views.view_hall,name='view_hall'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)