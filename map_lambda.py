# Procedural
# Vamos criar uma maneira de pegar a primeira lista e transformar em uma nova com o dobro dos valores da lista 1
a=[1,2,3]
a2=[]

for i in a:
    a2.append(i*2)
print("Estrutura Procedural")
print(a2)
print("="*30)
# Funcional usando Map e Lambda

print("Funcional MAP")
# Mapeia os elementos para uma nova lista, sem modificar a primeira.
m=map(lambda i: i*2,a)
print(list(m))


#  Funcional Lambda

produtos=(
    {"quantidade":2,"preco":10},
    {"quantidade":23,"preco":89},
    {"quantidade":11,"preco":7},
)

print("=====Lambda=====")
total= tuple(
    map(
        lambda produto:produto['quantidade']*produto['preco'],produtos
    )
)

print(total)
print(f"O total dos produtos é R${sum(total)}")

# Função Lambda Alternativa usando procedural 

print("Lambda Alternativa")
produtos2=(
    {"quantidade":2,"preco":10},
    {"quantidade":23,"preco":89},
    {"quantidade":11,"preco":7},
)


def calc_preco_total(produto):
    return produto['quantidade']*produto['preco']

total=list(map(calc_preco_total,produtos2))

print("Total de cada produto",total)
print("Total R$",float(sum(total)))