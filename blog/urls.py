
from django.urls import path
from . import views

#add variable app_name and set it equal to app
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    #below shows grabbing the id from the db and using id to print specific blog
    path('<int:blog_id>/',views.detail, name='detail'),

]
