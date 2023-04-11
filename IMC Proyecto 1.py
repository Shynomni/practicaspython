nombre = input("Por favor ingresa tu nombre")
apellido_paterno = input("Por favor ingresa tu apellido paterno: ")
apellido_materno = input("Por favor ingresa tu apellido materno: ")
while True:
    edad = input("Por favor ingresa tu edad: ")
    if edad.isdigit():
        edad = int(edad)
        break
    else:
        print("La edad debe ser un número entero.")
while True:
    peso = input("Por favor ingresa tu peso en kilogramos: ")
    if peso.isnumeric() or (len(peso.split(".")) == 2 and peso.split(".")[0].isnumeric() and peso.split(".")[1].isnumeric()):
        peso = float(peso)
        break
    else:
        print("El peso debe ser un número válido.")
while True:
    estatura = input("Por favor ingresa tu estatura en metros: ")
    if estatura.isnumeric() or (len(estatura.split(".")) == 2 and estatura.split(".")[0].isnumeric() and estatura.split(".")[1].isnumeric()):
        estatura = float(estatura)
        break
    else:
        print("La estatura debe ser un número válido.")
imc = peso / (estatura ** 2)
print("Nombre completo: " + nombre + " " + apellido_paterno + " " + apellido_materno)
print("Edad: " + str(edad) + " años")
print("Peso: " + str(peso) + " kg")
print("Estatura: " + str(estatura) + " m")
print("IMC: " + str(imc))
input ()
