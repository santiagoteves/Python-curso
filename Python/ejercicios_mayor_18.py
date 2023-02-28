
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""""
edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")
"""""



#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.


"""""
resultado = 0
numero_1 = int(input("Ingrese dos numeros: "))
numero_2 = int(input("Ingrese dos numeros: "))
if numero_2 == 0:
    print("Error")
else:
    print(f"{numero_1} % {numero_2}   = {resultado}")
    resultado = numero_1 / numero_2

"""""

 



