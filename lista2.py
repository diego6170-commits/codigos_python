valores = [] # Criando uma lista vazia

for item in range(10,14):
    valores.append(item)
    
print(valores)

# Preenchedo uma lista com dados dinâmicos
valores2 = []
while True:
    num = int(input("Informe um valor númerico qualquer - zero para encerrar: "))
     
    if num == 0:
        break # encerra o sistema
    else:
        valores2.append(num)
        
print("\nPrograma encerrado\n")
print(valores2)

while True:
    num = int(input("Deseja apagar o ultimo item do sistema? 1- Sim e 2- Não: "))
    
    if num == 1:
        valores2.pop()
        print(valores2)
        print("item foi deletado do sistema")
    elif num == 2:
        print("\nPrograma encerrado\n")
        print(valores2)
        break