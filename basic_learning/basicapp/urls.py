from django.urls import path
from basicapp import views

#template urls

app_name = 'basic_app'

urlpatterns = [
    path('basic_app/register/',views.register,name="register"),
    path('user_login/',views.user_login,name='user_login')
]

