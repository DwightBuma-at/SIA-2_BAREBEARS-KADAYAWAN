from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from myApp.models import (
    AdminInventory, Signup, Supplier, Booking, 
    PurchaseOrder, Tracking, Transaction, TransactionItem
)
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Populate database with sample static data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database with sample data...')

        # Create admin user
        if not Signup.objects.filter(email='admin@admin.com').exists():
            admin = Signup.objects.create_user(
                email='admin@admin.com',
                password='admin123'
            )
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin user: admin@admin.com'))

        # Create staff user
        if not Signup.objects.filter(email='staff@staff.com').exists():
            staff = Signup.objects.create_user(
                email='staff@staff.com',
                password='staff123'
            )
            staff.is_staff = False
            staff.save()
            self.stdout.write(self.style.SUCCESS(f'Created staff user: staff@staff.com'))

        # Create regular user
        if not Signup.objects.filter(email='user@gmail.com').exists():
            user = Signup.objects.create_user(
                email='user@gmail.com',
                password='user123'
            )
            self.stdout.write(self.style.SUCCESS(f'Created regular user: user@gmail.com'))

        # Create sample products (inventory)
        products_data = [
            {'name': 'Fried Chicken', 'price': Decimal('150.00'), 'stock': 50, 'image': '1.jpg'},
            {'name': 'Burger Steak', 'price': Decimal('120.00'), 'stock': 30, 'image': '2.jpg'},
            {'name': 'Spaghetti', 'price': Decimal('95.00'), 'stock': 40, 'image': '3.jpg'},
            {'name': 'Pancit Canton', 'price': Decimal('85.00'), 'stock': 35, 'image': '4.jpg'},
            {'name': 'Grilled Fish', 'price': Decimal('180.00'), 'stock': 25, 'image': '5.jpg'},
            {'name': 'Beef Tapa', 'price': Decimal('165.00'), 'stock': 20, 'image': '6.jpg'},
            {'name': 'Pork Adobo', 'price': Decimal('140.00'), 'stock': 30, 'image': '7.jpg'},
            {'name': 'Sisig', 'price': Decimal('155.00'), 'stock': 28, 'image': '8.jpg'},
            {'name': 'Lumpia', 'price': Decimal('75.00'), 'stock': 60, 'image': '9.jpg'},
            {'name': 'Halo-Halo', 'price': Decimal('90.00'), 'stock': 45, 'image': '10.jpg'},
            {'name': 'Chocolate Cake', 'price': Decimal('200.00'), 'stock': 15, 'image': 'art5.jpg'},
            {'name': 'Mango Graham', 'price': Decimal('110.00'), 'stock': 20, 'image': 'art6.jpg'},
            {'name': 'Leche Flan', 'price': Decimal('130.00'), 'stock': 18, 'image': 'art7.jpg'},
            {'name': 'Buko Pandan', 'price': Decimal('85.00'), 'stock': 25, 'image': 'art8.jpg'},
            {'name': 'Fresh Lumpia', 'price': Decimal('95.00'), 'stock': 30, 'image': 'art9.jpg'},
        ]

        for product_data in products_data:
            product, created = AdminInventory.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'image': f"inventory_images/{product_data['image']}"
                }
            )
            if created:
                self.stdout.write(f'  Created product: {product.name}')

        # Create suppliers
        suppliers_data = [
            {'name': 'Metro Mart Suppliers', 'contact_person': 'Juan Dela Cruz', 'contact_number': '09171234567'},
            {'name': 'Fresh Produce Co.', 'contact_person': 'Maria Santos', 'contact_number': '09181234567'},
            {'name': 'Quality Foods Inc.', 'contact_person': 'Pedro Garcia', 'contact_number': '09191234567'},
        ]

        for supplier_data in suppliers_data:
            supplier, created = Supplier.objects.get_or_create(
                name=supplier_data['name'],
                defaults={
                    'contact_person': supplier_data['contact_person'],
                    'contact_number': supplier_data['contact_number']
                }
            )
            if created:
                self.stdout.write(f'  Created supplier: {supplier.name}')

        # Create sample bookings
        user = Signup.objects.get(email='user@gmail.com')
        bookings_data = [
            {
                'customer_email': 'user@gmail.com',
                'booking_date': timezone.now().date() + timezone.timedelta(days=1),
                'people_count': 4,
                'estimated_time': '12:00:00',
                'status': 'Pending'
            },
            {
                'customer_email': 'user@gmail.com',
                'booking_date': timezone.now().date() + timezone.timedelta(days=2),
                'people_count': 2,
                'estimated_time': '18:00:00',
                'status': 'Approved'
            },
        ]

        for booking_data in bookings_data:
            booking, created = Booking.objects.get_or_create(
                customer_email=booking_data['customer_email'],
                booking_date=booking_data['booking_date'],
                defaults={
                    'people_count': booking_data['people_count'],
                    'estimated_time': booking_data['estimated_time'],
                    'status': booking_data['status'],
                    'booked_at': timezone.now()
                }
            )
            if created:
                self.stdout.write(f'  Created booking for {booking.customer_email}')

        # Create sample purchase orders
        purchase_orders_data = [
            {
                'supplier': 'Metro Mart Suppliers',
                'contact_person': 'Juan Dela Cruz',
                'contact_number': '09171234567',
                'product_name': 'Fried Chicken',
                'cost_price': Decimal('100.00'),
                'quantity_ordered': 50,
                'total_purchase_cost': Decimal('5000.00'),
                'payment_status': 'Paid',
                'payment_method': 'Cash',
                'order_status': 'Delivered'
            },
            {
                'supplier': 'Fresh Produce Co.',
                'contact_person': 'Maria Santos',
                'contact_number': '09181234567',
                'product_name': 'Grilled Fish',
                'cost_price': Decimal('120.00'),
                'quantity_ordered': 30,
                'total_purchase_cost': Decimal('3600.00'),
                'payment_status': 'Unpaid',
                'payment_method': 'Credit',
                'order_status': 'Unclaimed'
            },
        ]

        for po_data in purchase_orders_data:
            po, created = PurchaseOrder.objects.get_or_create(
                product_name=po_data['product_name'],
                supplier=po_data['supplier'],
                defaults=po_data
            )
            if created:
                self.stdout.write(f'  Created purchase order for {po.product_name}')

        # Create sample tracking/orders
        tracking_data = {
            'tracking_id': 'ORD-001-20250107',
            'customer_email': 'user@gmail.com',
            'customer_phone': '09171234567',
            'customer_address': '123 Main St, Davao City',
            'total_price': Decimal('500.00'),
            'shipping_subtotal': Decimal('50.00'),
            'payment_method': 'Cash On Delivery',
            'status': 'Pending',
            'source': 'ordering'
        }

        tracking, created = Tracking.objects.get_or_create(
            tracking_id=tracking_data['tracking_id'],
            defaults=tracking_data
        )

        if created:
            # Create a transaction for this tracking
            transaction = Transaction.objects.create(
                tracking=tracking,
                transaction_id=f'TXN-{timezone.now().timestamp()}',
                total_price=tracking_data['total_price'],
                payment_mode=tracking_data['payment_method']
            )

            # Add some items to the transaction
            chicken = AdminInventory.objects.get(name='Fried Chicken')
            sisig = AdminInventory.objects.get(name='Sisig')

            TransactionItem.objects.create(
                transaction=transaction,
                product_id=str(chicken.id),
                product_name=chicken.name,
                quantity=2,
                price=chicken.price,
                total_price=chicken.price * 2,
                image=f'/media/{chicken.image}'
            )

            TransactionItem.objects.create(
                transaction=transaction,
                product_id=str(sisig.id),
                product_name=sisig.name,
                quantity=1,
                price=sisig.price,
                total_price=sisig.price,
                image=f'/media/{sisig.image}'
            )

            self.stdout.write(f'  Created order: {tracking.tracking_id}')

        self.stdout.write(self.style.SUCCESS('\nDatabase populated successfully!'))
        self.stdout.write(self.style.SUCCESS('\nLogin credentials:'))
        self.stdout.write('  Admin: admin@admin.com / admin123')
        self.stdout.write('  Staff: staff@staff.com / staff123')
        self.stdout.write('  User: user@gmail.com / user123')

