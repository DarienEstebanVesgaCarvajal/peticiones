# Enviar datos a un servidor  
headers = {'Content-Type': 'application/json'}  
data = {'name': 'Miguel Angel Castro Escamilla', 'username': "Marcos"}  
response = requests.post('https://jsonplaceholder.typicode.com/users', headers=headers, json=data)  
# print(response.status_code)  
print(response.json())  

# Obtener todos los usuarios  
response = requests.get('https://jsonplaceholder.typicode.com/users')  
data = response.json()  
print(len(data))  
for i in range(1, len(data)):  
    print(f""" Id: {data[i].get("id")}, url {data[i].get("name")} """)

# Actualizar datos de un usuario en el servidor
updateData = {'name': 'Miguel Angel Updated', 'username': 'MarcosUpdated'}
response = requests.put('https://jsonplaceholder.typicode.com/users/1', headers=headers, json=updateData)
print("Status Code:", response.status_code)
print("Response:", response.json())

# Eliminar un usuario en el servidor
response = requests.delete('https://jsonplaceholder.typicode.com/users/1')
print("Status Code:", response.status_code)
