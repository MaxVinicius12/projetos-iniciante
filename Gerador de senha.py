from random import choice
import string

tamanho_da_senha = int(input("Informe o tamanho da senha: "))
caractere = (string.ascii_letters + string.digits + string.punctuation)
senha_segura = ''
for i in range(tamanho_da_senha):
    senha_segura += choice(caractere)

print(senha_segura)
print(f"O tamanho da senha é: {len(senha_segura)}")