from my_token import *

def main():
    """
    O analisador léxico funciona como uma máquina de estados, com as regras de negócio definidas no arquivo JFLAP.
    Ele processa o arquivo a ser compilado caractere por caractere, separando os tokens identificados ao longo da leitura.
    Os possíveis tokens estão detalhados no arquivo my_token.py.
    """
    file = IsiScanner('input.isi')
    print(file)
    state = 0
    tokens = []
    term = Token()
    
    debug = False

    if debug:

        print("Modo Debug ativado!\n")
        print("Imprimindo todos os simbolos reconhecidos: \n")

        print("Digits: " + str(digits))
        print("Low keys: " +str(low_keys))
        print("Up keys: " + str(up_keys))
        print("Valid symbols: " + str(valid_symbols))

    while True:
        if file.is_EOF(): break
        if debug:
            print("Estado: " + str(state))
            print("Current char: " + file.current_char)
        match state:
            case 0:
                # O caso 0 é o inicial:
                # Ao ler um caractere nulo (espaço, \n, \r, \t), ele é ignorado e permanecemos no estado 0.
                # Ao ler um caractere minúsculo, identificamos um possível identificador (palavra reservada ou nome de variável), começamos a gravar o token e avançamos para o estado 1.
                # Se o caractere lido for uma vírgula, registramos o token como um separador.
                # Se o caractere lido for um símbolo, mudamos para o estado 2.
                # Ao encontrar aspas duplas ("), iniciamos a leitura de uma String e passamos para o estado 3.
                # Se o caractere lido for um número, avançamos para o estado 4.

                if is_space(file.current_char):
                    file.next_char()
                    continue

                if is_separator(file.current_char):
                    state = 1
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_SEPARATOR)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    continue

                if is_opar(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_OPAR)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    continue

                if is_cpar(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_CPAR)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    continue

                if is_delimiter(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_DELIMITER)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    continue

                if is_okey(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_OKEY)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if is_ckey(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_CKEY)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if is_add_op(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_ADD_OP)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if is_minus_op(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_MINUS_OP)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if is_mul_op(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_MUL_OP)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if is_div_op(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 0
                    term.set_type(CRC_DIV_OP)
                    tokens.append(term)
                    print(term)
                    term = Token()

                    continue

                if file.current_char == ':':
                    state = 5
                    term.append_char(file.current_char)
                    file.next_char()
                    continue

                if is_symbol(file.current_char): ## and (not is_delimiter(file.current_char))
                    state = 2
                    term.append_char(file.current_char)
                    file.next_char()
                    continue

                if file.current_char == '"':
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 3
                    continue

                if is_number(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    state = 4
                    continue

                if is_lower(file.current_char):
                    state = 1
                    term.append_char(file.current_char)
                    file.next_char()
                    continue

                else: 
                    print("caso nao tratado no estado 0")
                    print("char: " + file.current_char)
                    input()
            case 1:
                # O estado 1 indica que a leitura de um identificador foi iniciada.
                # Se o caractere lido for uma letra ou número, a leitura do token continua.
                # Se for um espaço vazio, a leitura do token é finalizada e retornamos ao estado 0.
                # Se o caractere lido for um símbolo, a gravação do token é concluída e voltamos ao estado 0, porém, o caractere atual não é atualizado, pois ele pode fazer parte do próximo token.
                if is_letter(file.current_char) or is_number(file.current_char):
                    state = 1
                    term.append_char(file.current_char)
                    file.next_char()
                    continue
                if is_space(file.current_char) or is_symbol(file.current_char) or is_separator(file.current_char):
                    state = 0
                    if is_command(term.get_text()):
                        term.set_type(CRC_RESERVED_ID)
                    else:
                        term.set_type(CRC_IDENTIFIER)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    continue
            case 2:
                # O estado 2 indica o início da leitura de um símbolo.
                # Se o caractere lido for outro símbolo, a leitura do token continua.
                # Se o caractere lido não for um símbolo, a leitura do token é encerrada e retornamos ao estado 0, sem avançar para o próximo caractere, já que o caractere atual pode pertencer ao próximo token.
                if is_symbol(file.current_char): ## and not is_delimiter(file.current_char)
                    term.append_char(file.current_char)
                    file.next_char()
                    continue
                else:
                    term.set_type(CRC_OPERATOR)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    state = 0
                    continue
            case 3:
                # O estado 3 indica que estamos dentro de um bloco de texto (String).
                # A leitura do token continua enquanto os caracteres forem válidos.
                # Se o caractere lido for uma aspas duplas ("), o token de texto é finalizado e retornamos ao estado 0.
                if is_valid(file.current_char) and file.current_char != '"':
                    term.append_char(file.current_char)
                    file.next_char()
                    continue
                if file.current_char == '"':
                    term.append_char(file.current_char)
                    term.set_type(CRC_TEXT)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    file.next_char()
                    state = 0
                    continue
            case 4:
                # O estado 4 indica o início da leitura de um número, que pode ser um inteiro ou um número decimal (double).
                # A leitura do token continua enquanto o caractere for um número ou um ponto decimal.
                # Se o caractere lido for um ponto (.), o token é classificado como DOUBLE.
                if is_number(file.current_char):
                    term.append_char(file.current_char)
                    file.next_char()
                    continue
                if is_double(file.current_char):
                    term.append_char(file.current_char)
                    term.set_type(CRC_NUMBER_DOUBLE)
                    file.next_char()
                    continue
                if is_space(file.current_char):

                    if term.get_type() == '':
                        term.set_type(CRC_NUMBER_INT)
                        
                    tokens.append(term)
                    print(term)
                    term = Token()
                    file.next_char()
                    state = 0
                    continue
                else:
                    print("Exception - Invalid number!")
            case 5:
                # O estado 5 indica o início da leitura de um operador de atribuição (:=).
                if file.current_char == '=':
                    term.append_char(file.current_char)
                    term.set_type(CRC_ASSIGN)
                    tokens.append(term)
                    print(term)
                    term = Token()
                    file.next_char()
                    state = 0
                    continue

if __name__ == '__main__':
    main()