while True:
    print("¿Qué programa deseas ejecutar?")
    print("1. Longitud de una palabra")
    print("2. Encontrar el cuadrante")
    opcion = input("Ingrese la opción deseada (1 o 2): ")

    if opcion == "1":
        palabra = input("Ingresa una palabra: ")
        longitud = len(palabra)

        if longitud >= 4 and longitud <= 8:
            print("La palabra es correcta.")
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")
    elif opcion == "2":
        x = float(input("Ingrese X: "))
        y = float(input("Ingrese Y: "))

        if x == 0 or y == 0:
            print("Las coordenadas no pueden ser cero.")
        elif x > 0 and y > 0:
            print("El punto se encuentra en el cuadrante I.")
        elif x < 0 and y > 0:
            print("El punto se encuentra en el cuadrante II.")
        elif x < 0 and y < 0:
            print("El punto se encuentra en el cuadrante III.")
        else:
            print("El punto se encuentra en el cuadrante IV.")
    else:
        print("Opción inválida.")

    continuar = input("¿Desea ejecutar otro programa? (S/N): ")
    if continuar.upper() != "S":
        break
