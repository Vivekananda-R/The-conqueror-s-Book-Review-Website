from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as authviews


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.register,name="registration"),
    path('login/',authviews.LoginView.as_view(template_name = 'user/login.html'),name = 'login'),
    path('logout/',authviews.LogoutView.as_view(template_name = 'user/logout.html'),name = 'logout')
]
