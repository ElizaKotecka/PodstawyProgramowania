import queue

def customer_service():
    line = queue.Queue()
    ticket_number = 1

    while True:
        print("\nCustomer Service")
        print("1. Add a new customer")
        print("2. Serve the next customer")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            line.put(ticket_number)
            print(f"\nCustomer with ticket #{ticket_number} added to the queue.")
            ticket_number += 1

        elif choice == "2":
            if line.qsize() > 1:
                next_customer = line.get()
                print(f"\nServing customer with ticket #{next_customer}.")
            else:
                print("\nNo customers in the queue to serve.")

        elif choice == "3":
            print("\nExiting the system. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__=='__main__':
    customer_service()
