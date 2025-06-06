def print_receipt():
    name = input("Enter Customer Name: ")
    address = input("Enter Customer Address: ")
    phone_number = input("Enter Customer Phone Number: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (DD/MM/YYYY): ")

    print("\n\n")
    print("------------------------ RECEIPT ------------------------")
    print("Name:", name)
    print("Address:", address)
    print("Phone Number:", phone_number)
    print("Amount:", amount)
    print("Date:", date)
    print("---------------------------------------------------------")

print_receipt()