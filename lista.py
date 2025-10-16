# Criando uma lista
numeros = [3, 5, 8, 10, 14]

# print(type(lista))

print(numeros)

numeros[2] = 15 # Alterando o valor do índice 2


# Exibir todos os números
for item in numeros:
    print(item)
    
    
# Inserindo valores na lista
numeros.append(23)

print(numeros)

# Adicionando item em qualquer lugar
numeros.insert(2,90)# iremos inserir o valor 90 no índice 2 
print(numeros)

#Removendo item da lista
numeros.pop()# removendo item no final da lista
print(numeros)
