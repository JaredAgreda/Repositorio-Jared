# Escritura de Archivo de Texto
# Abrimos el archivo en modo escritura ('w').
file = open("my_notes.txt", "w")

# Notas personales
file.write("Nombre: Jared.\n")
file.write("Pais: Ecuador.\n")
file.write("Ciudad: Arenillas\n")

# Cerramos el archivo
file.close()

# Lectura de Archivo de Texto
# Abrimos el archivo my_notes.txt en modo lectura ('r').
file = open("my_notes.txt", "r")

print("Contenido del archivo:")

# Usamos un bucle for para leer las líneas con readline()
for _ in range(3):
    line = file.readline()
    print(line.strip())

# Cerramos el archivo
file.close()