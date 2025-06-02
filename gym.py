class GymMembershipSystem:
    def __init__(self):
        self.membership_plans = {
            'Basic': 50,
            'Premium': 80,
            'Family': 120
        }
        self.additional_features = {
            'Personal Training': 30,
            'Group Classes': 20
        }
        self.premium_features = {
            'Exclusive Gym Access': 40,
            'Specialized Training Programs': 60
        }
        self.selected_plan = None
        self.selected_features = []
        self.is_premium = False
        self.group_members = 1

    def display_plans(self):
        print("Available Membership Plans:")
        for plan, cost in self.membership_plans.items():
            print(f" - {plan}: ${cost}")

    def select_plan(self):
        plan = input("Select a membership plan: ").title()
        if plan in self.membership_plans:
            self.selected_plan = plan
            self.is_premium = (plan == 'Premium')
        else:
            print("Invalid plan selected. Please try again.")
            self.select_plan()

    def add_features(self):
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f" - {feature}: ${cost}")
        while True:
            feature = input("Add a feature (type 'done' when finished): ").title()
            if feature == 'Done':
                break
            elif feature in self.additional_features:
                self.selected_features.append(feature)
            else:
                print("Invalid feature. Please select again.")

    def calculate_cost(self):
        base_cost = self.membership_plans[self.selected_plan]
        features_cost = sum(self.additional_features[f] for f in self.selected_features)
        total_cost = base_cost + features_cost

        # Premium Features Surcharge
        if self.is_premium:
            surcharge = total_cost * 0.15
            print(f"Applying 15% surcharge for premium features: +${surcharge:.2f}")
            total_cost += surcharge

        # Special Discounts
        if total_cost > 400:
            print("Applying special discount of $50")
            total_cost -= 50
        elif total_cost > 200:
            print("Applying special discount of $20")
            total_cost -= 20

        # Group Membership Discount
        if self.group_members >= 2:
            discount = total_cost * 0.10
            print(f"Applying 10% group discount: -${discount:.2f}")
            total_cost -= discount

        return total_cost

    def confirm_user(self):
        print(f"\nMembership Plan: {self.selected_plan}")
        print(f"Additional Features: {', '.join(self.selected_features) if self.selected_features else 'None'}")
        print(f"Number of Members: {self.group_members}")
        total = self.calculate_cost()
        print(f"Total Cost: ${total:.2f}")
        confirm = input("Confirm membership? (yes/no): ").lower()
        return total if confirm == 'yes' else -1

    def run(self):
        try:
            self.display_plans()
            self.select_plan()
            self.add_features()
            group_input = input("Number of members signing up together (1 for solo): ")
            if group_input.isdigit() and int(group_input) >= 1:
                self.group_members = int(group_input)
            else:
                print("Invalid number. Assuming solo membership.")
            result = self.confirm_user()
            print(f"Final Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    system = GymMembershipSystem()
    system.run()
