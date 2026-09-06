# 💼 Online Job Portal

A Django-based web application designed to connect job seekers with employment opportunities across India.

The platform provides a simple interface where users can explore jobs, search and filter opportunities, view job details, apply for suitable positions, save jobs, and manage their applications. Recruiters can also post and manage job opportunities.

---

## ✨ Features

### 👩‍💻 For Job Seekers

- User registration and login
- Search and browse available jobs
- Search jobs by location
- Filter jobs by state and category
- Filter jobs by job type
- Filter jobs by experience level
- View complete job details
- Apply for jobs
- Save jobs for later
- View submitted applications

### 🏢 For Recruiters

- Post new job opportunities
- Manage posted jobs
- View job applications
- Manage recruitment-related information

### 🔎 Job Search

- India-wide demo job listings
- Location-based job search
- State and city-based filtering
- Category-based filtering
- Job type filtering
- Experience-level filtering
- Organized dropdown options

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML**
- **SQLite**
- **Django Templates**

---

## 📂 Project Structure

```text
online-job-portal/
│
├── jobs/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── views.py
│
├── online_job_portal/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── jobs.html
│   ├── job_detail.html
│   ├── login.html
│   ├── register.html
│   ├── post_job.html
│   ├── saved.html
│   └── my_applications.html
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Srishti-1111/online-job-portal.git
```

### 2. Open the project directory

```bash
cd online-job-portal
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 📊 Demo Job Database

The project includes a demo database containing India-wide academic/demo job listings across different:

- States
- Cities
- Categories
- Job types
- Experience levels

The demo listings are provided for educational and testing purposes and should not be considered verified live vacancies.

To load the demo job listings:

```bash
python manage.py seed_jobs
```

---

## 🎯 Project Objective

The objective of this project is to develop a simple and user-friendly online job portal that helps job seekers discover suitable employment opportunities and allows recruiters to post and manage job listings.

The project also demonstrates the practical use of Django for developing a database-driven web application.

---

## 🚀 Future Improvements

The project can be further enhanced with:

- Resume upload and management
- Email notifications for applications
- Recruiter dashboard
- Advanced job recommendation system
- Machine-learning-based job recommendations
- Real-time job data integration
- Improved authentication and security
- Responsive UI improvements
- Job application status tracking

---

## 📸 Screenshots

Screenshots of the application can be added here to demonstrate the major features of the project, including:

- Home page
- Job search page
- Job details page
- Login and registration
- Job application
- Saved jobs
- Recruiter job posting

---

## 👩‍💻 Author

**Srishti Agarwal**

BCA Student | Python & Django Developer

### GitHub

https://github.com/Srishti-1111

### LinkedIn

https://www.linkedin.com/in/srishti-agarwal-57782323/

---

## 📌 Disclaimer

This project has been developed for educational and demonstration purposes.

The job listings included in the demo database are not verified live vacancies.
