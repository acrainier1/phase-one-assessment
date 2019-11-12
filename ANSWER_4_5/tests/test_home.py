import unittest
from app import location

P = location.Person
H = location.Home
B = location.Business

class TestHome(unittest.TestCase):

    def testAdd_resident(self):
        js = P(first_name="John", last_name="Smith")
        ms = P(first_name="Mary", last_name="Sue")
        house = H(address="456 ghjk")
        house.add_resident(js)
        house.add_resident(ms)

        residents = house.residents
        self.assertEqual(len(residents), 2, msg="add_residents() should append 2 person objects")


    def testResident_names(self):
        js = P(first_name="John", last_name="Smith")
        ms = P(first_name="Mary", last_name="Sue")
        house = H(address="456 ghjk")
        house.add_resident(js)
        house.add_resident(ms)

        residents = house.resident_names()
        self.assertTrue(isinstance(residents[0], str), msg="resident_names() should create list of strings")


    def test__repr_home(self):
        house = H(address="456 ghjk")
        self.assertTrue(isinstance(house.__repr__(), str), msg="__repr__should return a string")


    def testAdd_employee(self):
        js = P(first_name="John", last_name="Smith")
        ms = P(first_name="Mary", last_name="Sue")

        biz = B(name="StoreRUS", address="123 hj")
        biz.add_employee(js)
        biz.add_employee(ms)
        self.assertTrue(isinstance(biz.employees, list), msg="add_employee() should create a list")
        self.assertTrue(isinstance(biz.employees[0].first_name, str), msg="resident_names() should create list of strings")


    def test__repr_business(self):
        biz = B(name="StoreRUS", address="123 hj")
        self.assertTrue(isinstance(biz.__repr__(), str), msg="__repr__should return a string")


