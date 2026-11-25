import getpass

with open("senhas_fracas.txt", "r", encoding="utf-8") as file:
 
    arquivo = file.read().splitlines()
    print (arquivo)

pontos = 6
senha = getpass.getpass("Digite sua senha: ")
print("Senha Recebida!")

#Aqui os dois lados são convertidos para minusculo
if senha.lower() in [a.lower() for a in arquivo]:
    print("Sua senha foi encontrada em uma lista de senhas padrões")
    pontos = pontos - 1


if len(senha) < 8:
    print ("A senha não contem caracteres suficientes")
    pontos = pontos - 1
if not any(c.isdigit() for c in senha):
    print ("A senha precisa conter ao menos um número")
    pontos = pontos - 1
if senha.isalnum():
    print("A senha precisa conter caracteres especiais")
    pontos = pontos - 1
if not any(c.isupper() for c in senha):
    print ("A senha precisa conter ao menos um caracter em caixa alta")
    pontos = pontos - 1
if not any (c.islower() for c in senha):
    print("A senha precisa conter ao menos um caracter em caixa baixa")
    pontos = pontos - 1

if pontos < 3:
    print ("Sua senha está Fraca")
elif pontos >=3 and pontos < 6 :
    print ("Sua senha está mediana")
elif pontos == 6:
    print ("Sua senha é forte Parabens!")

''' 
Logica:

SE senha menor que 8 
    SENHA POUCOS CARACTERES
    PERDE PONTOS
SE senha NÃO tem número
    SENHA PRECISA DE NUMEROS
    PERDE PONTOS
SE senha é totalmente alfanumerico
    SENHA PRECISA INCLUIR CARACTERES ESPECIAIS
    PERDE PONTOS
SE senha NÃO tem maiuscula
    SENHA PRECISA TER MAIUSCULAS
    PERDE PONTOS
SE senha NÃO tem minuscula
    SENHA PRECISA TER MINUSCULA
    PERDE PONTOS

SE PONTOS MENOR QUE 3
    SUA SENHA É FRACA
SE PONTOS MAIOR QUE ou igual a 3 E MENOR QUE 6
    SUA SENHA É MEDIANA
SE PONTOS IGUAL 6
    SUA SENHA É FORTE 

'''