senha = input("Digite sua senha: ")

if len(senha) < 8 :
    print ("senha não contem caracteres suficientes")
#a função isalnum() verifica se todo o texto é alfanumerico (numeros e letras) se for ele retorna true se não false
#o NOT na frente tem o intuito de indicar que a string não é apenas alfanumerico então é como fosse "SE não é apenas alfanumerico?"
elif not senha.isalnum():
    print ("senha forte")
else:
    print ("senha precisa incluir caracteres especiais")