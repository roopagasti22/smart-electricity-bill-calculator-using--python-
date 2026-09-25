def get_customer_details():
    """Get and validate the customer's information."""
    customer_name = input("Enter customer name: ")
    customer_id = input("Enter customer ID: ")

    while True:
        try:
            units_consumed = float(input("Enter electricity units consumed: "))

            if units_consumed < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units_consumed
        except ValueError:
            print("Please enter a valid number for units consumed.")


def calculate_bill(units_consumed):
    """Calculate the energy charge, service charge, and final bill amount."""
    if units_consumed <= 100:
        energy_charge = units_consumed * 2
    elif units_consumed <= 200:
        energy_charge = units_consumed * 4
    elif units_consumed <= 500:
        energy_charge = units_consumed * 6
    else:
        energy_charge = units_consumed * 8

    service_charge = 100.0
    final_amount = energy_charge + service_charge
    return energy_charge, service_charge, final_amount


def display_bill(customer_name, customer_id, units_consumed, energy_charge,
                 service_charge, final_amount):
    """Display the customer's electricity bill."""
    print("\n" + "=" * 40)
    print("          SMART ELECTRICITY BILL")
    print("=" * 40)
    print(f"Customer Name   : {customer_name}")
    print(f"Customer ID     : {customer_id}")
    print(f"Units Consumed  : {units_consumed:.2f}")
    print("-" * 40)
    print(f"Energy Charge   : ${energy_charge:.2f}")
    print(f"Service Charge  : ${service_charge:.2f}")
    print("-" * 40)
    print(f"Final Amount    : ${final_amount:.2f}")
    print("=" * 40)


def main():
    customer_name, customer_id, units_consumed = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units_consumed)
    display_bill(customer_name, customer_id, units_consumed, energy_charge,
                 service_charge, final_amount)


if __name__ == "__main__":
    main()