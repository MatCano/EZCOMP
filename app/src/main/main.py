from antlr4 import *
import os
ROOT_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../'))
import sys
sys.path.append(ROOT_PATH)
from src.parser.IsiLangLexer import IsiLangLexer     
from src.parser.IsiLangParser import IsiLangParser  


def main():
    input_isi = FileStream(f'{ROOT_PATH}/input.isi')
    outputname = 'output' #os.path.basename(input_isi.fileName).split('.')[0].split('\\')[-1]

    lexer = IsiLangLexer(input_isi)
    stream = CommonTokenStream(lexer)
    parser = IsiLangParser(stream)
    tree = parser.prog()
    #print(tree.toStringTree(recog=parser))

    #print(parser._isiProgram)

    print("\n\n---------- ExComp compilou em Python ----------\n")

    print(parser.generatePyCode(outputname+".py"))

    print("\n\n---------- ExComp compilou em C ----------\n")

    print(parser.generateCCode(outputname+".c"))


if __name__ == '__main__':
    main()
