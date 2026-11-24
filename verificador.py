pontos = 50
senha = input("Digite sua senha: ")

if len(senha) < 8:
    print ("A senha não contem caracteres suficientes")
    pontos = pontos - 10
if not any(c.isdigit() for c in senha):
    print ("A senha precisa conter ao menos um número")
    pontos = pontos - 10
if senha.isalnum():
    print("A senha precisa conter caracteres especiais")
    pontos = pontos - 10
if not any(c.isupper() for c in senha):
    print ("A senha precisa conter ao menos um caracter em caixa alta")
    pontos = pontos - 10
if not any (c.islower() for c in senha):
    print("A senha precisa conter ao menos um caracter em caixa baixa")
    pontos = pontos - 10

if pontos < 30:
    print ("Sua senha está Fraca")
elif pontos >=30 and pontos < 50 :
    print ("Sua senha está mediana")
elif pontos == 50:
    print ("Sua senha é forte Parabens!")

''' 
Logica:

SE senha menor que 8 
    SENHA POUCOS CARACTERES
SE senha NÃO tem número
    SENHA PRECISA DE NUMEROS
SE senha é totalmente alfanumerico
    SENHA PRECISA INCLUIR CARACTERES ESPECIAIS
SE senha NÃO tem maiuscula
    SENHA PRECISA TER MAIUSCULAS
SE senha NÃO tem minuscula
    SENHA PRECISA TER MINUSCULA
SE NÃO 
    SENHA FORTE
'''