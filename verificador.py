import getpass

with open("senhas_fracas.txt", "r", encoding="utf-8") as file:
    arquivo = file.read().splitlines()
    

pontos = 6
senha = getpass.getpass("Digite sua senha: ")
print("Senha Recebida!")



#verifica cada linha dentro do arquivo e compara se tem na senha
for palavra in arquivo:
    if palavra.lower() in senha.lower():
        sobra = len(senha) - len(palavra)
        if sobra < 5:
            print ("a seguinte senha foi encontrada em uma lista de senhas vazadas: ",palavra,"recomendamos adicionar mais algumas coisas ou criar outra.")
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

if pontos < 4:
    print ("Sua senha está Fraca")
elif pontos >=4 and pontos < 6 :
    print ("Sua senha está mediana")
elif pontos == 6:
    print ("Sua senha é forte Parabens!")

