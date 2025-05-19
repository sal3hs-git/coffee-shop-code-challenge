class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0.")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order._all_orders.append(self)

