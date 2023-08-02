from django.urls import path
from extracurricular import views

app_name = 'extracurricular'

urlpatterns = [
    path('', views.home, name='home'),
path('delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
path('manage_activities/', views.manage_activities, name='manage_activities'),
    path('halaman_utama/', views.halaman_utama, name='halaman_utama'),
     path('check_template/', views.check_template, name='check_template'),
    path('manage_activities/', views.manage_activities, name='manage_activities'),
    path('registration_form/', views.registration_view, name='registration_form'),   
    path('registration_success/', views.registration_success, name='registration_success'),   
]
