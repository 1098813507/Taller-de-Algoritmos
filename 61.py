print("numeros naturales contenidos en n y m")
  n=int(input("digita un numero"))
  m=int(input("digita un numero"))

  if m>n:
  	print("continuar el reprograma")

  else:
  	print("parar el programa")

  	for num in range(n,m+1):
  		print(num)