from datetime import datetime
import json
from pkg_resources import resource_filename

# Se carga la base de datos para trabajar.
filename = resource_filename('mi_primer_paquete', 'clients_db.json')

def importDb(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return { 'clients': [] }
database = importDb(filename)

# Creamos la clase.
class Client():
    def __init__(self, name, email, adress, orders = []):
        self.name = name
        self.email = email
        self.adress = adress
        self.orders = orders
        self.id = None
        self.lastSeen = None
    
    def __str__(self):
        return f'Client data:\n- ID: {self.id}\n- Nombre: {self.name}\n- Email: {self.email}\n- Dirección: {self.adress}\n- Ordenes de compra: {self.orders}\n- Ultima Vez Visto: {self.lastSeen}'
    
    def __getNextId(self):
        highestId = 0
        for client in database['clients']:
            clientId = client['id']
            if clientId > highestId:
                highestId = clientId
        nextId = highestId + 1
        return nextId;
        
    def __lastSeen(self):
        date = datetime.now()
        lastSeen = date.strftime('%A %d %b %Y, %I:%M%p')
        return lastSeen
        
    @classmethod
    def from_dict(cls, data):
        instance = cls.__new__(cls)  # Crear una nueva instancia sin llamar al constructor
        instance.__dict__.update(data)  # Actualizar el diccionario de la instancia con los datos del diccionario
        return instance
    
    def addToDb(self):
        try:
            for client in database['clients']:
                if client['email'] == self.email:
                    print('El usuario ya está en la DDBB. Se actualizaran sus datos de haber algún cambio con los de nuestro registro.')
                    self.id = client['id']
                    self.lastSeen = self.__lastSeen()
                    client.update(self.__dict__)

                    # Se guardan los nuevos datos en la DDBB
                    with open(filename, 'w') as file:
                        json.dump(database, file, indent=4)
                    return True
            else:
                self.id = self.__getNextId();
                self.lastSeen = self.__lastSeen()
                database['clients'].append(self.__dict__)

                # Se guardan los nuevos datos en la DDBB
                with open(filename, 'w') as file:
                    json.dump(database, file, indent=4)
                return True
        except Exception as e:
            return f'Algo salió mal en addToDb: {e}'

    def addOrder(self, order):
        try:
            for client in database['clients']:
                if client['email'] == self.email:
                    print(f'Order added: {order["product"]} - Price: US${order["price"]}')
                    self.orders.append(order)
                    client.update(self.__dict__)
                    
                    # Se guardan los nuevos datos en la DDBB
                    with open(filename, 'w') as file:
                        json.dump(database, file, indent=4)
                    return True

        except Exception as e:
            print(f'Error occurred while adding order: {e}')