from django.urls import path
from tap2eat import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('createuser/', views.createuser, name="createuser"),
    path('usertable1/', views.usertable1, name="usertable1"),
    path('usertable2/', views.usertable2, name="usertable2"),
    path('usertable3/', views.usertable3, name="usertable3"),
    path('mealtap/', views.taptap, name="mealtap"),
    path('mpesa/', views.mpesa, name="mpesa"),
    path('sms/', views.sms, name="sms"),
    path('dailyreports/', views.dailyreports, name="dailyreports"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]