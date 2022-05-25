from . import views
from django.views.generic import TemplateView
from django.urls import path , include

app_name='main'
urlpatterns=[
    path('',views.index,name='index'),
    path("contact/",views.contact,name='contact'),
    path("portfolio/",views.portfolio,name="porfolio"),
    path("we_do/",views.we_do,name="wedo"),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/',views.student_view, name='student'),
    path('dashboard/',views.project_view, name='project'),
    path('dashboard/',views.category_view, name='dashboard'),
    path('dashboard/',views.picture_view, name='dashboard'),
    path('dashboard/',views.video_view, name='dashboard'),

]
