# Student Tracker

A comprehensive, feature-rich Django-based web application for managing student attendance and academic performance with advanced analytics and reporting capabilities.

## 📸 Application Screenshots

### Dashboard
![Dashboard](https://user-images.githubusercontent.com/placeholder/dashboard.png)
The main overview displaying key statistics, active courses, real-time attendance, and quick action buttons.

### Attendance Tracking
![Attendance Tracking](https://user-images.githubusercontent.com/placeholder/attendance.png)
Comprehensive attendance management with date filtering, status categories, and record tracking.

### Performance & Grades
![Performance & Grades](https://user-images.githubusercontent.com/placeholder/performance.png)
Student performance records with filtering by student and course, and automatic grade calculation.

### Reports & Analytics
![Reports & Analytics](https://user-images.githubusercontent.com/placeholder/reports.png)
Advanced reporting with top performers, low attendance alerts, course-wise statistics, and export options.

### Students List
![Students List](https://user-images.githubusercontent.com/placeholder/students.png)
Complete student management with search functionality and enrollment details.

## ✨ Key Features

### Core Functionality
- **Student Management**: Add, view, edit, and manage comprehensive student information
- **Course Management**: Create and manage courses with instructor details and credit hours
- **Attendance Tracking**: Record daily attendance with multiple status options (Present/Absent/Late/Excused)
- **Performance Tracking**: Record grades and assessments with automatic calculation
- **Dashboard**: Interactive real-time statistics and quick actions
- **Reports & Analytics**: Comprehensive reporting with data visualization

### Advanced Capabilities
- Search and filter functionality across all modules
- Student-wise attendance and performance statistics
- Course-wise analytics and enrollment tracking
- Low attendance alerts and notifications
- Top performers identification
- Automatic grade calculation (A+ through F)
- Export reports to PDF and Excel
- Responsive Bootstrap 5 UI with mobile support
- Full Django admin interface

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python Django 5.2 |
| **Database** | SQLite3 |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **ORM** | Django ORM |
| **Image Handling** | Pillow |

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)
- ~100MB disk space for database

## 🚀 Installation & Setup

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd student-tracker
```

### Step 2: Create Virtual Environment
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account:
- **Username**: admin
- **Email**: admin@example.com
- **Password**: (enter your secure password)

### Step 6: Load Sample Data (Optional)
```bash
python manage.py shell < create_sample_data.py
```

This creates:
- 5 sample students
- 4 sample courses
- Enrollment records
- 20 attendance records per student per course
- 5 performance records per student per course

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Access the application at: **http://localhost:8000/**

## 📱 Application Usage

| Page | URL | Features |
|------|-----|----------|
| **Dashboard** | `/` | Overall statistics, recent records, quick actions |
| **Students** | `/students/` | View all students, search, add new students |
| **Student Details** | `/students/{roll_number}/` | Complete student info, enrollment, attendance, performance |
| **Attendance** | `/attendance/` | Record and filter attendance by date/course |
| **Performance** | `/performance/` | Track grades and assessments |
| **Reports** | `/reports/` | Top performers, low attendance alerts, course statistics |
| **Admin Panel** | `/admin/` | Full Django admin interface |

## 📊 Database Models

### Student
- Roll Number (unique)
- First & Last Name
- Email (unique)
- Phone, Gender, DOB
- Address, Photo (optional)
- Enrollment Date, Active Status

### Course
- Course Code (unique)
- Course Name, Description
- Credits, Instructor
- Active Status

### Enrollment
- Student (ForeignKey)
- Course (ForeignKey)
- Enrollment Date
- Unique constraint: (Student, Course)

### Attendance
- Student, Course (ForeignKey)
- Date, Status (Present/Absent/Late/Excused)
- Remarks (optional)
- Timestamps (created_at, updated_at)
- Unique constraint: (Student, Course, Date)

### Performance
- Student, Course (ForeignKey)
- Assessment Type (Quiz/Assignment/Midterm/Final/Project)
- Assessment Name, Marks Obtained, Total Marks
- Date, Remarks (optional)
- Computed: Percentage, Grade

## 📈 Grading System

Grades are calculated automatically based on percentage:

| Grade | Percentage Range |
|-------|-----------------|
| A+ | 90% and above |
| A | 80% to 89% |
| B | 70% to 79% |
| C | 60% to 69% |
| D | 50% to 59% |
| F | Below 50% |

## 📁 Project Structure

```
student_tracker/
├── manage.py                           # Django management script
├── requirements.txt                    # Project dependencies
├── create_sample_data.py              # Sample data generation script
├── README.md                          # Documentation
├── db.sqlite3                         # SQLite database
│
├── student_tracker/                   # Main project directory
│   ├── settings.py                   # Django settings
│   ├── urls.py                       # URL configuration
│   ├── asgi.py & wsgi.py            # ASGI/WSGI configuration
│
├── core/                             # Core Django app
│   ├── migrations/                   # Database migrations
│   ├── templates/core/               # HTML templates
│   │   ├── base.html                # Base template
│   │   ├── dashboard.html           # Dashboard page
│   │   ├── student_list.html        # Students listing
│   │   ├── student_detail.html      # Student details
│   │   ├── attendance.html          # Attendance page
│   │   ├── performance.html         # Performance page
│   │   └── reports.html             # Reports page
│   ├── models.py                     # Database models
│   ├── views.py                      # View functions
│   ├── urls.py                       # App URL routing
│   ├── admin.py                      # Admin configuration
│   └── tests.py                      # Test suite
│
├── static/                           # Static files (CSS, JS, images)
└── media/                            # User-uploaded files
```

## 🔧 Common Operations

### Add a Student
1. Navigate to `/admin/`
2. Click on "Students"
3. Click "Add Student"
4. Fill in the form with student details
5. Click "Save"

### Record Attendance
1. Go to `/admin/` → "Attendance" → "Add Attendance"
2. Select student, course, date, and status
3. Add remarks if necessary
4. Save the record

### Record Performance
1. Go to `/admin/` → "Performance" → "Add Performance"
2. Select student, course, and assessment type
3. Enter marks obtained and total marks
4. Grade is calculated automatically
5. Save the record

### Generate Reports
1. Navigate to `/reports/`
2. View top performers and low attendance alerts
3. Analyze course-wise statistics
4. Export to PDF/Excel as needed

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| "No such table" error | Run `python manage.py migrate` |
| Static files not loading | Create static folder and run `python manage.py collectstatic --noinput` |
| ImageField error | Install Pillow: `pip install Pillow` |
| ModuleNotFoundError | Install requirements: `pip install -r requirements.txt` |
| Port 8000 already in use | Use `python manage.py runserver 8001` |

## 🚀 Future Enhancements

- Email notifications for low attendance
- SMS alerts to parents/guardians
- Student login portal
- Performance trend analysis with charts
- Bulk upload functionality (CSV/Excel)
- REST API endpoints
- Two-factor authentication
- Assignment submission tracking
- GPA calculation and transcripts
- Advanced data export options

## 🤝 Contributing

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes and test thoroughly
3. Submit a pull request with detailed description
4. Ensure code follows project conventions

## 📄 License

This project is open source and available for educational purposes.

## 💬 Support

For issues, questions, or suggestions:

1. Check the troubleshooting section above
2. Review the [Django documentation](https://docs.djangoproject.com/)
3. Open an issue in the project repository

## 📦 Version Information

| Component | Version |
|-----------|---------|
| Application | 1.0.0 |
| Last Updated | January 2026 |
| Django | 5.2.10 |
| Python | 3.8+ |

---

**Happy Tracking!** 🎓 For more information, check the complete documentation in the project repository.
