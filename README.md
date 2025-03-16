# Shopping Cart

## Description

This is a simple shopping cart application that allows users to add items to their cart and view the total cost of their items with applied discounts. The application is built in Python 2.7.
This is a project assignment for DataRock.


## Running the code:

1. Clone the repository
2. Run the following command in the terminal from the root directory of the project:
```
python shoppingcart/main.py
```

## Implementation

### `Item` class

The `Item` class is a simple class that represents an item in the store. It has the following attributes:
- `name`: The name of the item
- `price`: The price of the item
- `code`: The SKU code of the item

### `Discount` class

The `Discount` class is a simple class that represents a discount that can be applied to an item. There are 3 types of discounts:

1. Type 1: Get x number of items and pay only for y items. Example: 3 for 2 deal on Apple TVs
2. Type 2: Bulk discount. Example: If you buy more than 4 iPads, the price of each iPad is reduced to $499.99
3. Type 3: Free item. Example: Buy a MacBook Pro and get a free VGA adapter

### `Pricing Rules` class

The `PricingRules` class is a simple class that represents the pricing rules of the store. It has the following attributes:
- `catalogue`: A dictionary that maps the SKU code of an item to the item object
- `discounts`: A list of discount objects

### `Checkout` class

The `Checkout` class is the main class of the application. It has the following attributes:
- `pricing_rules`: An instance of the `PricingRules` class
- `cart`: A dictionary that maps the SKU code of an item to the quantity of that item in the cart


### Running the tests:

To run the tests, run the following command in the terminal from the root directory of the project:
```
python -m unittest discover tests
```

