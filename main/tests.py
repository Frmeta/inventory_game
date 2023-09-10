from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    # Test dari Tutorial
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
   
    # Test selain dari Tutorial

    # def test_admin_url_is_exist(self):
    #     response = Client().get('/admin/')
    #     self.assertEqual(response.status_code, 200)

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)

    @classmethod
    def setUpTestData(cls):
        # Setu up data yang diperlukan
        Item.objects.create(name="Dompet", amount=1, description="Tempat menyimpan uang dan kartu KTM")
    
    def test_item_name_label(self):
        # memeriksa label nama dari Item
        name = Item.objects.get(id=1)._meta.get_field('name').verbose_name
        self.assertEqual(name, 'name')
    
    def test_first_name_max_length(self):
        # memeriksa banyak karakter maksimal nama dari Item
        max_length = Item.objects.get(id=1)._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)
    
    def test_item_as_string(self):
        # memeriksa apakah functin __str__ pada Item sudah benar
        first_item = Item.objects.get(id=1)
        expected_item_name = f'{first_item.name}x{first_item.amount}'
        self.assertEqual(str(first_item), expected_item_name)


# Referensi
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing