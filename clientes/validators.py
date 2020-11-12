def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11

def nome_valido(nome_do_cliente):
    return nome_do_cliente.isalpha()

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(celular):
    return len(celular) >= 11