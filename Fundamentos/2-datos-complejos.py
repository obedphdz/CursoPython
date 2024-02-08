# Variables: Sirven para almacenar los datos
# Definiendo Variables
a = 5
b = 10

# Concatenar con +
nombre = "Obed"
bienvenida = "Hola " + nombre + " ¿Cómo estas?"
print(bienvenida)

# Concatenar con fstrings, que es para convertir las variables a texto
nombre = "Obed"
bienvenida_al_usuario = f"Hola {nombre} ¿Cómo estas?"
print(bienvenida_al_usuario)

# tambien se cuenta con del para borrar variables
del nombre
print(nombre)  # Esto daria error ya que se elimino la variable nombre

# Operadores de Pertenencia (in / not in)
print(
    "estas" in bienvenida_al_usuario
)  # Esto devolveria un True ya que la palabra si se encuentra en la variable
print("estas" not in bienvenida_al_usuario)  # Esto devolveria un False
