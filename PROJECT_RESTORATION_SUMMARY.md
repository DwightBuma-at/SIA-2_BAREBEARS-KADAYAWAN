# Django Project Restoration Summary

## What Was Done

Your Django project has been successfully restored and is now running with a fresh SQLite database populated with sample data!

### Changes Made

1. **Database Configuration Updated**
   - Changed from PostgreSQL/Supabase to SQLite
   - Location: `myProject/myProject/settings.py`
   - SQLite database file: `myProject/db.sqlite3`

2. **Database Structure Created**
   - Deleted old migration files
   - Generated fresh migrations
   - Applied all migrations successfully
   - Created all required tables for your models

3. **Sample Data Populated**
   - Created management command: `myProject/myApp/management/commands/populate_data.py`
   - Added sample data including:
     - **Users**: Admin, Staff, and Regular user accounts
     - **Products**: 15 food items with prices and stock
     - **Suppliers**: 3 suppliers with contact information
     - **Bookings**: 2 sample bookings
     - **Purchase Orders**: 2 sample orders
     - **Tracking Orders**: 1 sample customer order

### Login Credentials

Access your application with these test accounts:

- **Admin Account**
  - Email: `admin@admin.com`
  - Password: `admin123`
  - Access: Admin Dashboard, full privileges

- **Staff Account**
  - Email: `staff@staff.com`
  - Password: `staff123`
  - Access: Staff Dashboard

- **User Account**
  - Email: `user@gmail.com`
  - Password: `user123`
  - Access: User Dashboard

## How to Run the Server

The server is already running! If you need to restart it:

```powershell
cd "C:\Users\Dwight\Desktop\expr\DJANGO - CURRENT - WORKING - Copy"
python myProject\manage.py runserver
```

Then open your browser and go to:
- **http://127.0.0.1:8000** or **http://localhost:8000**

## Available Pages

Based on your URL structure, you can access:

- `/` - Landing page
- `/login/` - Login page
- `/signup/` - Sign up page
- `/admin-dashboard/` - Admin dashboard (requires admin@admin.com)
- `/staff-dashboard/` - Staff dashboard (requires staff@staff.com)
- `/user-dashboard/` - User dashboard (requires user@gmail.com)

### Admin Features
- `/admin-inventory/` - Manage inventory
- `/admin-ordering/` - View and manage orders
- `/admin-booking/` - Manage table bookings
- `/admin-pos/` - Point of Sale system
- `/admin-purchasing/` - Purchase order management

### Staff Features
- `/staff-ordering/` - Staff ordering interface
- `/staff-booking/` - Staff booking management
- `/staff-pos/` - Staff POS interface

### User Features
- `/user-ordering/` - Place orders
- `/user-booking/` - Book tables
- `/user-about/` - About page
- `/user-settings/` - User settings

## Sample Data Included

### Products (15 items)
- Fried Chicken (₱150.00, Stock: 50)
- Burger Steak (₱120.00, Stock: 30)
- Spaghetti (₱95.00, Stock: 40)
- Pancit Canton (₱85.00, Stock: 35)
- Grilled Fish (₱180.00, Stock: 25)
- Beef Tapa (₱165.00, Stock: 20)
- Pork Adobo (₱140.00, Stock: 30)
- Sisig (₱155.00, Stock: 28)
- Lumpia (₱75.00, Stock: 60)
- Halo-Halo (₱90.00, Stock: 45)
- Chocolate Cake (₱200.00, Stock: 15)
- Mango Graham (₱110.00, Stock: 20)
- Leche Flan (₱130.00, Stock: 18)
- Buko Pandan (₱85.00, Stock: 25)
- Fresh Lumpia (₱95.00, Stock: 30)

### Suppliers (3)
- Metro Mart Suppliers
- Fresh Produce Co.
- Quality Foods Inc.

### Sample Orders
- One customer order with tracking ID: ORD-001-20250107
- Items: 2x Fried Chicken, 1x Sisig

## Adding More Data

To add more sample data, you can:

1. Run the populate command again:
   ```powershell
   python myProject\manage.py populate_data
   ```

2. Use the admin interface (login as admin) to manually add data through the web interface

3. Use the Django admin panel at `/admin/` (you may need to create a Django superuser first)

## Troubleshooting

If you encounter any issues:

1. **Server not starting**: Make sure no other process is using port 8000
2. **Database issues**: Delete `myProject/db.sqlite3` and run migrations again:
   ```powershell
   python myProject\manage.py migrate
   python myProject\manage.py populate_data
   ```
3. **Static files not loading**: Run `python myProject\manage.py collectstatic`

## Important Notes

- The database is now SQLite (file-based) instead of PostgreSQL
- All original functionality should work as before
- The Supabase authentication integration in your code still uses Supabase for user verification
- Media files are stored in `myProject/media/inventory_images/`
- Static files are in `myProject/myApp/static/`

## Project Technology Stack

- **Backend**: Django 5.1.6, Python 3.13
- **Database**: SQLite3
- **API**: Django REST Framework
- **Frontend**: HTML, CSS, JavaScript
- **Auth**: Supabase (for signup/login verification)

Your project is now fully functional with static data and ready for development!

