import requests
from tkinter import *

# Crea la ventana
ventana = Tk()
ventana.geometry("350x550")

# Crea el campo de texto para la ciudad
texto_ciudad = Entry(ventana, font=('Courier', 20, 'normal'), justify='center')
texto_ciudad.pack(padx=30, pady=30)

# Crea la etiqueta para mostrar la ciudad
ciudad = Label(font=('Courier', 20, 'normal'))
ciudad.pack(padx=25, pady=25)

# Crea la etiqueta para mostrar la temperatura
temperatura = Label(font=('Courier', 40, 'normal'))
temperatura.pack(padx=15, pady=15)

# Crea la etiqueta para mostrar la descripción del clima
descripcion = Label(font=('Courier', 20, 'normal'))
descripcion.pack(padx=15, pady=15)

# Crea una etiqueta con el nombre del autor
mostrar_clima = Label(text='By Bruno Tornese', font=('Courier', 20, 'normal'))
mostrar_clima.pack(padx=30, pady=30)


def mostrar_respuesta():
    # Actualiza la etiqueta de la ciudad 
    ciudad['text'] = texto_ciudad.get()
    # Obtiene los datos del clima de la ciudad
    clima = obtener_clima(texto_ciudad.get())
    # Actualiza las etiquetas de temperatura y descripción con los datos del clima 
    temperatura['text'] = clima['main']['temp']
    descripcion['text'] = clima['weather'][0]['description']


def obtener_clima(ciudad):
    # Define la URL de la API y los parámetros
    API_KEY = "c6d6587cc5608f36f0f61d9bf51b8d36"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    parametros = {'APPID': API_KEY, 'q': ciudad, 'units': 'metric'}
    #Hace la solicitud a la API
    response = requests.get(url, params=parametros)
    # Convierte la respuesta a JSON
    clima = response.json()
    #Retorna los dados 
    return clima

#Crea el botón para obtener el clima 
obtener_clima_btn = Button(ventana, text='Obtener clima', font=('Courier', 20, 'normal'), command=mostrar_respuesta)
obtener_clima_btn.pack()

# Inicia el codigo
ventana.mainloop()



    






