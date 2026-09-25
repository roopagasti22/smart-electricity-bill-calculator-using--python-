# Smart Electricity Bill Calculator

A beginner-friendly Python console program that calculates an electricity bill
from the customer's name, customer ID, and units consumed.

## Run the program

```bash
python smart_electricity_bill_calculator.py
```

## Program flow

1. `get_customer_details()` asks for the customer name, customer ID, and units consumed.
2. The program converts the units to a floating-point number and rejects negative or invalid values.
3. `calculate_bill()` selects the energy rate based on the unit slab:
	- 0 to 100 units: $2 per unit
	- 101 to 200 units: $4 per unit
	- 201 to 500 units: $6 per unit
	- Above 500 units: $8 per unit
4. A fixed service charge of $100 is added to the energy charge.
5. `display_bill()` prints the customer details, energy charge, service charge, and final amount.

The program uses only standard Python features: variables, strings, integers,
floats, functions, parameters, return values, input, type conversion,
comparison operators, conditional statements, and formatted output.