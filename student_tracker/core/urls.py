from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/<str:roll_number>/', views.student_detail, name='student_detail'),
    path('attendance/', views.attendance_view, name='attendance'),
    path('performance/', views.performance_view, name='performance'),
    path('reports/', views.reports_view, name='reports'),
]
