from django.core.management.base import BaseCommand
from myApp.models import Signup


class Command(BaseCommand):
    help = 'Check user accounts and their login credentials'

    def handle(self, *args, **kwargs):
        self.stdout.write('Checking user accounts...\n')

        users = Signup.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found in database!'))
            return

        for user in users:
            self.stdout.write(f'\nEmail: {user.email}')
            self.stdout.write(f'Is Staff: {user.is_staff}')
            self.stdout.write(f'Is Superuser: {user.is_superuser}')
            self.stdout.write(f'Has usable password: {user.has_usable_password()}')
            
            # Test password
            if user.email == 'admin@admin.com':
                if user.check_password('admin123'):
                    self.stdout.write(self.style.SUCCESS('[OK] Admin password is correct'))
                else:
                    self.stdout.write(self.style.ERROR('[FAIL] Admin password is WRONG'))
            elif user.email == 'staff@staff.com':
                if user.check_password('staff123'):
                    self.stdout.write(self.style.SUCCESS('[OK] Staff password is correct'))
                else:
                    self.stdout.write(self.style.ERROR('[FAIL] Staff password is WRONG'))
            elif user.email == 'user@gmail.com':
                if user.check_password('user123'):
                    self.stdout.write(self.style.SUCCESS('[OK] User password is correct'))
                else:
                    self.stdout.write(self.style.ERROR('[FAIL] User password is WRONG'))

        self.stdout.write(self.style.SUCCESS(f'\nTotal users: {users.count()}'))

