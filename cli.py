from models import OrderORM, CustomerORM

def display_menu():
    print("Please select an option:")
    print("1. Create Order")
    print("2. Delete Order")
    print("3. Display All Orders")
    print("4. Find Order by Customer ID")
    print("5. Create Customer")
    print("6. Delete Customer")
    print("7. Display All Customers")
    print("8. Find Customer by Name")
    print("9. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            customer_id = int(input("Enter customer id: "))
            order_date = input("Enter order date: ")
            total = float(input("Enter total: "))
            OrderORM.create(customer_id, order_date, total)
            print("Order was successfully placed.🥳")
        elif choice == "2":
            id = int(input("Enter order id: "))
            OrderORM.delete(id)
            print("The order was deleted!!")
        elif choice == "3":
            orders = OrderORM.get_all()
            for order in orders:
                print(order)
        elif choice == "4":
            customer_id = int(input("Enter customer id: "))
            orders = OrderORM.find_by_customer_id(customer_id)
            for order in orders:
                print(order)
        elif choice == "5":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            CustomerORM.create(name, email)
            print("The customer was added successfully.🥳")
        elif choice == "6":
            id = int(input("Enter customer id: "))
            CustomerORM.delete(id)
            print("Deleted.😢")
        elif choice == "7":
            customers = CustomerORM.get_all()
            for customer in customers:
                print(customer)
        elif choice == "8":
            name = input("Enter customer name: ")
            customer = CustomerORM.find_by_name(name)
            if customer:
                print(customer)
        elif choice == "9":
            break
        else:
            print("Invalid choice.😢 Please try again.")


if __name__ == '__main__':
    main()