from django.contrib import admin
from .models import Student, Course, Enrollment, Attendance, Performance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'full_name', 'email', 'gender', 
                    'enrollment_date', 'is_active', 'attendance_percentage']
    list_filter = ['gender', 'is_active', 'enrollment_date']
    search_fields = ['roll_number', 'first_name', 'last_name', 'email']
    list_per_page = 20
    ordering = ['roll_number']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('roll_number', 'first_name', 'last_name', 'email')
        }),
        ('Personal Details', {
            'fields': ('phone', 'gender', 'date_of_birth', 'address', 'photo')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'credits', 'instructor', 'is_active']
    list_filter = ['is_active', 'credits']
    search_fields = ['code', 'name', 'instructor']
    list_per_page = 20


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date']
    list_filter = ['enrollment_date', 'course']
    search_fields = ['student__first_name', 'student__last_name', 'course__name']
    autocomplete_fields = ['student', 'course']
    date_hierarchy = 'enrollment_date'


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date', 'status', 'created_at']
    list_filter = ['status', 'date', 'course']
    search_fields = ['student__first_name', 'student__last_name', 'course__code']
    date_hierarchy = 'date'
    list_per_page = 50
    
    fieldsets = (
        ('Attendance Details', {
            'fields': ('student', 'course', 'date', 'status')
        }),
        ('Additional Information', {
            'fields': ('remarks',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'assessment_type', 'assessment_name', 
                    'marks_obtained', 'total_marks', 'percentage', 'grade', 'date']
    list_filter = ['assessment_type', 'date', 'course']
    search_fields = ['student__first_name', 'student__last_name', 
                    'course__code', 'assessment_name']
    date_hierarchy = 'date'
    list_per_page = 50
    
    fieldsets = (
        ('Student & Course', {
            'fields': ('student', 'course')
        }),
        ('Assessment Details', {
            'fields': ('assessment_type', 'assessment_name', 'date')
        }),
        ('Marks', {
            'fields': ('marks_obtained', 'total_marks')
        }),
        ('Remarks', {
            'fields': ('remarks',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = []
    
    def percentage(self, obj):
        return f"{obj.percentage}%"
    
    def grade(self, obj):
        return obj.grade