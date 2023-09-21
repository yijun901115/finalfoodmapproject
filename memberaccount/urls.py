from django.urls import path
from memberaccount import views

app_name = 'memberaccountnewuser'
urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('signin/', views.signIn, name='signin'),
]