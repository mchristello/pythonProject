import json

filename = 'user-data.json'

# Import del archivo json con los datos existentes
def cargarDatabase(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'users': []}
    
database = cargarDatabase(filename)

# Creación de Clase
class User:
    def __init__(self, fullName, email, password):
        self.fullName = fullName
        self.email = email
        self.password = password
    
    def showUserInfo(self):
        try:
            usuario = input("Enter the username you're searching for: \n")
            for user in database['users']:
                if user['username'] == usuario:
                    return f"The user you're lookin for is {self.usuario} \nThe password is: {self.user['password']}"
            else:
                return f'The user {usuario} does not exist in our database.'
        except Exception as e:
            return f'Something went wrong: {e}'

# Declaración de funciones
# Menu de opciones
def menu():
    try:
        option = int(input(f'Please enter de number of the wanted option:\n 1 - Create a new user.- \n 2 - Show user information.-\n 3 - Login.-\n 0 - Exit.-\n'));
        if option == 1:
            return createUser();
        if option == 2:
            return showUserInfo();
        if option == 3:
            return login()
        if option == 0:
            return print(f'Thank you. Hope to see you again soon.');
        print(f'Please, enter a valid option number.');
        return menu();
    except Exception as e:
        return f'Something went wrong in menu function: {e}'

# Creación de usuarios
def createUser():
    try:
        email = input('Please, enter your email: ');
        for user in database['users']:
            if user['email'] == email:
                print(f'Already exist a user with the email you entered.');
                menu();
                return False
        fullName = input('Please, enter your full name: ')
        password = input('Please, enter your password: ')
        checkPassword = input('Re enter your password to check...')
        if password != checkPassword:
            print(f'Passwor check failed, please try again.');
            menu();
            return False
        else:
            newUser = User(fullName, email, password)
            print(f'New user created: \n Name: {newUser.fullName}\n Email: {newUser.email}')
            database['users'].append(newUser.__dict__)
            return newUser;
    except Exception as e:
        return f'Something went wrong in createUser function: {e}'

# Muestra info del usuario requerido
def showUserInfo():
    try:
        usuario = input("Enter the email you're searching for:  \n")
        for user in database['users']:
            if user['email'] == usuario:
                print(f' - Full Name: {user["fullName"]}\n - Email: {user["email"]}');
                return True
        else:
            print(f'The user with the email {usuario} does not exist in our database.');
            menu();
            return False;
    except Exception as e:
        return f'Something went wrong in showUserInfo function: {e}'

# Login de usuario
def login():
    try:
        email = input("Enter your email address:    ")
        for user in database['users']:
            if user['email'] == email:
                password = input("Enter your password:    ")
                if user['password'] == password:
                    print(f'Login successful, welcome {email} to your account!')
                    return True
                else:
                    print(f'Sorry, invalid credentials for login. Please try again.');
                    menu();
                    return False
        print(f'The user {email} does not exist.')
        menu()
        return False
    except Exception as e:
        return f'Something went wrong in login function: {e}'

# Llamado de funciones
menu()

# Se guardan los datos actualizados en un json
with open(filename, 'w') as file:
    json.dump(database, file, indent=4)