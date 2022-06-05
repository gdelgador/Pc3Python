# Importamos libreria


# constantes
MIMES = {
    'gif':'image/gif',
    'jpg':'image/jpeg',
    'jpeg':'image/jpeg',
    'png':'image/png',
    'pdf':'application/pdf',
    'txt':'text/plain',
    'zip':'application/zip'
    }

# funciones

def get_mime(file_name:str, mimes=MIMES):
    """Imprime el valor del mime correspondiente según nombre de archivo"""
    
    # separamos archivo de extension
    _, ext = file_name.split('.')
    
    # Obtendo valor MIME correspondiente de diccionario
    if ext.lower() in mimes.keys():
        x = mimes.get(ext)
        print(x)
    else:
        print('application/octet-stream')

#principal
if __name__ == '__main__':
    # obtenemos dato
    response = input('ext name: ')
    response = response.lower().strip()

    get_mime(response)

