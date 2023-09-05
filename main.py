from modulo.clientes import Cliente

def main():
    cliente1 = Cliente("Juan Pérez", "juan@test.com", "123 High Street, London", 500)
    cliente2 = Cliente("María Gómez", "maria@test.com", "456 Oxford Road, Manchester", 1000)
    cliente3 = Cliente("Carlos Rodríguez", "carlos@test.com", "789 Queen's Lane, Edinburgh", 750)
    cliente4 = Cliente("Luisa Martínez", "luisa@test.com", "101 King's Avenue, Liverpool", 300)
    cliente5 = Cliente("Pedro Sánchez", "pedro@test.com", "222 Park Street, Belfast", 100)
    cliente6 = Cliente("Ana López", "ana@test.com", "333 Castle Road, Cardiff", 600)
    cliente7 = Cliente("Manuel Torres", "manuel@test.com", "444 Prince's Place, Glasgow", 900)

    print("Clientes:")
    print(cliente1)
    print(cliente2)
    print(cliente3)
    print(cliente4)
    print(cliente5)
    print(cliente6)
    print(cliente7)


    cliente1.comprar(300)
    cliente2.comprar(800)
    cliente3.comprar(1000)  
    cliente5.comprar(2000) 
    cliente7.comprar(400)  
    cliente4.recargar_saldo(500)  
    cliente1.recargar_saldo(200)
    cliente6.recargar_saldo(2000)  

if __name__ == "__main__":
    main()