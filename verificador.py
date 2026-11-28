import getpass

try:
    with open("senhas_fracas.txt", "r", encoding="utf-8") as file:
        arquivo = file.read().splitlines()
    
except FileNotFoundError:
    print ("arquivo senhas_fracas.txt não encontrado seguindo sem ele")
    arquivo = []

def tem_numero (senha):
    return any(s.isdigit() for s in senha)

def tem_maiuscula (senha):
    return any(s.isupper() for s in senha)

def tem_minuscula(senha):
    return any(s.islower() for s in senha)

def tem_simbolo(senha):
    return not senha.isalnum()

def tamanho(senha):
    return len(senha) >= 8

def compararsenha(senha,arquivo):
    for palavra in arquivo:
        if palavra.lower() in senha.lower():
            sobra = len(senha) - len(palavra)
            if sobra < 5:
                return palavra
    return None

def classificar_senha(pontos):
    if pontos < 4:
        return print ("Sua senha está Fraca")
    elif pontos == 6:
        return print ("Sua senha é forte Parabens!")    
    elif pontos >=4:
        return print ("Sua senha está mediana")

pontos = 6
senha = getpass.getpass("Digite sua senha: ")
print("Senha Recebida!")

palavra_comum = compararsenha(senha,arquivo)

if palavra_comum is not None:
    print ("a seguinte senha foi encontrada em uma lista de senhas comuns: ´",palavra_comum,"´recomendamos adicionar mais algumas coisas ou criar outra.")
    pontos = pontos - 1

if not tamanho(senha):
    print ("A senha não contem caracteres suficientes")
    pontos = pontos - 1
if not tem_numero(senha):
    print ("A senha precisa conter ao menos um número")
    pontos = pontos - 1
if not tem_simbolo(senha):
    print("A senha precisa conter caracteres especiais")
    pontos = pontos - 1
if not tem_maiuscula(senha):
    print ("A senha precisa conter ao menos um caracter em caixa alta")
    pontos = pontos - 1
if not tem_minuscula(senha):
    print("A senha precisa conter ao menos um caracter em caixa baixa")
    pontos = pontos - 1

classificar_senha(pontos)