#Função - Modo 1 sem parâmetro e sem retorno
def menu():
    print("--- Menu ---")
    print("1- Consultar")
    print("2- Inserir")
    print("3- Excluir")
    
#chamando a fução
menu()

#Função - Modo 2 com parâmetro e sem retorno
def somar(num1, num2):
    print(f"A soma é {num1+num2}")
    
#chamando a função somar
somar(4,5)

#Função - Modo 3 - sem parâmetro com retorno
def dobro():
    valor = int(input("Informe um valor númerico: "))
    
    return valor * 2

#chamando a função
print(f"O dobro é {dobro()}")

#Função - Modo 4 - com parâmetro e com retorno
def triplo(valor):
    resposta = valor * 3
    
    return resposta

#chamndo a função
print(f"O triplo do valor é {triplo(8)}")

#chamndo a função com valor dinâmico
numero = int(input("Informe um valor: "))
print(f"O triplo do valor é {triplo(numero)}")
