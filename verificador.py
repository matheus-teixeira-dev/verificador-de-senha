senha = input("Digite sua senha: ")

if len(senha) <= 8 :
    print ("a senha não contem caracteres suficientes")
#a função isalnum() verifica se todo o texto é alfanumerico (numeros e letras) se for ele retorna true se não false
#o NOT na frente tem o intuito de indicar que a string não é apenas alfanumerico então é como fosse "SE não é apenas alfanumerico?"
elif not any(c.isdigit() for c in senha):
    print("precisa conter pelo menos um número na senha")
elif senha.isalnum():
    print ("a senha precisa incluir caracteres especiais")
elif not any(c.isupper() for c in senha):
    print ("a senha precisa incluir pelo menos uma letra maiuscula")
elif not any(c.islower() for c in senha):
    print ("a senha precisa incluir pelo menos uma letra minuscula")
else:
    print("Senha Forte")

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