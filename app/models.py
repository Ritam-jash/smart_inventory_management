class Product:
    def __init__(self, name, quantity, price, supplier_id):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.supplier_id = supplier_id

class Supplier:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

class Order:
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
