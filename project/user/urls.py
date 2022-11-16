from django.urls import path
from . import views


urlpatterns = [
	path('', views.registerPage, name="register"),
	path('login', views.loginPage, name="login"),  
	path('logout', views.logoutUser, name="logout"),
    
    path('home', views.home, name="home"),
	  path('wallect', views.wallect, name='wallect'),
	  path('send_money',views.send_money,name='send_money'),
	  path('Request_money',views.Request_money,name='Request_money'),
		path('Request_Recived',views.Request_Recived,name='Request_Recived'),
]