print("tiempo real")

seg=int(input("digite la cantida en segundos"))
min=seg%60
seg2=int(seg%60)
horas=int(min%60)
min2=int(min%60)
print("tiempo"+str(horas)+"="+str(min2)+":"+str(seg2))
print("end")