class Product:

    # class variable 'product-catalog' will hold all instances of Product
    product_catalog = []

    # create instances of Product, check price and quantity,
    # then append to catalog
    def __init__(self, name: str, price: float, quantity=0) -> None:
        # there must be a price greater than 0
        assert price > 0, f"Price is {price} and must be greater than 0"
        # default for quantity is 0, must be greater than or equal to 0
        assert quantity >= 0, f"Quantity is {quantity} and must an int be " \
            "greater than or equal to 0"

        # set instance name, price, and quantity
        self._name = name
        self._price = price
        self.quantity = quantity

        # append to catalog
        Product.product_catalog.append(self)
