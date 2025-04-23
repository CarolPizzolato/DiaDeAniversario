import sys
# dia nao pode ser maior que 31

#teste dia
try:
    dia = int (input("Digite o dia do seu aniversáio: "))
    if dia > 31 or dia <= 0:
        print("Dia inválido")
        sys.exit()

    
except ValueError:
    print ("Digite um número por favor")
    sys.exit()

    
#teste mes

try:
    mes = int(input("Digite o mês do seu nascimento: "))
    if mes > 12 or mes < 1:
        print("Mês inválido")
        sys.exit()

except ValueError:
    print ("Digite um número por favor")
    sys.exit()

try:
    ano = int(input("Digite o ano: "))
    if ano < 1900 or ano > 2025:  
        print("Ano inválido")
        sys.exit()

except ValueError:
    print ("Digite um número por favor")
    sys.exit()                         

print (f"{dia}/{mes}/{ano}")
