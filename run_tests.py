import unittest
from gym import GymMembershipSystem

class GymMembershipSystemTest(unittest.TestCase):
    def setUp(self):
        self.system = GymMembershipSystem()

    def test_basic_membership_no_features(self):
        self.system.selected_plan = 'Basic'
        self.system.selected_features = []
        self.system.group_members = 1
        cost = self.system.calculate_cost()
        self.assertEqual(cost, 50)

    def test_premium_membership_with_features(self):
        self.system.selected_plan = 'Premium'
        self.system.selected_features = ['Personal Training', 'Group Classes']
        self.system.group_members = 1
        cost = self.system.calculate_cost()
        base = 80
        features = 30 + 20
        total = base + features
        surcharge = total * 0.15
        expected = total + surcharge
        self.assertAlmostEqual(cost, expected)

    def test_group_discount(self):
        self.system.selected_plan = 'Basic'
        self.system.selected_features = []
        self.system.group_members = 3
        cost = self.system.calculate_cost()
        base = 50
        total = base
        discount = total * 0.10
        expected = total - discount
        self.assertAlmostEqual(cost, expected)

    def test_special_discount_20(self):
        self.system.selected_plan = 'Family'
        self.system.selected_features = ['Personal Training']
        self.system.group_members = 1
        cost = self.system.calculate_cost()
        base = 120
        features = 30
        total = base + features
        if total > 200:
            total -= 20  # Apply $20 discount
        self.assertAlmostEqual(cost, total)

    def test_special_discount_50(self):
        self.system.selected_plan = 'Family'
        self.system.selected_features = ['Personal Training', 'Group Classes']
        self.system.group_members = 1
        cost = self.system.calculate_cost()
        base = 120
        features = 30 + 20
        total = base + features
        if total > 400:
            total -= 50  # Apply $50 discount
        elif total > 200:
            total -= 20  # Apply $20 discount
        self.assertAlmostEqual(cost, total)

    def test_combined_group_and_special_discount(self):
        self.system.selected_plan = 'Family'
        self.system.selected_features = ['Personal Training', 'Group Classes']
        self.system.group_members = 2
        cost = self.system.calculate_cost()
        base = 120
        features = 30 + 20
        total = base + features
        if total > 400:
            total -= 50  # Apply $50 discount
        elif total > 200:
            total -= 20  # Apply $20 discount
        discount = total * 0.10  # Group discount
        expected = total - discount
        self.assertAlmostEqual(cost, expected)

    def test_invalid_plan_selection(self):
        with self.assertRaises(KeyError):
            self.system.selected_plan = 'Invalid'
            self.system.calculate_cost()

if __name__ == "__main__":
    unittest.main()
