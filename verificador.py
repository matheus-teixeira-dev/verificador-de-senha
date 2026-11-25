import getpass

pontos = 5
senha = getpass.getpass("Digite sua senha: ")
print("Senha Recebida!")

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
elif pontos >=3 and pontos < 5 :
    print ("Sua senha está mediana")
elif pontos == 5:
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
SE PONTOS MAIOR QUE 3 E MENOR QUE 5
    SUA SENHA É MEDIANA
SE PONTOS IGUAL 5
    SUA SENHA É FORTE 

'''