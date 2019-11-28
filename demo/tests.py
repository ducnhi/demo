from django.test import TestCase
from .models import OrderModels


class DemoTest(TestCase):
    def setUp(self):
        OrderModels.objects.create(
            seller_id=23,
            tracking_number='NH234',
            country="VN",
        )

    def test_string(self):
        order = OrderModels(seller_id=23, tracking_number='Md33')
        self.assertEqual(str(order), order.tracking_number)
        print('jk')

    def test_get_list(self):
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 24)
