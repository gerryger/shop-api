from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load sample categories and products"

    def handle(self, *args, **options):
        data = {
            ("Electronics", "electronics"): [
                ("Wireless Earbuds", 499000, 50),
                ("Mechanical Keyboard", 1250000, 20),
                ("USB-C Hub", 350000, 100),
            ],
            ("Apparel", "apparel"): [
                ("Batik Shirt", 275000, 40),
                ("Running Shoes", 899000, 15),
            ],
            ("Home", "home"): [
                ("Coffee Grinder", 650000, 10),
                ("Desk Lamp", 210000, 30),
            ],
        }
        for (cat_name, slug), products in data.items():
            category, _ = Category.objects.get_or_create(slug=slug, defaults={"name": cat_name})
            for name, price, stock in products:
                Product.objects.get_or_create(
                    name=name, category=category, defaults={"price": price, "stock": stock}
                )
        self.stdout.write(self.style.SUCCESS(f"Seeded {Product.objects.count()} products"))
