from django.urls import path
from first_django_app.views import comment_refactor, request_show_name

urlpatterns = [
    path('', comment_refactor, name='index'),
    path('name/', request_show_name, name='index')
]
