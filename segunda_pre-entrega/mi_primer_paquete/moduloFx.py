from mi_primer_paquete.moduloClass import Client
import json
from pkg_resources import resource_filename


# Import del archivo json con los datos existentes
filename = resource_filename('mi_primer_paquete', 'clients_db.json')
def importDb(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'clients': []}
    
data = importDb(filename)

clients_instances = []
for client_data in data['clients']:
    client_instance = Client.from_dict(client_data)
    clients_instances.append(client_instance)
    

# Funciones
def menu():
    try:
        option = int(input(f'MENU:\n - Please enter de number of the wanted option:\n 1 - Create a new user.- \n 2 - Show user information.-\n 3 - New Order\n 0 - Exit.-\n'));
        if option == 1:
            return createClient();
        if option == 2:
            return showClientInfo(clients_instances);
        if option == 3:
            return newOrder(clients_instances);
        if option == 0:
            return print(f'Thank you. Hope to see you again soon.');
        print(f'Please, enter a valid option number.');
        return menu();
    except Exception as e:
        return f'Something went wrong in menu function: {e}'

# Se crea un nuevo cliente, pidiendo los datos por input.
def createClient():
    try:
        email = input('Please, enter your email: ');
        fullName = input('Enter your full name: ')
        adress = input('Now enter your adress: ')
        newUser = Client(fullName, email, adress)
        newUser.addToDb()
        print(newUser)
        menu();
        return newUser;
    except Exception as e:
        return f'Something went wrong in createClient function: {e}'

# Muestra info del usuario requerido
def showClientInfo(clients_instances):
    try:
        client_email = input("Enter the email you're searching for:  ")
        for client in clients_instances:
            if client.email == client_email:
                print(client)
                menu()
                return True
        else:
            print(f'The client with the email {client_email} does not exist in our database.')
            menu()
            return False;
    except Exception as e:
        return f'Something went wrong in showClientInfo function: {e}'

#  Agrega ordenes de compra
def newOrder(clients_instances):
    print('You are aboout to make a new order')
    email = input('Enter your email: ')
    found_client = None
    for client in clients_instances:
        if client.email == email:
            found_client = client
            break
    if found_client:
        choice = int(input("Select the number of the product you want to buy:\n 1 - Notebook ASUS ZenBook i7 16gb ---> US$1200\n 2 - Xbox One 2TB ---> US$300\n 3 - Iphone 14 256GB ---> US$990.- \n    "))
        if choice == 1:
            found_client.addOrder({'product': 'Notebook ASUS ZenBook i7 16gb', 'price': 1200})
            print('Order added successfully!')
        elif choice == 2:
            found_client.addOrder({'product': 'Xbox One 2TB', 'price': 300})
            print('Order added successfully!')
        elif choice == 3:
            found_client.addOrder({'product': 'Iphone 14 256GB', 'price': 990})
            print('Order added successfully!')
        else:
            print('Incorrect choice number.')