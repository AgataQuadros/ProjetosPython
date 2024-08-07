def dividir(a, b):
    '''Método para dividir 2 números
    Args:
        a (Any): Dividendo
        b (Any): Divisor
        
    Returns:
    str: Mensagem de erro ou "OK!" se a divisão for bem-sucedida
    any: Quociente ou Nome em caso de erro
    '''
    if b == 0:
        return None, 'Erro de divisão'
    else:
        divisao = a/b
        return divisao, 'OK!'