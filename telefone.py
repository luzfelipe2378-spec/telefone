def aplicar_mascara_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, telefone)) 
    
    if len(telefone) != 10:
        raise ValueError('Telefone precisa ter 10 dígitos')
    
    return f'({telefone[0:2]}){telefone[2:6]}-{telefone[6:10]}'

print(aplicar_mascara_telefone(input('Digite seu telefone: ')))