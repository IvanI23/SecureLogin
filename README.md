# 🔐 Django Authentication System with Email Verification & Password Reset

A login system built using the Django framework, featuring:

- ✅ Email verification before login  
- 🔒 Password reset capabilities  
- 🎨 Clean, intuitive UI with a focus on user experience (UX)  
- 🛡️ Secure user management via Django best practices  

---

## 🧩 Features

- 🔐 **User Registration & Login**
- 📧 **Email Verification via 6-digit Code**
- 🔁 **Secure Password Reset with Email Link**
- ✅ **Email Verification Status Tracking**
- 🛠️ **Admin Panel Support**
- 🧼 **Minimal, Clean Front-End Templates**

---

## ⚙️ Setup Instructions

### 1. Clone the Project
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install Django>=4.2,<5.0
pip install python-dotenv
```

### 4. Configure Email Settings

📌 **IMPORTANT:** Replace with your SMTP credentials in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

---
