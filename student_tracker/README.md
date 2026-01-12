# Student Attendance and Performance Tracker

A comprehensive Django-based web application for managing student attendance and academic performance.

## Features

### Core Features
- **Student Management**: Add, view, edit, and manage student information
- **Course Management**: Create and manage courses with instructors and credits
- **Attendance Tracking**: Track daily attendance with multiple status options (Present/Absent/Late/Excused)
- **Performance Tracking**: Record grades and assessments with automatic grade calculation
- **Dashboard**: Interactive dashboard with real-time statistics
- **Reports & Analytics**: Generate comprehensive reports and analytics
- **Admin Panel**: Full Django admin interface for data management

### Key Capabilities
- Search and filter functionality across all modules
- Student-wise attendance and performance statistics
- Course-wise analytics and enrollment tracking
- Low attendance alerts
- Top performers identification
- Automatic grade calculation (A+, A, B, C, D, F)
- Responsive Bootstrap 5 UI
- Mobile-friendly design

## Tech Stack

- **Backend**: Python Django 5.2
- **Database**: SQLite3 (default)
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **ORM**: Django ORM
- **Image Handling**: Pillow

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

### Step 1: Create Virtual Environment

```bash
python -m venv env
env\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account:
- Username: admin
- Email: admin@example.com
- Password: (enter your secure password)

### Step 5: Load Sample Data (Optional)

```bash
python manage.py shell < create_sample_data.py
```

This will create:
- 5 sample students
- 4 sample courses
- Enrollment records
- 20 attendance records per student per course
- 5 performance records per student per course

### Step 6: Run Development Server

```bash
python manage.py runserver
```

The application will be available at: `http://localhost:8000/`

## Usage

### Access the Application

1. **Dashboard**: http://localhost:8000/
   - View overall statistics
   - See recent students and performance records
   - Quick access to admin functions

2. **Students**: http://localhost:8000/students/
   - View all students
   - Search students by name, roll number, or email
   - Click on a student to view detailed information

3. **Student Details**: http://localhost:8000/students/{roll_number}/
   - View complete student information
   - Enrollment status
   - Attendance statistics
   - Performance records

4. **Attendance**: http://localhost:8000/attendance/
   - View attendance records
   - Filter by date and course
   - Edit attendance records

5. **Performance**: http://localhost:8000/performance/
   - View performance records
   - Filter by student and course
   - Track grades and assessments

6. **Reports**: http://localhost:8000/reports/
   - Top performers list
   - Low attendance alerts
   - Course-wise statistics

7. **Admin Panel**: http://localhost:8000/admin/
   - Full admin interface
   - Add/edit/delete students, courses, attendance, and performance
   - Manage enrollments
   - Apply filters and search

## Project Structure

```
student_tracker/
├── manage.py                           # Django management script
├── requirements.txt                    # Project dependencies
├── create_sample_data.py              # Sample data generation script
├── README.md                          # This file
├── db.sqlite3                         # SQLite database
│
├── student_tracker/                   # Main project directory
│   ├── __init__.py
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── core/                             # Core Django app
│   ├── migrations/                   # Database migrations
│   ├── templates/core/               # HTML templates
│   │   ├── base.html                # Base template
│   │   ├── dashboard.html           # Dashboard page
│   │   ├── student_list.html        # Students listing
│   │   ├── student_detail.html      # Individual student details
│   │   ├── attendance.html          # Attendance page
│   │   ├── performance.html         # Performance page
│   │   └── reports.html             # Reports page
│   │
│   ├── __init__.py
│   ├── admin.py                      # Admin interface configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Database models
│   ├── urls.py                       # App URL configuration
│   ├── views.py                      # View functions
│   └── tests.py                      # Tests
│
├── static/                           # Static files (CSS, JS, images)
└── media/                            # User-uploaded media files
```

## Database Models

### Student
- Roll Number (unique)
- Name (First & Last)
- Email (unique)
- Phone
- Gender
- Date of Birth
- Address
- Photo (optional)
- Enrollment Date
- Active Status

### Course
- Course Code (unique)
- Course Name
- Description
- Credits
- Instructor
- Active Status

### Enrollment
- Student (ForeignKey)
- Course (ForeignKey)
- Enrollment Date
- Unique constraint: (Student, Course)

### Attendance
- Student (ForeignKey)
- Course (ForeignKey)
- Date
- Status (Present/Absent/Late/Excused)
- Remarks (optional)
- Timestamps (created_at, updated_at)
- Unique constraint: (Student, Course, Date)

### Performance
- Student (ForeignKey)
- Course (ForeignKey)
- Assessment Type (Quiz/Assignment/Midterm/Final/Project)
- Assessment Name
- Marks Obtained
- Total Marks
- Date
- Remarks (optional)
- Computed: Percentage, Grade

## Common Operations

### Add a Student via Admin Panel
1. Go to `/admin/`
2. Click on "Students"
3. Click "Add Student"
4. Fill in the form
5. Click "Save"

### Record Attendance
1. Go to `/admin/` → "Attendance" → "Add Attendance"
2. Select student, course, date, and status
3. Save the record

### Record Performance
1. Go to `/admin/` → "Performance" → "Add Performance"
2. Select student, course, assessment type
3. Enter marks obtained and total marks
4. Grade is calculated automatically
5. Save the record

### View Student Details
1. Go to `/students/`
2. Click on the student's name or "View" button
3. See complete student information, attendance, and performance data

### Generate Reports
1. Go to `/reports/`
2. View top performers, low attendance alerts, and course statistics

## Grades

Grades are calculated automatically based on percentage:
- A+ : 90% and above
- A  : 80% to 89%
- B  : 70% to 79%
- C  : 60% to 69%
- D  : 50% to 59%
- F  : Below 50%

## User Interface Features

### Dashboard
The main overview page displaying key statistics and quick actions:
- **Total Students**: Monitor total student enrollment
- **Active Courses**: Track active courses
- **Today's Attendance**: View real-time attendance tracking
- **Recent Records**: Quick access to recent performance entries
- **Quick Actions**: Buttons to quickly Add Student, Add Course, Record Attendance, and Record Performance
- **Recent Students**: View newly enrolled students
- **Recent Performance Records**: Display latest performance entries

### Students List
Manage and search student information:
- View all enrolled students with detailed information
- Search functionality by name, roll number, or email
- Add new students with the "Add Student" button
- Click on student to view complete details, attendance, and performance data
- Empty state guidance for new databases

### Attendance Tracking
Track and monitor student attendance with comprehensive statistics:
- **Attendance Records**: View attendance entries filtered by date and course
- **Status Categories**:
  - Total Records: Overall attendance entries
  - Present: Students marked present
  - Absent: Students marked absent
  - Late/Excused: Students marked late or with excused absence
- Date and course filtering options
- Record new attendance entries
- Filter and search capabilities

### Performance & Grades
Monitor student academic performance:
- **Performance Records**: Track grades and performance metrics
- Filter by student and course
- Record new performance entries
- View performance data by individual student or course-wise
- Track academic progress over time
- Automatic grade calculation (A+, A, B, C, D, F)

### Reports & Analytics
Comprehensive reporting and data analysis:
- **Top Performers**: Identify and recognize high-performing students
- **Low Attendance Alert**: Automatic alerts for students with attendance concerns
- **Course-wise Statistics**: Detailed statistics broken down by course
- **Export & Share Options**:
  - Export to PDF
  - Export to Excel
  - Print Report

### Admin Panel
Administrative controls and system management:
- Full Django admin interface for complete data control
- Add, edit, and delete students, courses, attendance, and performance records
- Manage course enrollments
- Apply filters and search across all modules
- Advanced data management capabilities

## API Endpoints

The application provides the following endpoints:

| Endpoint | View | Description |
|----------|------|-------------|
| `/` | Dashboard | Main dashboard with statistics |
| `/students/` | Student List | All students with search |
| `/students/<roll_number>/` | Student Detail | Individual student details |
| `/attendance/` | Attendance | Attendance records with filters |
| `/performance/` | Performance | Performance records with filters |
| `/reports/` | Reports | Various reports and analytics |
| `/admin/` | Django Admin | Full admin panel |

## Troubleshooting

### Issue: "No such table" error
**Solution**: Run migrations again:
```bash
python manage.py migrate
```

### Issue: Static files not loading
**Solution**: Create static folder and collect static files:
```bash
mkdir static
python manage.py collectstatic --noinput
```

### Issue: ImageField error
**Solution**: Install Pillow:
```bash
pip install Pillow
```

### Issue: "ModuleNotFoundError"
**Solution**: Install requirements:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- PDF report generation
- Email notifications for low attendance
- SMS alerts
- Student login portal
- Performance trend analysis
- Export to Excel/CSV
- Bulk upload functionality
- REST API endpoints
- Two-factor authentication
- Assignment submission tracking
- GPA calculation
- Transcript generation

## Contributing

To contribute to this project:
1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is open source and available for educational purposes.

## Support

For issues, questions, or suggestions:
1. Check the troubleshooting section
2. Review the Django documentation: https://docs.djangoproject.com/
3. Open an issue in the project repository

## Version

**Current Version**: 1.0.0
**Last Updated**: January 2026
**Django Version**: 5.2.10
**Python Version**: 3.8+

---

**Happy Tracking!** 🎓
