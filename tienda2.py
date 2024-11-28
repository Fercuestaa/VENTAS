
def vender(nombreprenda,valor):
    with open("ventas.txt","a") as archivo:
        archivo.write(nombreprenda+";"+valor+"\n")
        
def listado():
    with open("ventas.txt","r") as archivo:
        print("**listado de articulos**")
        print("************************")
        print(archivo.read())

def totales():
    with open("ventas.txt","r") as archivo:
        ventastotales=0
        for totales in archivo:
            valor=totales.split(";")
            ventastotales=ventastotales+int(valor[1])
        print(ventastotales)
    
op=0
while op!=1000:
    print("------TIENDA 2------")
    print("1. Camiseta $150.000")
    print("2. zapatos  $100.000")
    print("3. jogger   $250.000")
    print("4. medias   $190.000")
    print("5. buzo     $199.000")
    print("6. tennis   $110.000")
    print("--------------------")
    print("100. listado")
    print("101. totales")
    print("--------------------")
    print("1000. salir")
    op=int(input("Ingrese una opcion : "))
    if op==1:vender("camiseta","150000")
    elif op==2: vender("zapatos","100000")
    elif op==3: vender("jogger","250000")
    elif op==4: vender("medias","190000")
    elif op==5: vender("buzo","199000")
    elif op==6: vender("tennis","110000")
    elif op==100:listado()
    elif op==101:totales()