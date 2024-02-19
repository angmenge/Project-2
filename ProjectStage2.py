

def login():
    print('Please choose 1 for Manager, 2 for Customer >')
    login_option = input('1 or 2 >> ')

    if login_option == '1':
        manager_id = input('Please enter Manager ID >> ')
        manager_password = input('Please enter Manager password >> ')
        if manager_id == '1000' and manager_password == 'monkeyland123':
            print('Manager Login Successful!')
            return 'manager'
        else:
            print('Invalid ID or password. Try again')
            return None
    elif login_option == '2':
        customer_id = input('Please enter Customer ID >> ')
        customer_password = input('Please enter Customer password >> ')
        if customer_id == '2000' and customer_password == 'popo20':
            print('Customer Login Successful!')
            return 'customer'
        else:
            print('Invalid ID or password. Try again')
            return None
    else:
        print('Invalid option. Please try again.')
        return None

def manager_menu():
    while True:
        print('\nManager Menu:')
        print('1. Display Orders')
        print('2. Edit Prices')
        print('3. Reorder Inventory')
        print('4. Logout')
        print('5. Exit')
        choose = input('Choose 1, 2, 3, 4, or 5 >> ')
        if choose == '1':
            display_orders() #Need to write
        elif choose == '2':
            edit_prices()   #Need to write
        elif choose == '3':
            reorder_inventory() #Need to write
        elif choose == '4':
            print('Logged out as manager.')
            return
        elif choose == '5':
            print('Thank you! See you again!')
            exit()
        else:
            print('Invalid choice. Please try again.')

def customer_menu():
    while True:
        print('\nCustomer Menu:')
        print('1. Submit Order')
        print('2. Logout')
        print('3. Exit')
        choose = input('Choose 1, 2, or 3 >> ')
        if choose == '1':
            pass  
        elif choose == '2':
            print('Logged out as customer.')
            return
        elif choose == '3':
            print('Thank you! See you again!')
            exit()
        else:
            print('Invalid choice. Please try again.')

# Main
quit_program = False
while not quit_program:
    print('\n1. Login   2. Quit')
    choice = input('Choose 1 or 2 >> ')

    if choice == '1':
        user_type = login()
        if user_type == 'manager':
            manager_menu()
        elif user_type == 'customer':
            customer_menu()
        else:
            print('Login failed. Please try again.')
    elif choice == '2':
        quit_program = True
        print('Goodbye!')
    else:
        print('Invalid choice. Please try again.')