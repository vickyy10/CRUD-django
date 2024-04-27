
from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
     path('addcar/',views.add_car,name='addcar'),
       path('update/<int:id>',views.update_car,name='update'),
       path('delete/<int:id>',views.delete_car,name='update'),
        path('signup/',views.signup,name='signup'),
        path('login/',views.user_login,name='login'),
        path('logout/',views.user_logout,name='logout'),

]
