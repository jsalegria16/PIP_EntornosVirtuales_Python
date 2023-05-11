import requests 

def GetCategories ():
    request = requests.get('https://api.escuelajs.co/api/v1/categories')
    print('status:', request.status_code) # Status
    print('response:',request.text) # Lo que regresa la API
    print('Type of response:',type(request.text)) # Necesitamos pasarlo a lista
    
    Respuesta =  request.json() # Pasar a una lista
    
    print('Nombre de todas las categorías obtenidas: ')
    
    for categoria in Respuesta:
        print('Nombre CAtegoria:',categoria['name'])

