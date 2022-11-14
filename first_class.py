a=[10,20,100]
b=a

print(b[1])
b[1]=11
print(a)




# First Class Functions

def dobro(x):
    return x*2

def quadrado(x):
    return x**2

if __name__=="__main__":
    # vai retornar alternadamente as duas funções criadas
    funcs=[dobro,quadrado]*5

    for func, numero in zip(funcs, range(1,11)):
        print(f"o {func.__name__} de {numero} é {func(numero)}")


    print("#"*30)

    a=dobro
    print(a(13))

    q=quadrado
    print(q(a(34)))

