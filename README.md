# SIA-2 BAREBEARS KADAYAWAN

A comprehensive restaurant management system built with Django, featuring inventory management, order tracking, booking system, and point-of-sale functionality.

## 🍽️ Features

### Admin Dashboard
- **Inventory Management** - Add, edit, and track product stock
- **Order Management** - View and manage online orders
- **Booking System** - Handle table reservations
- **POS System** - Point of sale for in-store orders
- **Purchase Orders** - Manage supplier orders
- **Reports & Logs** - View transaction history

### Staff Dashboard
- **POS Interface** - Process in-store orders
- **Booking Management** - Handle table reservations
- **Order Tracking** - Monitor order status

### User Dashboard
- **Online Ordering** - Browse menu and place orders
- **Table Booking** - Reserve tables online
- **Order Tracking** - Track order status
- **Order History** - View past orders

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.1.6
- SQLite3

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/DwightBuma-at/SIA-2_BAREBEARS-KADAYAWAN.git
   cd SIA-2_BAREBEARS-KADAYAWAN
   ```

2. **Create virtual environment**
   ```bash
   python -m venv myVenv
   # Windows
   myVenv\Scripts\activate
   # Linux/Mac
   source myVenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework pillow supabase
   ```

4. **Run migrations**
   ```bash
   cd myProject
   python manage.py migrate
   ```

5. **Populate sample data**
   ```bash
   python manage.py populate_data
   ```

6. **Start the server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open browser: http://localhost:8000

## 🔐 Login Credentials

### Admin Account
- **Email:** admin@admin.com
- **Password:** admin123
- **Access:** Full system access

### Staff Account
- **Email:** staff@staff.com
- **Password:** staff123
- **Access:** Staff functions

### User Account
- **Email:** user@gmail.com
- **Password:** user123
- **Access:** Customer features

## 🛠️ Technology Stack

- **Backend:** Django 5.1.6, Python 3.13
- **Database:** SQLite3 (development)
- **API:** Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Custom User Model
- **Image Handling:** Pillow

## 📁 Project Structure

```
SIA-2_BAREBEARS-KADAYAWAN/
├── myProject/                 # Django project
│   ├── myApp/                # Main application
│   │   ├── models.py         # Database models
│   │   ├── views.py          # View functions
│   │   ├── urls.py           # URL routing
│   │   ├── templates/        # HTML templates
│   │   ├── static/           # CSS, JS, images
│   │   └── management/       # Custom commands
│   ├── myProject/            # Project settings
│   │   ├── settings.py       # Configuration
│   │   └── urls.py           # Main URL config
│   ├── manage.py             # Django management
│   └── db.sqlite3            # Database
├── myVenv/                   # Virtual environment
└── README.md                 # This file
```

## 🎯 Key Models

- **AdminInventory** - Product catalog
- **Signup** - User accounts
- **Tracking** - Order tracking
- **Transaction** - Order transactions
- **Booking** - Table reservations
- **PurchaseOrder** - Supplier orders
- **Supplier** - Supplier information

## 🔧 Custom Management Commands

- `populate_data` - Add sample data to database
- `check_users` - Verify user accounts and passwords

## 🌐 Deployment Options

Since this is a Django application, it cannot be hosted on GitHub Pages (which only supports static sites). Consider these alternatives:

### Free Hosting Options
1. **Railway** - Easy Django deployment
2. **Render** - Free tier available
3. **Heroku** - Popular platform (limited free tier)
4. **PythonAnywhere** - Beginner-friendly

### Paid Hosting Options
1. **DigitalOcean** - VPS hosting
2. **AWS** - Scalable cloud hosting
3. **Google Cloud** - Enterprise solutions

## 📝 Sample Data

The application comes with pre-populated data:
- 15 food products with prices and stock
- 3 suppliers with contact information
- Sample bookings and orders
- Test user accounts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes as part of SIA-2 coursework.

## 👨‍💻 Author

**Dwight Buma-at**
- GitHub: [@DwightBuma-at](https://github.com/DwightBuma-at)

## 🎓 Course Information

**SIA-2 (System Integration and Architecture 2)**
- **Project:** BAREBEARS KADAYAWAN Restaurant Management System
- **Technology:** Django Web Framework
- **Purpose:** Educational project demonstrating full-stack web development

---

**Note:** This is a local development setup. For production deployment, additional configuration for security, database, and static files is required.