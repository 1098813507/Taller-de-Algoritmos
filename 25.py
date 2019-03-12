print("invertir un numero de 4 cifras")

a=int(input("digita un numero de 4 cifras"))
b=int(a%1000)
c=a-(b*1000)
d=int(c%100)
e=c-(d*100)
f=int(e%10)
g=e-(f*10)

print(str(g)+str(f)+str(d)+str(b))
print("end")