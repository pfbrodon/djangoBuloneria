import json

# Nombre del archivo JSON
json_file_path = 'intarplano.json'

# Leer datos desde el archivo JSON
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)


# Grabar resultados en un archivo de texto
txt_file_path = 'resultado.txt'
with open(txt_file_path, 'w') as txt_file:
    for item in data:
        for key, value in item.items():
            txt_file.write(f'INSERT INTO stock_producto (codigo,categoria,descripcion,cantidad,precioCosto,precioPublico,marca,utilidad) VALUES (categoria,codigo,{item['descripcion']},{item['cantidad']},{item['precioCosto']}),utilidad;'+'\n')
