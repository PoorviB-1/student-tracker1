from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count, Q
from django.contrib import messages
from .models import Student, Course, Attendance, Performance, Enrollment
from datetime import datetime, timedelta

def dashboard(request):
    """Main dashboard view with statistics"""
    context = {
        'total_students': Student.objects.filter(is_active=True).count(),
        'total_courses': Course.objects.filter(is_active=True).count(),
        'today_attendance': Attendance.objects.filter(date=datetime.now().date()).count(),
        'recent_students': Student.objects.filter(is_active=True)[:5],
        'recent_performances': Performance.objects.select_related('student', 'course')[:10],
    }
    return render(request, 'core/dashboard.html', context)


def student_list(request):
    """Display list of all students with search functionality"""
    search_query = request.GET.get('search', '')
    
    students = Student.objects.filter(is_active=True)
    
    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    context = {
        'students': students,
        'search_query': search_query,
    }
    return render(request, 'core/student_list.html', context)


def student_detail(request, roll_number):
    """Display detailed information about a specific student"""
    student = get_object_or_404(Student, roll_number=roll_number)
    
    # Get enrolled courses
    enrollments = Enrollment.objects.filter(student=student).select_related('course')
    
    # Get attendance statistics
    total_attendance = Attendance.objects.filter(student=student).count()
    present_count = Attendance.objects.filter(student=student, status='P').count()
    attendance_percentage = (present_count / total_attendance * 100) if total_attendance > 0 else 0
    
    # Get performance statistics
    performances = Performance.objects.filter(student=student).select_related('course')
    avg_percentage = performances.aggregate(
        avg=Avg('marks_obtained')
    )['avg'] or 0
    
    # Recent attendance
    recent_attendance = Attendance.objects.filter(student=student).select_related('course')[:10]
    
    context = {
        'student': student,
        'enrollments': enrollments,
        'total_attendance': total_attendance,
        'present_count': present_count,
        'attendance_percentage': round(attendance_percentage, 2),
        'performances': performances,
        'avg_percentage': round(avg_percentage, 2),
        'recent_attendance': recent_attendance,
    }
    return render(request, 'core/student_detail.html', context)


def attendance_view(request):
    """View and mark attendance"""
    selected_date = request.GET.get('date', datetime.now().date())
    selected_course = request.GET.get('course', '')
    
    courses = Course.objects.filter(is_active=True)
    
    attendances = Attendance.objects.filter(date=selected_date)
    
    if selected_course:
        attendances = attendances.filter(course_id=selected_course)
    
    attendances = attendances.select_related('student', 'course')
    
    # Calculate statistics
    total = attendances.count()
    present = attendances.filter(status='P').count()
    absent = attendances.filter(status='A').count()
    late = attendances.filter(status='L').count()
    excused = attendances.filter(status='E').count()
    
    context = {
        'attendances': attendances,
        'courses': courses,
        'selected_date': selected_date,
        'selected_course': selected_course,
        'total': total,
        'present': present,
        'absent': absent,
        'late': late,
        'excused': excused,
    }
    return render(request, 'core/attendance.html', context)


def performance_view(request):
    """View student performance and grades"""
    selected_student = request.GET.get('student', '')
    selected_course = request.GET.get('course', '')
    
    students = Student.objects.filter(is_active=True)
    courses = Course.objects.filter(is_active=True)
    
    performances = Performance.objects.select_related('student', 'course')
    
    if selected_student:
        performances = performances.filter(student_id=selected_student)
    
    if selected_course:
        performances = performances.filter(course_id=selected_course)
    
    context = {
        'performances': performances,
        'students': students,
        'courses': courses,
        'selected_student': selected_student,
        'selected_course': selected_course,
    }
    return render(request, 'core/performance.html', context)


def reports_view(request):
    """Generate various reports"""
    # Top performers
    top_performers = Student.objects.filter(is_active=True).annotate(
        avg_marks=Avg('performance__marks_obtained')
    ).order_by('-avg_marks')[:10]
    
    # Attendance report
    low_attendance = []
    for student in Student.objects.filter(is_active=True):
        if student.attendance_percentage < 75:
            low_attendance.append({
                'student': student,
                'percentage': student.attendance_percentage
            })
    
    # Course-wise statistics
    course_stats = []
    for course in Course.objects.filter(is_active=True):
        enrolled = Enrollment.objects.filter(course=course).count()
        avg_performance = Performance.objects.filter(course=course).aggregate(
            avg=Avg('marks_obtained')
        )['avg'] or 0
        
        course_stats.append({
            'course': course,
            'enrolled': enrolled,
            'avg_performance': round(avg_performance, 2)
        })
    
    context = {
        'top_performers': top_performers,
        'low_attendance': low_attendance,
        'course_stats': course_stats,
    }
    return render(request, 'core/reports.html', context)