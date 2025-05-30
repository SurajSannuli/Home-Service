from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registration',views.Registerpage,name='registration'),
    path('login',views.loginpage,name='login'),
    path('book',views.book,name='book'),
    path('view_list',views.viewlist,name='view_list'),
    path('invoice/<str:pk>/',views.invoice,name='invoice'),
    
]
