from django.test import TestCase
from restaurant.models import MenuTable


class MenuTableTest(TestCase):
    def test_get_item(self):
        item = MenuTable.objects.create(title='Cake', price=200, inventory=100)
        # self.assertEqual(item, "Cake : 200")

        itemstr = item.get_item()
        self.assertEqual(itemstr, "Cake : 200")
