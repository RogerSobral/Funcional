#!/usr/local/bin/python3

def multiplicar(x):
    #  A FUnção Calcular tem consciencia que esta dentro de Multiplicar, sendo assim ela tem acesso ao parametro que entrou na função Multiplicar
    def calcular(y):
        # Vai ocorrer uma avaliação tardia, o valor que entrar primeiro vai ser armazenado, esperando o segundo ser realizado 
        return x*y
    return calcular

if __name__=="__main__":
    #  Aqui estamos carregando o valor de X
    dobro=multiplicar(2) 
    triplo=multiplicar(3)
    print(dobro)
    print(triplo)
    # Agora vamos de modo tardio enviar o valor de Y
    print(f"o Triplo de 3 é {triplo(3)}")
    print(f"o dobro de 7 é {dobro(7)}")