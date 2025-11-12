# Função que irá somar valores
def soma_ate(n):
    # Caso base: se n for igual 1 devolve 1 
    if n == 1:
        return 1
    
    # Caso recursivo: n + soma dos anteriores
    return n + soma_ate(n-1)

# chamando a função - exemplos

print(soma_ate(3))



# Função que irá somar valores
def soma_ate(n):
    print(f"Entrando na soma_ate({n})")
    if n == 1:
        print("-> Caso base! Retornando")
        return 1
    
    resultado = n + soma_ate(n-1)
    print(f"<- Retornando {n} + ... = {resultado}")
    
    return resultado

# chamando a função - exemplos

print(soma_ate(3))