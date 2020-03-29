from django.urls import path
from .import views
app_name = 'blogs'
urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('edit_blog',views.edit_blog, name='edit_blog'),
]