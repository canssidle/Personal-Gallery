from django.test import TestCase

# Create your tests here.

from .models import Location,categories,Image
# import datetime as dt
# # Create your tests here.
# class LocationTestClass(TestCase):
#     def setUp(self):
#         self.Nyeri= Location(location='Nyeri')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.Nyeri,Location))

#     def tearDown(self):
#         Location.objects.all().delete()

#     def test_save_method(self):
#         self.Nyeri.save_location()
#         locations = Location.objects.all()
#         self.assertTrue(len(locations)>0)

#     def test_delete_method(self):
#         self.Nyeri.delete_location('Nyeri')
#         locations = Location.objects.all()
#         self.assertTrue(len(locations)==0)

# class categoriesTestClass(TestCase):
#     def setUp(self):
#         self.Food = categories(category='Food')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.Food,categories))

#     def tearDown(self):
#         categories.objects.all().delete()

#     def test_save_method(self):
#         self.Food.save_category()
#         category = categories.objects.all()
#         self.assertTrue(len(category)>0)

#     def test_delete_method(self):
#         self.Food.delete_category('Food')
#         category = categories.objects.all()
#         self.assertTrue(len(category)==0)

# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.test_category = categories(category=list('Travel'))
#         self.test_category.save_category()

#         self.location = Location(location="Nyeri")
#         self.location.save_location()

#         self.image = Image(id=1,title="Me",categories=self.test_category,location=self.location,)
#         self.image.save_image()

#     def tearDown(self):
#         categories.objects.all().delete()
#         Location.objects.all().delete()
#         Image.objects.all().delete()
