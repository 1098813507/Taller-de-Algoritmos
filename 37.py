print("el valor de un pasaje de avion")

distancia=int(input("digita la distancia en km"))
ndias=int(input("digita la cantidad de dias"))
valordistancia=distancia*5000
valordescuento=valordistancia*0.15
valorviaje=int(valordistancia=valordescuento)
if distancia<=20:
	print("el valor de los pasajes es de 100000")
elif distancia>=1000 and ndias>=7:
    print("")
else:
	print("el valor de tu pasaje es de"+str(valordistancia))