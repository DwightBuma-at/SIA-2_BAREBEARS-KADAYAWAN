# How to Run Your Django Server

## Quick Start - Option 1 (Recommended)
Open PowerShell/Terminal in the project root folder and run:
```powershell
cd myProject
python manage.py runserver
```

## Quick Start - Option 2
Run from the project root without changing directories:
```powershell
python myProject\manage.py runserver
```

## After Starting the Server

You should see output like:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 07, 2025 - 12:00:00
Django version 5.1.6, using settings 'myProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Access Your Application

Open your browser and go to:
- **http://127.0.0.1:8000/** or **http://localhost:8000/**

## To Stop the Server

Press **CTRL+C** in the terminal where the server is running

## Troubleshooting

**Error: "python: can't open file 'manage.py'"**
- Solution: Make sure you're in the `myProject` folder or use `python myProject\manage.py runserver`

**Error: "Port 8000 is already in use"**
- Solution: Either stop the existing server or use a different port:
  ```powershell
  cd myProject
  python manage.py runserver 8080
  ```
  Then access at http://localhost:8080/

**Error: "No module named 'django'"**
- Solution: Install Django:
  ```powershell
  pip install django djangorestframework pillow
  ```

## Login Credentials

- **Admin**: admin@admin.com / admin123
- **Staff**: staff@staff.com / staff123  
- **User**: user@gmail.com / user123

## Your Project Structure
```
DJANGO - CURRENT - WORKING - Copy/
├── myProject/              ← This is where manage.py is located
│   ├── manage.py          ← The file you need to run
│   ├── myApp/
│   ├── myProject/
│   └── db.sqlite3
├── myVenv/
└── README.md
```

Always run `python manage.py runserver` from inside the **myProject** folder!

