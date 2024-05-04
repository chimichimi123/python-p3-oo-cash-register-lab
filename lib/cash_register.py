#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity
        self.price_of_last_item = price
        self.name_of_last_item = title

    def apply_discount(self):
      if self.discount:
        self.total -= self.total * (self.discount / 100)
        self.total = round(self.total)
        print(f"After the discount, the total comes to ${self.total}.")
      else:
        print("There is no discount to apply.")

    def void_last_transaction(self):
      self.total -= self.last_transaction
      for _ in range(int(self.last_transaction / self.price_of_last_item)):
        self.items.remove(self.name_of_last_item)
