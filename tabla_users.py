import pandas as pd
import json

def procesar_cosas(cosas)
    elementos_procesados = []
    for datos in data:
        nombre = str(datos['userId'])
        password = str(datos['password'])
        nombre = f'{nombre:.2f}'
        password = f'{password:.3f}'
        datos['nombre'] = nombre
        datos['password'] = password
        elementos_procesados.append(datos)

    return elementos_procesados
with open("secure-users.json", 'r') as file:
    data = json.load(file)

datos_procesados = procesar_cosas(data)
df =pd.DataFrame(datos_procesados)

nombre_archivo_excel = f"usuarios.xlsx"
df.to_excel(nombre_archivo_excel, index=False)