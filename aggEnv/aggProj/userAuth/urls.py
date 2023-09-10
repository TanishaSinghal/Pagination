from . import views
from django.urls import path, re_path

app_name = 'userAuth'

urlpatterns = [
    # path('userLogin/', views.userLogin, name="members"),
    # re_path(r"", views.homepage, name="homepage"),
    re_path(r'userRegistration/', views.userRegistration, name="userRegistration"),
    re_path(r'userLogin/', views.userLogin, name="userLogin"),
]