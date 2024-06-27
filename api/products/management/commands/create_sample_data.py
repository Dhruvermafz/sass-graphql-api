from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Creates sample data for products'

    def handle(self, *args, **kwargs):
        Product.objects.create(
            name='Product A',
            description='This is product A',
            price=19.99,
            stock=100
        )

        Product.objects.create(
            name='Product B',
            description='This is product B',
            price=29.99,
            stock=50
        )

        Product.objects.create(
            name='Product C',
            description='This is product C',
            price=39.99,
            stock=75
        )

        Product.objects.create(
            name='Product D',
            description='This is product D',
            price=49.99,
            stock=25
        )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully'))
