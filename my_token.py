import traceback
import os
import sys

numbers = [x for x in '0123456789']
low_keys = [x for x in 'abcdefghijklmnopqrstuvwxyz']
up_keys = [x for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
valid_symbols = [x for x in "+-*/()[]{}'.;,<>:="]
commands = {
    "start"  : '',
    "end"  : '',
    "var"   : '',
    "input"      : '',
    "print"   : '',
    "if"        : '',
    "then"     : '',
    "else"     : '',
}

CRC_IDENTIFIER    = 0
CRC_NUMBER        = 1
CRC_OPERATOR      = 2
CRC_DELIMITER     = 3
CRC_ASSIGN        = 4
CRC_TEXT          = 5
CRC_NUMBER_INT    = 6
CRC_NUMBER_DOUBLE = 7
CRC_SEPARATOR     = 8 
CRC_OPAR          = 9
CRC_CPAR          = 10
CRC_RESERVED_ID   = 11 
CRC_OKEY          = 12
CRC_CKEY          = 13
CRC_ADD_OP        = 14
CRC_MINUS_OP      = 15
CRC_MUL_OP        = 16
CRC_DIV_OP        = 17

def is_number(symbol):
    return symbol in numbers

def is_lower(symbol):
    return symbol in low_keys

def is_upper(symbol):
    return symbol in up_keys

def is_letter(symbol):
    return is_lower(symbol) or is_upper(symbol)

def is_symbol(symbol):
    return symbol in valid_symbols

def is_space(symbol):
    return symbol in [' ', '\t', '\n', '\r']

def is_operator(symbol):
    return symbol in ['<', '>', '=', '!', ':']

def is_valid(symbol):
    return is_letter(symbol) or is_number(symbol) or is_symbol(symbol) or is_operator(symbol) or symbol == ' '

def is_delimiter(symbol):
    return symbol == ';'

def is_double(symbol):
    return symbol == '.'

def is_separator(symbol):
    return symbol == ','

def is_opar(symbol):
    return symbol == '('

def is_cpar(symbol):
    return symbol == ')'

def is_okey(symbol):
    return symbol == '{'

def is_ckey(symbol):
    return symbol == '}'

def is_add_op(symbol):
    return symbol == '+'

def is_minus_op(symbol):
    return symbol == '-'

def is_mul_op(symbol):
    return symbol == '*'

def is_div_op(symbol):
    return symbol == '/'

def is_command(symbol):
    try:
        check = commands[symbol]
    except KeyError:
        check = None
    return check is not None

class IsiScanner():
    '''
    A classe IsiScanner atua como um navegador do arquivo, implementando funções responsáveis por ler o próximo caractere, retroceder um caractere e identificar o fim do arquivo.
    '''
    def __init__(self, filename):
        self.pos = 0
        try:
            with open('/'.join([os.getcwd(), filename]), 'r') as file:
                self.content = file.read()
        except Exception as e:
            print(traceback.format_exc())
            exit(1)
        self.current_char = self.content[self.pos]

    def next_char(self):
        self.pos += 1
        self.current_char = self.content[self.pos]

    def back(self):
        self.pos -= 1
        self.current_char = self.content[self.pos]

    def is_EOF(self):
        return self.pos == len(self.content)-1

    def __str__(self):
        return self.content

class Token():
    '''
    A classe Token define os tokens, que possuem um tipo (atribuído ao final de sua leitura) e um texto (incrementado durante o processo de leitura).
    A classe também implementa os métodos que permitem definir o tipo e o texto do token, além de adicionar novos caracteres ao token conforme necessário.
    '''
    tk_text = ''
    tk_type = ''
    def set_text(self, text):
        self.tk_text = text

    def append_char(self, char):
        self.tk_text = self.tk_text + char
    
    def set_type(self, type_txt):
        self.tk_type = type_txt
    
    def get_text(self):
        return self.tk_text

    def get_type(self):
        return self.tk_type

    def __str__(self):
        return f'[Token Type = {self.tk_type}, Text = {self.tk_text}]'
