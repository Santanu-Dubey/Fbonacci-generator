def calculate_rent(total_rent, electricity_bill, maintenance_charge, roommates):
    """
    Calculate total expense and rent per person.
    """

    total_expense = total_rent + electricity_bill + maintenance_charge
    rent_per_person = total_expense / roommates

    return total_expense, rent_per_person


def main():

    print("=" * 45)
    print("          RENT CALCULATOR")
    print("=" * 45)

    try:
        total_rent = float(input(" Enter Monthly Rent (₹): "))
        electricity_bill = float(input(" Enter Electricity Bill (₹): "))
        maintenance_charge = float(input("🛠Enter Maintenance Charge (₹): "))
        roommates = int(input(" Number of Roommates: "))

        if total_rent < 0 or electricity_bill < 0 or maintenance_charge < 0:
            print("\n❌ Expenses cannot be negative.")
            return

        if roommates <= 0:
            print("\n❌ Number of roommates must be greater than 0.")
            return

        total_expense, rent_per_person = calculate_rent(
            total_rent,
            electricity_bill,
            maintenance_charge,
            roommates
        )

        print("\n" + "=" * 45)
        print("          MONTHLY EXPENSE SUMMARY")
        print("=" * 45)
        print(f" Rent                 : ₹{total_rent:.2f}")
        print(f" Electricity Bill     : ₹{electricity_bill:.2f}")
        print(f" Maintenance Charge   : ₹{maintenance_charge:.2f}")
        print("-" * 45)
        print(f" Total Expense        : ₹{total_expense:.2f}")
        print(f" Rent Per Person      : ₹{rent_per_person:.2f}")
        print("=" * 45)

    except ValueError:
        print("\n❌ Invalid input! Please enter numeric values.")


if __name__ == "__main__":
    main()