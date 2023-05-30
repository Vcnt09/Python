usuario = input("Ingrese su nombre de ususario:")
contraseña = input("Ingrese su contraseña:")

if usuario == "pedro" and contraseña == "1234":
    print("User_1",usuario)
    print("Pass_1",contraseña)
elif usuario == "angel" and contraseña == "a4s1":
    print("User_2:",usuario)
    print("Pass_2:",contraseña)
else:
    print("Son incorrecos los datos ingresados.")
##
##convertidor de dolares
cantidad = 0
conversionchile = 0.0
preciodolarchile = 540.31
precioyen = 6.05
precioargentino = 3.79


cantidad = int(input("Ingrese la cantidad de a cambiar:"))
monedacambiar = input("Ingrese que moneda desea cambiar(JPY-AUD-Peso Argentino):")

if monedacambiar == "JPY":
    conversionchile = precioyen * cantidad
    print("$",cantidad,"Yenes equivalen a $",conversionchile ,"pesos chilenos")
elif monedacambiar == "AUD":
    conversionchile = preciodolarchile * cantidad
    print("$",cantidad,"dolares Australianos equivalen a $",conversionchile ,"pesos chilenos")
elif monedacambiar == "Peso Argentino":
    conversionchile = precioargentino * cantidad
    print("$",cantidad,"Pesos Argentinos equivalen a $",conversionchile ,"pesos chilenos")
else:
    print("Debe ingresar alguna opción valida.......")
##
##Numero mayor
numero1 = int(input("Ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))

if numero1 > numero2:
    print("El numero",numero1," es mayor")
else:
    print("El numero",numero2," es mayor")

##
##Suma de dos numeros :)
num1 = int(input("Numero uno:"))
num2 = int(input("Numero dos:"))

sumanum = 0

sumanum = num1+num2

print("La suma de los dos numeros ingresados es:",sumanum)

##
##Ejercicio notas echo por el profesor.
nota1= float(input("Hola ingrese la nota 1:"))
nota2= float(input("Hola ingrese la nota 2:"))
nota3= float(input("Hola ingrese la nota 3:"))

if 1 <= nota1 <=7 and 1<= nota2 <=7 and 1<= nota3 <=7:
		promedio=(nota1+nota2+nota3)/3
		if promedio >=4.0:
			print("Aprobado")
		else:
				print("Reprobado")
else:
		print("Notas Invalidas")

##
salario = int(input("Ingrese salario Bruto:"))

descuento = 0
liquido = 0

if salario <= 300000:
    descuento = round(salario * 0.1)
    liquido = salario - descuento
    print("Su sueldo Liquido es de:",liquido)
elif salario <= 400000:
    descuento = round(salario * 0.15)
    liquido = salario - descuento
    print("Su sueldo Liquido es de:",liquido)
else:  
    descuento = round(salario * 0.20)
    liquido = salario - descuento
    print("Su sueldo Liquido es de:",liquido)
##
numero = int(input("Ingrese numero :"))

if (numero % 2 == 0) and (numero % 3 == 0):
    print("El numero ingresado es divisible por 2 y 3.")
elif (numero % 2 == 0):
    print("El numero ingresado es solo divisible por 2.")
else :
    numero % 3 == 0
    print("El numero es divisible solo por 3.")
##
numero = int(input("Ingrese numero :"))

if numero >= 1:
    print("El numero es psositivo. :D")
elif numero <= -1:
    print("El numero es negativo.")
else:
    print("El nuemro es cero.")
##
#Par impar
nume = int(input("Ingrese un numero mayor a 1 y menor a 101:"))

if nume < 1 and nume >101:
		print("el numero ingresado esta fuera de rango ")
elif nume % 2 == 0:
        print("El numero ingresado es par")
else:
    print("El numero es impar")
        
##
numero1 = int(input("Ingrese numero :"))
numero2 = int(input("Ingrese numero 2:"))

suma = 0

if numero1 > numero2:
    print("El numero ",numero1," es mayor")
elif numero2 > numero1 :
    print("El numero", numero2, "es mayor")
else:
    print("Los numero son iguales")
    
suma = numero1 + numero2
print("La suma de ambos numeros es de",suma)
##
##Caso con flag
numero1 = int(input("Ingrese numero :"))
numero2 = int(input("Ingrese numero 2:"))
numero3 = int(input("Ingrese numero 3:"))
suma = 0 
contador = 0
flag= False


if numero1 > 0 and numero1 % 2 == 0:
    suma = suma + numero1
    flag = True
else:
    contador = contador + 1
if numero2 > 0 and numero2 % 2 == 0:
    suma = suma + numero2
    flag = True
else:
    contador = contador + 1
if numero3 > 0 and numero3 % 2 == 0:
    suma = suma + numero3
    flag = True
else:
    contador = contador + 1
    
if flag:
    print("La suma de los numeros pares es:", suma)
    print("Cantidad de numeros pares es:",contador)
else:
    print("El numero no es impar ni par , que raro")

##

contador = 0
num1 =int(input("Ingrese el numero 1:"))
num2 =int(input("Ingrese el numero 2:"))
num3 =int(input("Ingrese el numero 3:"))


if num1 < 0:
    contador = contador + 1
if num2 < 0:
    contador = contador + 1
if num3 < 0:
    contador = contador + 1
    
if contador == 0:
    print("No se encontraron numeros menores a 0")
else:
    print("Se encontraron ",contador," Numeros distintos de 0")
##
a = int(input("Ingrese el lado 1:"))
b = int(input("Ingrese el lado 2:"))
c = int(input("Ingrese el lado 3:"))

if a == b == c:
    print("El triangulo es equilatero")
elif a==b or a==c or b==c:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")
##
precio_churrasco = 1500
completo = 1000
vegetariano = 2000
barrosluco = 3000

cantidad_churrascos = int(input("Que cantidad de chucarrascos desea comprar:"))
cantidad_completos = int(input("Que cantidad de completos desea comprar:"))
cantidad_vegetariano = int(input("Que cantidad de vegetariano desea comprar:"))
cantidad_luco = int(input("Que cantidad de barros luco desea comprar:"))

subtotal = (precio_churrasco * cantidad_churrascos) + (completo * cantidad_completos) + (vegetariano * cantidad_vegetariano) + (barrosluco * cantidad_luco)


descuento = 0 

tiene_descuento = input("¿Posee descuento?(si/no): ")

if tiene_descuento.lower() == "si":
    descuento = subtotal * 0.1
    
    
total = subtotal - descuento
print("El total a pagar es:$ ",total)
##
mascarilla = 500
cant_masc =int(input("Ingrese la cantidad de mascarillas:"))
comuna = input("Pertenece a la misma comuna o es aledaña?(misma comuna o aledaña): ")
envio = 0


total = mascarilla * cant_masc

if total > 15000:
    envio = 0
elif comuna.lower() == "misma comuna":
    envio = 1000
elif comuna.lower() == "aledaña":
    envio = 2000
else:
    envio = 3000

total_pagar = total + envio

print("El total a pagar es de", total_pagar )
##
v_agua = 600
v_azúcar = 1200
v_aceite = 1500
v_arroz = 1250
v_fideos = 790
v_bebida = 1780
v_chocolate = 2500
v_pan_molde = 1340

ca_agua = int(input("Ingrese la cantidad de agua que desea:"))
ca_azucar = int(input("Ingrese la cantidad de azucar que desea:"))
ca_aceite = int(input("Ingrese la cantidad de aceite que desea:"))
ca_arroz = int(input("Ingrese la cantidad de arroz que desea:"))
ca_fideos = int(input("Ingrese la cantidad de fideos que desea:"))
ca_bebida = int(input("Ingrese la cantidad de bebidas que desea:"))
ca_chocolate = int(input("Ingrese la cantidad de chocolates que desea:"))
ca_pan_molde = int(input("Ingrese la cantidad de pan de molde que desea:"))

subtotal = (v_agua * ca_agua) + (v_azúcar * ca_azucar) + (v_aceite * ca_aceite) + (v_arroz * ca_arroz) + (v_fideos * ca_fideos) + (v_bebida * ca_bebida) + (v_chocolate * ca_chocolate) + (v_pan_molde * ca_pan_molde)
total = 0

preferencial = input("Usted es cliente preferencial?(Si / No) :")

if preferencial.lower() == "si":
    subtotal = round(subtotal * 0.25)
else:
    subtotal = subtotal
    
efectivo = int(input("Ingrese dinero en efectivo para cancelar:"))

if efectivo >= subtotal:
    total = round(efectivo - subtotal)
    print("El total de la compra es de:$",subtotal)
    print("Su vuelto es de:$",total)
else:
    print("No tiene suficiente dinero para completar la compra......")

##
estreno = 4800
normal = 2900
pa_peque = 2500
pa_medi = 4500
pa_gran = 7800
bebi_pe = 1000
bebi_medi = 1250
bebi_gra = 2000


print("------Bienvenido a CineDuoc--------")
pduoc = input("Usted pertenece a Duoc Uc (Si / No) :")
    
can_estreno = int(input("¿Cuantas entradas de estreno desea comprar? :"))
can_normal = int(input("¿Cuantas entradas normales desea comprar? :"))
totalentradas = (estreno * can_estreno) + (normal * can_normal)

if pduoc.lower() == "si":
    totalentradas = (totalentradas * 0.30)
else:
    totalentradas = totalentradas    

eleccion = input("¿Desea comprar palomitas?(Si / No):")

if eleccion.lower() == "si":
    can_pape = int(input("Cuantas palomitas pequeñas desea comprar:"))
    can_pame = int(input("Cuantas palomitas medianas desea comprar:"))
    can_pagr = int(input("Cuantas palomitas grandes desea comprar:"))
    valorpalomitas = (pa_peque * can_pape) + (pa_medi * can_pame) + (pa_gran * can_pagr)
else:
    valorpalomitas = 0
    print("Gracias.Que disfrute su pelicula.")
    

bebi = input("Desea agregar bebidas? (Si/No):")
if bebi.lower() == "si":
    can_bepe = int(input("Ingrese la cantidad de bebidas pequeñas que desea:"))
    can_beme = int(input("Ingrese la cantidad de bebidas medianas que desea:"))
    can_begr = int(input("Ingrese la cantidad de bebidas grandes que desea:"))
    valorbebi = (bebi_pe * can_bepe) + (bebi_medi * can_beme) + (bebi_gra * can_begr)
else:
    valorbebi = 0
    print("Gracias.Que disfrute su pelicula.")


totalcompra = totalentradas + valorpalomitas + valorbebi

efectivo = int(input("Ingrese efecivo para cancelar la compra:"))
if efectivo >= totalcompra:
    total = efectivo - totalcompra
    print("El valor total de la compra es de:$", totalcompra)
    print("Su vuelto es de:$",total)
else:
    print("No tiene suficiente dinero para realizar la compra.....")

##
pertenece_duoc= False
placa = input("¿Posee placa de identificacion?(si o no)").lower()
if placa== "si":
    pertenece_duoc = True
entrada = input("Ingrese tipo de entrada que desea (normal/estreno):").lower()
cantidad_entrada = int(input("Ingrese la cantidad de entradas:"))

precio_entrada = 4800 if entrada == "estreno" else 2900
total_entrada = precio_entrada * cantidad_entrada
descuento = 0

if pertenece_duoc:
    descuento = total_entrada * 0.3
    total_entrada -= descuento

quiere_palomitas = input("¿Desea palomitas? (si/no)").lower()
if quiere_palomitas == "si":
    print("Promocion palomitas")
    print("1.Palomitas pequeñas = $2500")
    print("2.Palomitas mediana = $4500")
    print("3.Palomitas Grande = $7800")
    tipo_palomita = int(input("Ingrese el tipo de palomita que quiere(1, 2 o 3)"))
    cantidad_palomitas = int(input("Ingrese la cantdad de palomitas:"))

    precio_palomita = 0
    if tipo_palomita == 1:
        precio_palomita = 2500
    elif tipo_palomita == 2:
        precio_palomita =4500
    elif tipo_palomita== 3:
        precio_palomita = 7800
    
    total_palomitas = precio_palomita * cantidad_palomitas
    
        

quiere_bebida= input("¿Desea bebida? (si/no)").lower()
if quiere_bebida == "si":
    print("Promocion Bebidas")
    print("1.Palomitas pequeñas = $1000")
    print("2.Palomitas mediana = $1250")
    print("3.Palomitas Grande = $2000")
    tipo_bebida = int(input("Ingrese el tipo de bebida que quiere(1, 2 o 3)"))
    cantidad_bebida = int(input("Ingrese la cantidad de bebidas:"))

    precio_bebida = 0
    if tipo_bebida == 1:
        precio_bebida = 1000
    elif tipo_bebida == 2:
        precio_bebida =1250
    elif tipo_bebida== 3:
        precio_bebida = 2000
    
    total_bebida = precio_bebida * cantidad_bebida
    
    
total_pagar = total_entrada 
if quiere_palomitas == "si":
    total_pagar += total_palomitas
if quiere_bebida == "si":
    total_pagar+=total_bebida

print("Total a pagar es : ",total_pagar)

efectivo = int(input("Ingrese efectivo con el que va a pagar: "))
vuelto = efectivo - total_pagar

print("Su vuelto es: ",vuelto)

##

a = 0
suma=0
while a < 5:
    num = int(input("Ingrese un numero:"))
    a = a + 1
    suma=suma+num
    
print(suma)


##
i=0
suma=0

while i < 5:
    numero = int(input("Ingrese una numero positivo:"))
    if numero > 0:
        suma = suma + numero
        i= i + 1
    else:
        print("El numero es negativo, ingrese un numero positivo.....")

print(suma)
##

i=0
mayorcero=0
sumapar= 0

while i < 5:
    numero=int(input("Ingrese un numero positivo:"))
    if numero > 0:
        mayorcero = mayorcero+1
    if numero % 2 == 0:
        sumapar = sumapar + numero
    i = i + 1
    
print("La cantidad de numeros mayores a cero es:", mayorcero)
print("La suma de los pares es:", sumapar)

##
print("Bienvenido al centro pokemon")
dueno_pokemon = input("Ingrese el dueño del pokemon (ash/oak):").lower()
while dueno_pokemon!="ash" and dueno_pokemon != "oak":
    dueno_pokemon = input("Opción no valida. Ingrese nuevamente:").lower()
    
tipo_pokemon = input("Ingrese el tipo de pokemon que desea consultar (Agua,Fuego,Planta): ").lower()
while tipo_pokemon != "agua" and tipo_pokemon != "fuego" and tipo_pokemon != "planta":
    tipo_pokemon=input("Tipo de pokemon invalido. Ingrese nuevamente").lower()
    
if tipo_pokemon == "agua":
    if dueno_pokemon == "oak":
        cantidad_pokemon = 3
    else:
        cantidad_pokemon = 2
elif tipo_pokemon =="fuego":
    if dueno_pokemon == "oak":
        cantidad_pokemon = 1
    else:
        cantidad_pokemon = 6
elif tipo_pokemon =="planta":
    if dueno_pokemon == "oak":
        cantidad_pokemon = 2
    else:
        cantidad_pokemon = 3

print("--------- Resumen de consulta ------------")
print("Dueño pokemon:",dueno_pokemon)
print("Tipo pokemon:",tipo_pokemon)
print("Cantidad de pokemon:",cantidad_pokemon)

##
print(" Valorant Armas y pro players ")

proplayer = input("Ingrese el propalyer (keznit/mazino):").lower()
while proplayer!="keznit" and proplayer != "mazino":
    proplayer = input("Opción no valida. Ingrese nuevamente:").lower()
    
tipo_arma = input("Ingrese el arma que desea consultar (vandal,phantom,ghost,operator): ").lower()
while tipo_arma != "vandal" and tipo_arma != "phantom" and tipo_arma != "ghost" and tipo_arma != "operator":
    tipo_arma=input("Tipo de arma invalido. Ingrese nuevamente").lower()
    
if tipo_arma == "vandal":
    if proplayer == "keznit":
        valoracion = "Buena"
    else:
        valoracion = "Buena"
elif tipo_arma =="phantom":
    if proplayer == "keznit":
        valoracion = "buena"
    else:
        valoracion = "mala"
elif tipo_arma =="ghost":
    if proplayer == "keznit":
        valoracion = "regular"
    else:
        valoracion = "buena"
elif tipo_arma == "operator":
    if proplayer == "keznit":
        valoracion ="mala"
    else:
        valoracion = "mala"
        
print("Tipo de arma:",tipo_arma)
print("Pro Player:",proplayer)
print("Opinion de la arma:",valoracion)

print("GG WP")

##
sw = 1
while sw == 1:
    print("1.Opcion 1.Pedir el nombre")
    print("2.Opcion 2. Pedir edad")
    print("3.Salir")
    op=int(input("Ingrese una opción"))
    try:
        if op > 0 and op < 4:
            if op == 1:
                print("Usted selecciono la opcion 1")
                name = input("Ingrese su nombre: ")
                continuar = int(input("Desea salir 1=si 2=no"))
                if continuar == 1:
                    print("Adios")
                    sw = 0
            if op == 2:
                print("Usted selecciono la opcion 2")
                age = int(input("Ingrese su edad"))
                continuar = int(input("Desea salir 1=si 2=no"))
                if continuar == 1:
                    print("Adios")
                    sw = 0
            if op == 3:
                print("Gracias por jugar conmigo")
                sw = 0            
            
            
    except:
        print("Ocurrio un error")


##
sw = 1
while sw == 1:
    print("1. par y impar")
    print("2.Numero mayor")
    print("Salir")
    try:
        op=int(input("Ingrese la opcion que desea"))
        if op == 1:
            print("Seleccionaste la opcion 1.")
            num = int(input("Ingresa un numero: "))
            if num % 2 == 0:
                print(num," es par")
            else:
                print(num," es impar")
        if op == 2:
            print("Seleccionaste la opcion 2")
            num2 = int(input("Ingrese un numero grande:"))
            maximo = num2
            i = 1
            while i < 5:
                num2 = int(input("Ingrese otro numero:"))
                if num2 > maximo:
                    maximo = num2
                i=i+1
            print("El numero maximo es", maximo)
        if op == 3:
            print("Seleccionaste la opcion 3")
            sw = 0
    except ValueError:
        print("Error.... el valor no corresponde......")


##
sw = 1
total=0
print("Bienvenido a la panaderia")
while sw == 1:
    print("Ingrese el pan que desea comprar.")
    print("1.Pan Amasado.")
    print("2.Pan de Molde")
    print("3.Pan Baguette")
    print("4.Pan Integral")
    print("5.Salir.")
    op = int(input("Ingrese una opción:"))
    try:
        if op > 0 and op < 6:
            if op == 1:
                cant = int(input("Ingrese la cantidad de pan amasado que desea:"))
                total += 1500 *cant
                print("Ha comprado",cant,"panes amasado.")
            if op == 2:
                cant = int(input("Ingrese la cantidad de pan de molde que desea:"))
                total += 1000 *cant
                print("Ha comprado",cant,"panes de molde.")
            if op == 3:
                cant = int(input("Ingrese la cantidad de pan amasado que desea:"))
                total += 2000 *cant
                print("Ha comprado",cant,"panes baguette.")
            if op == 4:
                cant = int(input("Ingrese la cantidad de panes integrales que desea:"))
                total += 3000 *cant
                print("Ha comprado",cant,"panes amasado.")
            if op == 5:
                sw = 0
            if op < 1 or op > 5:
                print("Opcion invalida")
    except:
        print("Ocurrio un error.....")            
if total > 5000:
    print("Total a pagar",round(total),".El envio es gratis.")
else:
    total = total * 1.1
    print("Total a pagar",round(total),".Se agrega el 10%")