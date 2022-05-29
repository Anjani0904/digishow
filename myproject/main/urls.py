from . import views
from django.views.generic import TemplateView
from django.urls import path , include

app_name='main'
urlpatterns=[
    path('',views.index,name='index'),
    path("about/",views.aboutpage,name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('project/all',views.all_projects,name='all_projects'),
    path('project/<int:id>',views.project_details,name='project_details'),
    path('project/<int:id>/delete',views.project_delete,name='project_delete'),
    path('project/<int:id>/like',views.project_like,name='like'),
    path('project/<int:id>/unlike',views.project_unlike,name='unlike'),
    path('project/<int:id>/edit',views.project_edit,name='project_edit'),
    path('profile/<int:id>/edit',views.profile_edit,name='profile_edit'),
]
