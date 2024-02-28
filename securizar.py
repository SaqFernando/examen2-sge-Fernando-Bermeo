import os.path
import json
import hashlib

def escribir_archivo():
    fichero_primero = open('users.json')
    data = json.load(fichero_primero)

    for contraseña in data:
        contra = contraseña['password']
        hash=hashlib.sha256(contra.encode('UTF-8')).digest()
        with open('secure-users.json', 'w')as final:
            final.write('[\n')
            for datos in data:
                final.write('{\n\t"userId": ' + '" ' + datos['userId'] + ' ",'+'\n')
                final.write('\t"password": ' + '" ' + hash.hex()+ ' "\n},' "\n")
            final.write(']')

escribir_archivo()