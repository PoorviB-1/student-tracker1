"""
Script to create sample data for the Student Tracker application
Run with: python manage.py shell < create_sample_data.py
"""

import os
import django
from datetime import datetime, timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_tracker.settings')
django.setup()

from core.models import Student, Course, Enrollment, Attendance, Performance

# Clear existing data
print("Clearing existing data...")
Student.objects.all().delete()
Course.objects.all().delete()
Enrollment.objects.all().delete()
Attendance.objects.all().delete()
Performance.objects.all().delete()

# Create sample courses
print("Creating courses...")
courses_data = [
    {
        'code': 'CS101',
        'name': 'Introduction to Computer Science',
        'description': 'Fundamentals of programming and computer science concepts',
        'credits': 3,
        'instructor': 'Dr. John Smith'
    },
    {
        'code': 'CS201',
        'name': 'Data Structures',
        'description': 'Advanced data structures and algorithms',
        'credits': 4,
        'instructor': 'Prof. Sarah Johnson'
    },
    {
        'code': 'MATH101',
        'name': 'Discrete Mathematics',
        'description': 'Mathematical foundations for computer science',
        'credits': 3,
        'instructor': 'Dr. Michael Brown'
    },
    {
        'code': 'ENG101',
        'name': 'English Communication',
        'description': 'Professional communication and writing skills',
        'credits': 2,
        'instructor': 'Ms. Emily Davis'
    },
]

courses = []
for course_data in courses_data:
    course = Course.objects.create(**course_data)
    courses.append(course)
    print(f"  Created course: {course.code}")

# Create sample students
print("\nCreating students...")
students_data = [
    {
        'roll_number': 'STU001',
        'first_name': 'Rajesh',
        'last_name': 'Kumar',
        'email': 'rajesh.kumar@email.com',
        'phone': '+91-9876543210',
        'gender': 'M',
        'date_of_birth': datetime(2003, 5, 15).date(),
        'address': '123 Main Street, New Delhi',
        'is_active': True
    },
    {
        'roll_number': 'STU002',
        'first_name': 'Priya',
        'last_name': 'Singh',
        'email': 'priya.singh@email.com',
        'phone': '+91-9876543211',
        'gender': 'F',
        'date_of_birth': datetime(2003, 8, 22).date(),
        'address': '456 Oak Avenue, Mumbai',
        'is_active': True
    },
    {
        'roll_number': 'STU003',
        'first_name': 'Amit',
        'last_name': 'Patel',
        'email': 'amit.patel@email.com',
        'phone': '+91-9876543212',
        'gender': 'M',
        'date_of_birth': datetime(2004, 1, 10).date(),
        'address': '789 Pine Road, Bangalore',
        'is_active': True
    },
    {
        'roll_number': 'STU004',
        'first_name': 'Neha',
        'last_name': 'Gupta',
        'email': 'neha.gupta@email.com',
        'phone': '+91-9876543213',
        'gender': 'F',
        'date_of_birth': datetime(2003, 12, 5).date(),
        'address': '321 Elm Street, Hyderabad',
        'is_active': True
    },
    {
        'roll_number': 'STU005',
        'first_name': 'Vikram',
        'last_name': 'Verma',
        'email': 'vikram.verma@email.com',
        'phone': '+91-9876543214',
        'gender': 'M',
        'date_of_birth': datetime(2004, 3, 18).date(),
        'address': '654 Maple Drive, Pune',
        'is_active': True
    },
]

students = []
for student_data in students_data:
    student = Student.objects.create(**student_data)
    students.append(student)
    print(f"  Created student: {student.roll_number} - {student.full_name}")

# Create enrollments
print("\nCreating enrollments...")
for student in students:
    for course in courses:
        enrollment = Enrollment.objects.create(
            student=student,
            course=course
        )
        print(f"  Enrolled {student.roll_number} in {course.code}")

# Create attendance records
print("\nCreating attendance records...")
today = datetime.now().date()
attendance_statuses = ['P', 'A', 'L', 'E']

for student in students:
    for course in courses:
        # Create 20 attendance records for the last 20 days
        for i in range(20):
            date = today - timedelta(days=i)
            status = attendance_statuses[i % len(attendance_statuses)]
            
            attendance = Attendance.objects.create(
                student=student,
                course=course,
                date=date,
                status=status,
                remarks='Sample attendance record' if status == 'L' else None
            )
            
print(f"  Created 20 attendance records per student per course")

# Create performance records
print("\nCreating performance records...")
assessment_types = ['QUIZ', 'ASSIGNMENT', 'MIDTERM', 'PROJECT', 'FINAL']

for student in students:
    for course in courses:
        # Create 5 performance records
        for i, assessment_type in enumerate(assessment_types):
            date = today - timedelta(days=i*5)
            
            # Generate realistic marks
            marks_obtained = 70 + (student.id * 3 % 25)  # Vary by student
            total_marks = 100
            
            performance = Performance.objects.create(
                student=student,
                course=course,
                assessment_type=assessment_type,
                assessment_name=f'{assessment_type.title()} Exam {i+1}',
                marks_obtained=marks_obtained,
                total_marks=total_marks,
                date=date,
                remarks=f'Good performance in {assessment_type.lower()}' if marks_obtained > 75 else None
            )
            
print(f"  Created 5 performance records per student per course")

print("\n✅ Sample data created successfully!")
print("\nSummary:")
print(f"  - Students: {Student.objects.count()}")
print(f"  - Courses: {Course.objects.count()}")
print(f"  - Enrollments: {Enrollment.objects.count()}")
print(f"  - Attendance Records: {Attendance.objects.count()}")
print(f"  - Performance Records: {Performance.objects.count()}")
