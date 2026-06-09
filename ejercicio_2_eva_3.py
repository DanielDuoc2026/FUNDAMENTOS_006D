capacidad_max = 30
historial = 0
capacidad = 30
opcion = 0
regi_vehiculo = 0
retiro_vehiculo = 0

print("¡Bienvenido al sistema de gestión de cupos del Estacionamiento Corporativo!")

while opcion != 5:

    print("=== MENÚ PRINCIPAL ===")
    print("1.	Cupos disponibles")
    print("2.	Registrar vehículo")
    print("3.	Retirar vehículo")
    print("4.	Historial de ocupaciones")
    print("5.	Salir")

    seguir =  True

    while seguir:
        try:
             opcion =  int(input("Ingrese opcion "))
             if opcion  > 0:
                seguir=False
             else:
                raise ValueError
        except ValueError:
            print("¡Opcion inválida! Ingresa un entero positivo para continuar.")
    
    match opcion:
        case 1:
              print(f"Los cupos disponibles son {capacidad}")
        case 2:
               seguir =  True

               while seguir:
                        try:
                            regi_vehiculo =  int(input("Ingrese cantidad de cupos a registrar "))
                            if regi_vehiculo  > 0:
                                seguir=False
                            else:
                                raise ValueError
                        except ValueError:
                            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
               if regi_vehiculo <=   capacidad:
                  capacidad =  capacidad - regi_vehiculo
                  historial =  historial + regi_vehiculo 
               else:
                  print("Error:  Se  sobrepaso la capacidad de estacionamiento")
        case 3:
               seguir =  True

               while seguir:
                        try:
                            retiro_vehiculo =  int(input("Ingrese cantidad de vehiculos a retirar "))
                            if retiro_vehiculo  > 0:
                                seguir=False
                            else:
                                raise ValueError
                        except ValueError:
                            print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
               if (retiro_vehiculo + capacidad) <=   capacidad_max:
                  capacidad =  capacidad + retiro_vehiculo
                  historial =  historial - retiro_vehiculo 
               else:
                  print("Error:  Se  sobrepaso la capacidad maxima  de estacionamiento")      
        case 4:
              print(f"La cantidad de vehículos registrados en el estacionamiento es {historial} ")  
        case 5:
              print("Gracias por utilizar nuestro software, hasta la próxima.")      
        case _:
              print ("Opcion Invalida")
                    