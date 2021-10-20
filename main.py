import rsa
# Entrada de dados do usuário 
print('entre com o seu usuario')
login = input()

print('entre com sua senha')
password = input()

# print(login +"\n"+ password) (pular linha entre o login / password)


# - Verificar se o usuário existe no DB



# - Tratamento dos dados do usuário 
user = {
    login,
    password
}


# - Se não existe, avise o usuário 
# - Se existe, criptografar as credenciais com a Chave Pública do usuário 
# - Enviar as credenciais criptografadas para o servidor
# - Verificar e validar as credenciais do usuário com as no banco de dados
# - Se valido, retorna o acesso ao usuário 
# - Se inválido, retorna ao usuário que "o usuário ou senha estão incorretos"