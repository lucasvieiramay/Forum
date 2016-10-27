#-*- coding: utf -8 -*-

#Testa se a senha e segura
def senha_segura(senha):
    #minimo de digitos
    senha = str(senha)
    min_length = 6
    if len(senha) < min_length:
        return False
    # testa se tem um digito
    if not any(char.isdigit() for char in senha):
        return False
    # testa se tem letras
    if not any(char.isalpha() for char in senha):
        return False

    return True
