from django.urls import path, re_path
from . import views

app_name = 'aggApp'

urlpatterns = [
    # path('aggApp/', views.members, name='aggApp'),
    re_path(r'^api/students/$', views.students_list),
    re_path(r'^api/students/([0-9])$', views.students_detail),
    re_path(r'^paginate/', views.paginate, name='paginate_page'),
    re_path(r'^api/paginate/', views.paginate, name='paginate'),
    # re_path(r'^page_num/', views.current_page, name='current_page'),
]