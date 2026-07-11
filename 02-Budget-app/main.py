class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    spent = []
    total_spent = 0

    for category in categories:
        amount = 0
        for item in category.ledger:
            if item["amount"] < 0:
                amount += -item["amount"]
        spent.append(amount)
        total_spent += amount

    percentages = []
    for amount in spent:
        percentages.append(int((amount / total_spent) * 10) * 10)

    chart = title

    for index in range(100, -1, -10):
        chart += f"{index:>3}|"
        for percent in percentages:
            if percent >= index:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)

    for index in range(max_length):
        chart += "     "
        for category in categories:
            if index < len(category.name):
                chart += category.name[index] + "  "
            else:
                chart += "   "
        if index != max_length - 1:
            chart += "\n"

    return chart
