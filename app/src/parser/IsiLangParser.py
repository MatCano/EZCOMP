# Generated from IsiLang.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

 

from isiExceptions import IsiSemanticException
from isiSymbol import IsiSymbol
from isiVariable import IsiVariable
from isiSymbolTable import IsiSymbolTable
from isiProgram import IsiProgram, AbstractCommand, ReadCommand, WriteCommand, AttribCommand, DecisionCommand, WhileCommand



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("\u014e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\39\n\3\r\3\16\3:\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4C\n\4\f\4\16\4F\13\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5P\n\5\3\6\3\6\6\6T\n\6\r\6\16")
        buf.write("\6U\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7b\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n}\n\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\5\f\u008b\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\6\r\u0099\n\r\r\r\16\r\u009a\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\6\16\u00a7\n\16\r\16\16")
        buf.write("\16\u00a8\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\5\17\u00b4\n\17\3\17\3\17\3\17\3\17\6\17\u00ba\n\17\r")
        buf.write("\17\16\17\u00bb\3\17\3\17\3\17\3\17\6\17\u00c2\n\17\r")
        buf.write("\17\16\17\u00c3\3\17\3\17\3\20\3\20\5\20\u00ca\n\20\3")
        buf.write("\21\3\21\3\21\5\21\u00cf\n\21\3\21\3\21\3\21\3\21\6\21")
        buf.write("\u00d5\n\21\r\21\16\21\u00d6\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00fa\n\24\f\24\16")
        buf.write("\24\u00fd\13\24\3\24\3\24\3\24\3\24\6\24\u0103\n\24\r")
        buf.write("\24\16\24\u0104\3\24\3\24\3\24\3\24\3\24\3\24\6\24\u010d")
        buf.write("\n\24\r\24\16\24\u010e\3\24\3\24\3\24\5\24\u0114\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\7\25\u0125\n\25\f\25\16\25\u0128")
        buf.write("\13\25\3\25\3\25\3\25\3\25\6\25\u012e\n\25\r\25\16\25")
        buf.write("\u012f\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\7\26\u013c\n\26\f\26\16\26\u013f\13\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\5\27\u0149\n\27\3\30\3\30")
        buf.write("\3\30\3\30\2\2\31\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\2\3\3\2\27\32\2\u015d\2\60\3\2\2\2\48\3\2")
        buf.write("\2\2\6<\3\2\2\2\bO\3\2\2\2\nQ\3\2\2\2\fa\3\2\2\2\16c\3")
        buf.write("\2\2\2\20k\3\2\2\2\22t\3\2\2\2\24\u0081\3\2\2\2\26\u008a")
        buf.write("\3\2\2\2\30\u008c\3\2\2\2\32\u009e\3\2\2\2\34\u00b0\3")
        buf.write("\2\2\2\36\u00c9\3\2\2\2 \u00cb\3\2\2\2\"\u00da\3\2\2\2")
        buf.write("$\u00e4\3\2\2\2&\u00ec\3\2\2\2(\u0117\3\2\2\2*\u0134\3")
        buf.write("\2\2\2,\u0148\3\2\2\2.\u014a\3\2\2\2\60\61\b\2\1\2\61")
        buf.write("\62\7\3\2\2\62\63\5\4\3\2\63\64\5\n\6\2\64\65\7\4\2\2")
        buf.write("\65\66\b\2\1\2\66\3\3\2\2\2\679\5\6\4\28\67\3\2\2\29:")
        buf.write("\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\5\3\2\2\2<=\5\b\5\2=>\7")
        buf.write("\30\2\2>D\b\4\1\2?@\7\22\2\2@A\7\30\2\2AC\b\4\1\2B?\3")
        buf.write("\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2")
        buf.write("\2GH\7\17\2\2H\7\3\2\2\2IJ\7\5\2\2JP\b\5\1\2KL\7\6\2\2")
        buf.write("LP\b\5\1\2MN\7\7\2\2NP\b\5\1\2OI\3\2\2\2OK\3\2\2\2OM\3")
        buf.write("\2\2\2P\t\3\2\2\2QS\b\6\1\2RT\5\f\7\2SR\3\2\2\2TU\3\2")
        buf.write("\2\2US\3\2\2\2UV\3\2\2\2V\13\3\2\2\2Wb\5\24\13\2Xb\5\16")
        buf.write("\b\2Yb\5\20\t\2Zb\5\22\n\2[b\5\26\f\2\\b\5\36\20\2]b\5")
        buf.write("$\23\2^b\5&\24\2_b\5(\25\2`b\5.\30\2aW\3\2\2\2aX\3\2\2")
        buf.write("\2aY\3\2\2\2aZ\3\2\2\2a[\3\2\2\2a\\\3\2\2\2a]\3\2\2\2")
        buf.write("a^\3\2\2\2a_\3\2\2\2a`\3\2\2\2b\r\3\2\2\2cd\7\b\2\2de")
        buf.write("\7\r\2\2ef\7\30\2\2fg\b\b\1\2gh\7\16\2\2hi\7\17\2\2ij")
        buf.write("\b\b\1\2j\17\3\2\2\2kl\7\t\2\2lm\b\t\1\2mn\7\r\2\2no\5")
        buf.write(",\27\2op\b\t\1\2pq\7\16\2\2qr\7\17\2\2rs\b\t\1\2s\21\3")
        buf.write("\2\2\2tu\7\30\2\2uv\b\n\1\2v|\7\r\2\2w}\7\30\2\2x}\7\31")
        buf.write("\2\2y}\5*\26\2z}\5,\27\2{}\7\32\2\2|w\3\2\2\2|x\3\2\2")
        buf.write("\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}~\3\2\2\2~\177\7\16\2")
        buf.write("\2\177\u0080\7\17\2\2\u0080\23\3\2\2\2\u0081\u0082\7\b")
        buf.write("\2\2\u0082\u0083\7\r\2\2\u0083\u0084\7\16\2\2\u0084\u0085")
        buf.write("\b\13\1\2\u0085\u0086\7\17\2\2\u0086\25\3\2\2\2\u0087")
        buf.write("\u008b\5\34\17\2\u0088\u008b\5\30\r\2\u0089\u008b\5\32")
        buf.write("\16\2\u008a\u0087\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\27\3\2\2\2\u008c\u008d\7\n\2\2\u008d\u008e")
        buf.write("\7\r\2\2\u008e\u008f\7\30\2\2\u008f\u0090\7\25\2\2\u0090")
        buf.write("\u0091\5,\27\2\u0091\u0092\7\16\2\2\u0092\u0093\7\23\2")
        buf.write("\2\u0093\u0094\7\24\2\2\u0094\u0095\b\r\1\2\u0095\u0096")
        buf.write("\7\13\2\2\u0096\u0098\7\23\2\2\u0097\u0099\5\f\7\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\7")
        buf.write("\24\2\2\u009d\31\3\2\2\2\u009e\u009f\7\n\2\2\u009f\u00a0")
        buf.write("\7\r\2\2\u00a0\u00a1\7\30\2\2\u00a1\u00a2\7\25\2\2\u00a2")
        buf.write("\u00a3\5,\27\2\u00a3\u00a4\7\16\2\2\u00a4\u00a6\7\23\2")
        buf.write("\2\u00a5\u00a7\5\f\7\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa\u00ab\7\24\2\2\u00ab\u00ac\7\13\2")
        buf.write("\2\u00ac\u00ad\7\23\2\2\u00ad\u00ae\7\24\2\2\u00ae\u00af")
        buf.write("\b\16\1\2\u00af\33\3\2\2\2\u00b0\u00b1\7\n\2\2\u00b1\u00b3")
        buf.write("\7\r\2\2\u00b2\u00b4\t\2\2\2\u00b3\u00b2\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\7\16\2")
        buf.write("\2\u00b6\u00b7\b\17\1\2\u00b7\u00b9\7\23\2\2\u00b8\u00ba")
        buf.write("\5\f\7\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00be\7\24\2\2\u00be\u00bf\7\13\2\2\u00bf\u00c1")
        buf.write("\7\23\2\2\u00c0\u00c2\5\f\7\2\u00c1\u00c0\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5\u00c6\7\24\2\2\u00c6\35\3\2")
        buf.write("\2\2\u00c7\u00ca\5 \21\2\u00c8\u00ca\5\"\22\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\37\3\2\2\2\u00cb\u00cc")
        buf.write("\7\f\2\2\u00cc\u00ce\7\r\2\2\u00cd\u00cf\t\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d1\7\16\2\2\u00d1\u00d2\b\21\1\2\u00d2\u00d4")
        buf.write("\7\23\2\2\u00d3\u00d5\5\f\7\2\u00d4\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\u00d8\3\2\2\2\u00d8\u00d9\7\24\2\2\u00d9!\3\2\2")
        buf.write("\2\u00da\u00db\7\f\2\2\u00db\u00dc\7\r\2\2\u00dc\u00dd")
        buf.write("\7\30\2\2\u00dd\u00de\7\25\2\2\u00de\u00df\5,\27\2\u00df")
        buf.write("\u00e0\7\16\2\2\u00e0\u00e1\7\23\2\2\u00e1\u00e2\7\24")
        buf.write("\2\2\u00e2\u00e3\b\22\1\2\u00e3#\3\2\2\2\u00e4\u00e5\7")
        buf.write("\30\2\2\u00e5\u00e6\b\23\1\2\u00e6\u00e7\7\21\2\2\u00e7")
        buf.write("\u00e8\b\23\1\2\u00e8\u00e9\5*\26\2\u00e9\u00ea\7\17\2")
        buf.write("\2\u00ea\u00eb\b\23\1\2\u00eb%\3\2\2\2\u00ec\u00ed\7\n")
        buf.write("\2\2\u00ed\u00ee\7\r\2\2\u00ee\u00ef\7\30\2\2\u00ef\u00f0")
        buf.write("\b\24\1\2\u00f0\u00f1\7\25\2\2\u00f1\u00f2\b\24\1\2\u00f2")
        buf.write("\u00f3\5,\27\2\u00f3\u00fb\b\24\1\2\u00f4\u00f5\7\26\2")
        buf.write("\2\u00f5\u00f6\b\24\1\2\u00f6\u00f7\5,\27\2\u00f7\u00f8")
        buf.write("\b\24\1\2\u00f8\u00fa\3\2\2\2\u00f9\u00f4\3\2\2\2\u00fa")
        buf.write("\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2")
        buf.write("\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7")
        buf.write("\16\2\2\u00ff\u0100\7\23\2\2\u0100\u0102\b\24\1\2\u0101")
        buf.write("\u0103\5\f\7\2\u0102\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0106\3")
        buf.write("\2\2\2\u0106\u0107\7\24\2\2\u0107\u0113\b\24\1\2\u0108")
        buf.write("\u0109\7\13\2\2\u0109\u010a\7\23\2\2\u010a\u010c\b\24")
        buf.write("\1\2\u010b\u010d\5\f\7\2\u010c\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write("\u0110\3\2\2\2\u0110\u0111\7\24\2\2\u0111\u0112\b\24\1")
        buf.write("\2\u0112\u0114\3\2\2\2\u0113\u0108\3\2\2\2\u0113\u0114")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\b\24\1\2\u0116")
        buf.write("\'\3\2\2\2\u0117\u0118\7\f\2\2\u0118\u0119\7\r\2\2\u0119")
        buf.write("\u011a\7\30\2\2\u011a\u011b\b\25\1\2\u011b\u011c\7\25")
        buf.write("\2\2\u011c\u011d\b\25\1\2\u011d\u011e\5,\27\2\u011e\u0126")
        buf.write("\b\25\1\2\u011f\u0120\7\26\2\2\u0120\u0121\b\25\1\2\u0121")
        buf.write("\u0122\5,\27\2\u0122\u0123\b\25\1\2\u0123\u0125\3\2\2")
        buf.write("\2\u0124\u011f\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u012a\7\16\2\2\u012a\u012b\7\23\2")
        buf.write("\2\u012b\u012d\b\25\1\2\u012c\u012e\5\f\7\2\u012d\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\7\24\2")
        buf.write("\2\u0132\u0133\b\25\1\2\u0133)\3\2\2\2\u0134\u013d\5,")
        buf.write("\27\2\u0135\u0136\7\20\2\2\u0136\u0137\b\26\1\2\u0137")
        buf.write("\u013c\5,\27\2\u0138\u0139\7\26\2\2\u0139\u013a\b\26\1")
        buf.write("\2\u013a\u013c\5,\27\2\u013b\u0135\3\2\2\2\u013b\u0138")
        buf.write("\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e+\3\2\2\2\u013f\u013d\3\2\2\2\u0140")
        buf.write("\u0141\7\30\2\2\u0141\u0149\b\27\1\2\u0142\u0143\7\31")
        buf.write("\2\2\u0143\u0149\b\27\1\2\u0144\u0145\7\32\2\2\u0145\u0149")
        buf.write("\b\27\1\2\u0146\u0147\7\27\2\2\u0147\u0149\b\27\1\2\u0148")
        buf.write("\u0140\3\2\2\2\u0148\u0142\3\2\2\2\u0148\u0144\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0149-\3\2\2\2\u014a\u014b\7\13\2")
        buf.write("\2\u014b\u014c\b\30\1\2\u014c/\3\2\2\2\32:DOUa|\u008a")
        buf.write("\u009a\u00a8\u00b3\u00bb\u00c3\u00c9\u00ce\u00d6\u00fb")
        buf.write("\u0104\u010e\u0113\u0126\u012f\u013b\u013d\u0148")
        return buf.getvalue()


class IsiLangParser ( Parser ):

    grammarFileName = "IsiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'programa'", "'fimprog;'", "'numero'", 
                     "'texto'", "'booleano'", "'leia'", "'escreva'", "'se'", 
                     "'senao'", "'enquanto'", "'('", "')'", "';'", "<INVALID>", 
                     "'='", "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "AP", "FP", 
                      "SC", "OP", "ATTR", "VIR", "ACH", "FCH", "OPREL", 
                      "OPLOG", "BOOL", "ID", "NUMBER", "TEXT", "WS", "MLCOMMENT", 
                      "SLCOMMENT" ]

    RULE_prog = 0
    RULE_decl = 1
    RULE_declaravar = 2
    RULE_tipo = 3
    RULE_bloco = 4
    RULE_cmd = 5
    RULE_cmdleitura = 6
    RULE_cmdescrita = 7
    RULE_invalidcmd = 8
    RULE_invalidcmdleitura = 9
    RULE_invalidcmdselecao = 10
    RULE_invalidcmdselecaocmdv = 11
    RULE_invalidcmdselecaocmdf = 12
    RULE_invalidcmdselecaocond = 13
    RULE_invalidcmdenquanto = 14
    RULE_invalidcmdenquantocond = 15
    RULE_invalidcmdenquantocmd = 16
    RULE_cmdattrib = 17
    RULE_cmdselecao = 18
    RULE_cmdenquanto = 19
    RULE_expr = 20
    RULE_termo = 21
    RULE_invalidelse = 22

    ruleNames =  [ "prog", "decl", "declaravar", "tipo", "bloco", "cmd", 
                   "cmdleitura", "cmdescrita", "invalidcmd", "invalidcmdleitura", 
                   "invalidcmdselecao", "invalidcmdselecaocmdv", "invalidcmdselecaocmdf", 
                   "invalidcmdselecaocond", "invalidcmdenquanto", "invalidcmdenquantocond", 
                   "invalidcmdenquantocmd", "cmdattrib", "cmdselecao", "cmdenquanto", 
                   "expr", "termo", "invalidelse" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    AP=11
    FP=12
    SC=13
    OP=14
    ATTR=15
    VIR=16
    ACH=17
    FCH=18
    OPREL=19
    OPLOG=20
    BOOL=21
    ID=22
    NUMBER=23
    TEXT=24
    WS=25
    MLCOMMENT=26
    SLCOMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    def setTipo(self, tipo):
      self._tipo = tipo
    def getTipo(self):
      return self._tipo


    def checkVar(self, varName):
      if not self._isiProgram._varTable.exists(varName):
        raise IsiSemanticException("Erro Semantico! A variavel {} NAO existe! ".format(varName))
      self._isiProgram._varTable.setUsed(varName)

    def checkVarType(self, var):
      if var.getTypeStr() != self._exprType and self._exprType != "any":
        raise IsiSemanticException("Erro Semantico! Esperava valor do tipo {}, mas recebeu {}, que possui tipo {}! ".format( self._exprType, var.getName(), var.getTypeStr()))

    def generatePyCode(self, outputname="stdOutput.py"):
        return self._isiProgram.generatePyTarget(outputname)

    def generateCCode(self, outputname="stdOutput.c"):
        return self._isiProgram.generateCTarget(outputname)
         



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(IsiLangParser.DeclContext,0)


        def bloco(self):
            return self.getTypedRuleContext(IsiLangParser.BlocoContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = IsiLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)

            self._isiProgram = IsiProgram()
            self._readIDCommand = None
            self._curThread = []
            self._stack = []
            self._exprID = None
            self._exprContent = None
            self._exprDecision = None
            self._exprDecisionStack = []
            self._trueList = []
            self._falseList = []
            self._cmdList   = []
            self._exprType = None
            self._elseCheck = False
            self._elseCheckStack = []


            self.state = 47
            self.match(IsiLangParser.T__0)
            self.state = 48
            self.decl()
            self.state = 49
            self.bloco()
            self.state = 50
            self.match(IsiLangParser.T__1)

            self._isiProgram._varTable.checkUnused()
            self._isiProgram.setCommands(self._stack.pop())

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaravar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.DeclaravarContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.DeclaravarContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = IsiLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 53
                self.declaravar()
                self.state = 56 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__2) | (1 << IsiLangParser.T__3) | (1 << IsiLangParser.T__4))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaravarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(IsiLangParser.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def VIR(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.VIR)
            else:
                return self.getToken(IsiLangParser.VIR, i)

        def getRuleIndex(self):
            return IsiLangParser.RULE_declaravar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaravar" ):
                listener.enterDeclaravar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaravar" ):
                listener.exitDeclaravar(self)




    def declaravar(self):

        localctx = IsiLangParser.DeclaravarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaravar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.tipo()
            self.state = 59
            self.match(IsiLangParser.ID)

            symbol = IsiVariable(self._ctx.getChild(-1), self.getTipo(), None, False)

            if(self._isiProgram._varTable.exists(str(symbol.getName())) == False):
                 self._isiProgram._varTable.add(symbol)
            else:
                 raise IsiSemanticException("Erro Semantico! A variavel {} ja existe, e nao pode ser declarada novamente!".format(symbol.getName()))
                                
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.VIR:
                self.state = 61
                self.match(IsiLangParser.VIR)
                self.state = 62
                self.match(IsiLangParser.ID)

                symbol = IsiVariable(self._ctx.getChild(-1), self.getTipo(), None, False)

                if(self._isiProgram._varTable.exists(str(symbol.getName())) == False):
                     self._isiProgram._varTable.add(symbol)
                else:
                     raise IsiSemanticException("Erro Semantico! A variavel {} ja existe, e nao pode ser declarada novamente!".format(symbol.getName()))

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(IsiLangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsiLangParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = IsiLangParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.match(IsiLangParser.T__2)

                self.setTipo(IsiVariable.NUMBER)
                                    
                pass
            elif token in [IsiLangParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(IsiLangParser.T__3)

                self.setTipo(IsiVariable.TEXT)
                                    
                pass
            elif token in [IsiLangParser.T__4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(IsiLangParser.T__4)

                self.setTipo(IsiVariable.BOOL) 

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = IsiLangParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)

            self._curThread = []
            self._stack.append(self._curThread)

            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.cmd()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invalidcmdleitura(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdleituraContext,0)


        def cmdleitura(self):
            return self.getTypedRuleContext(IsiLangParser.CmdleituraContext,0)


        def cmdescrita(self):
            return self.getTypedRuleContext(IsiLangParser.CmdescritaContext,0)


        def invalidcmd(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdContext,0)


        def invalidcmdselecao(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdselecaoContext,0)


        def invalidcmdenquanto(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdenquantoContext,0)


        def cmdattrib(self):
            return self.getTypedRuleContext(IsiLangParser.CmdattribContext,0)


        def cmdselecao(self):
            return self.getTypedRuleContext(IsiLangParser.CmdselecaoContext,0)


        def cmdenquanto(self):
            return self.getTypedRuleContext(IsiLangParser.CmdenquantoContext,0)


        def invalidelse(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidelseContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = IsiLangParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmd)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.invalidcmdleitura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.cmdleitura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.cmdescrita()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.invalidcmd()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.invalidcmdselecao()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.invalidcmdenquanto()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.cmdattrib()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.cmdselecao()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
                self.cmdenquanto()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 94
                self.invalidelse()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdleituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdleitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdleitura" ):
                listener.enterCmdleitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdleitura" ):
                listener.exitCmdleitura(self)




    def cmdleitura(self):

        localctx = IsiLangParser.CmdleituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdleitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(IsiLangParser.T__5)
            self.state = 98
            self.match(IsiLangParser.AP)
            self.state = 99
            self.match(IsiLangParser.ID)

            self.checkVar(self._ctx.getChild(-1).getText())
            self._readIDCommand = str(self._ctx.getChild(-1))

            self.state = 101
            self.match(IsiLangParser.FP)
            self.state = 102
            self.match(IsiLangParser.SC)

            cmd = ReadCommand(self._readIDCommand, self._isiProgram._varTable.get(self._readIDCommand))
            self._stack[-1].append(cmd)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdescritaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLangParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdescrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdescrita" ):
                listener.enterCmdescrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdescrita" ):
                listener.exitCmdescrita(self)




    def cmdescrita(self):

        localctx = IsiLangParser.CmdescritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdescrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(IsiLangParser.T__6)
            self._exprType = "any"
            self.state = 107
            self.match(IsiLangParser.AP)
            self.state = 108
            self.termo()

            varName = self._ctx.getChild(-1).getText()
            self._readIDCommand = str(varName)

            self.state = 110
            self.match(IsiLangParser.FP)
            self.state = 111
            self.match(IsiLangParser.SC)

            variavel = self._isiProgram._varTable.get(self._readIDCommand)
            if(variavel != None):
                 tipo = variavel.getType()
            else:
                 tipo = IsiVariable.TEXT
            cmd = WriteCommand(self._readIDCommand, tipo)
            self._stack[-1].append(cmd)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ID)
            else:
                return self.getToken(IsiLangParser.ID, i)

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLangParser.ExprContext,0)


        def termo(self):
            return self.getTypedRuleContext(IsiLangParser.TermoContext,0)


        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmd" ):
                listener.enterInvalidcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmd" ):
                listener.exitInvalidcmd(self)




    def invalidcmd(self):

        localctx = IsiLangParser.InvalidcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_invalidcmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(IsiLangParser.ID)

            raise IsiSemanticException("Erro Semantico! Comando {} nao reconhecido ou mal utilizado!".format(self._ctx.getChild(-1).getText()))   

            self.state = 116
            self.match(IsiLangParser.AP)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 117
                self.match(IsiLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 118
                self.match(IsiLangParser.NUMBER)
                pass

            elif la_ == 3:
                self.state = 119
                self.expr()
                pass

            elif la_ == 4:
                self.state = 120
                self.termo()
                pass

            elif la_ == 5:
                self.state = 121
                self.match(IsiLangParser.TEXT)
                pass


            self.state = 124
            self.match(IsiLangParser.FP)
            self.state = 125
            self.match(IsiLangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdleituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdleitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdleitura" ):
                listener.enterInvalidcmdleitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdleitura" ):
                listener.exitInvalidcmdleitura(self)




    def invalidcmdleitura(self):

        localctx = IsiLangParser.InvalidcmdleituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_invalidcmdleitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(IsiLangParser.T__5)
            self.state = 128
            self.match(IsiLangParser.AP)
            self.state = 129
            self.match(IsiLangParser.FP)
            raise IsiSemanticException("Erro Semantico! Comando de leitura sem uma variavel para armazenar a entrada do terminal !!")
            self.state = 131
            self.match(IsiLangParser.SC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdselecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invalidcmdselecaocond(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdselecaocondContext,0)


        def invalidcmdselecaocmdv(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdselecaocmdvContext,0)


        def invalidcmdselecaocmdf(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdselecaocmdfContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdselecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdselecao" ):
                listener.enterInvalidcmdselecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdselecao" ):
                listener.exitInvalidcmdselecao(self)




    def invalidcmdselecao(self):

        localctx = IsiLangParser.InvalidcmdselecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_invalidcmdselecao)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.invalidcmdselecaocond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.invalidcmdselecaocmdv()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.invalidcmdselecaocmdf()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdselecaocmdvContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLangParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ACH)
            else:
                return self.getToken(IsiLangParser.ACH, i)

        def FCH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.FCH)
            else:
                return self.getToken(IsiLangParser.FCH, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdselecaocmdv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdselecaocmdv" ):
                listener.enterInvalidcmdselecaocmdv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdselecaocmdv" ):
                listener.exitInvalidcmdselecaocmdv(self)




    def invalidcmdselecaocmdv(self):

        localctx = IsiLangParser.InvalidcmdselecaocmdvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_invalidcmdselecaocmdv)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(IsiLangParser.T__7)
            self.state = 139
            self.match(IsiLangParser.AP)
            self.state = 140
            self.match(IsiLangParser.ID)
            self.state = 141
            self.match(IsiLangParser.OPREL)
            self.state = 142
            self.termo()
            self.state = 143
            self.match(IsiLangParser.FP)
            self.state = 144
            self.match(IsiLangParser.ACH)
            self.state = 145
            self.match(IsiLangParser.FCH)
            raise IsiSemanticException("Erro Semantico! Comando de selecao sem comando para condicao == Verdadeiro !!")

            self.state = 147
            self.match(IsiLangParser.T__8)
            self.state = 148
            self.match(IsiLangParser.ACH)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.cmd()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 154
            self.match(IsiLangParser.FCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdselecaocmdfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLangParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ACH)
            else:
                return self.getToken(IsiLangParser.ACH, i)

        def FCH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.FCH)
            else:
                return self.getToken(IsiLangParser.FCH, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdselecaocmdf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdselecaocmdf" ):
                listener.enterInvalidcmdselecaocmdf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdselecaocmdf" ):
                listener.exitInvalidcmdselecaocmdf(self)




    def invalidcmdselecaocmdf(self):

        localctx = IsiLangParser.InvalidcmdselecaocmdfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_invalidcmdselecaocmdf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(IsiLangParser.T__7)
            self.state = 157
            self.match(IsiLangParser.AP)
            self.state = 158
            self.match(IsiLangParser.ID)
            self.state = 159
            self.match(IsiLangParser.OPREL)
            self.state = 160
            self.termo()
            self.state = 161
            self.match(IsiLangParser.FP)
            self.state = 162
            self.match(IsiLangParser.ACH)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 163
                self.cmd()
                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 168
            self.match(IsiLangParser.FCH)
            self.state = 169
            self.match(IsiLangParser.T__8)
            self.state = 170
            self.match(IsiLangParser.ACH)
            self.state = 171
            self.match(IsiLangParser.FCH)
            raise IsiSemanticException("Erro Semantico! Comando de selecao, com uso de SENAO, sem comando para condicao == Falso !!")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdselecaocondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ACH)
            else:
                return self.getToken(IsiLangParser.ACH, i)

        def FCH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.FCH)
            else:
                return self.getToken(IsiLangParser.FCH, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(IsiLangParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdselecaocond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdselecaocond" ):
                listener.enterInvalidcmdselecaocond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdselecaocond" ):
                listener.exitInvalidcmdselecaocond(self)




    def invalidcmdselecaocond(self):

        localctx = IsiLangParser.InvalidcmdselecaocondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_invalidcmdselecaocond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(IsiLangParser.T__7)
            self.state = 175
            self.match(IsiLangParser.AP)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.BOOL) | (1 << IsiLangParser.ID) | (1 << IsiLangParser.NUMBER) | (1 << IsiLangParser.TEXT))) != 0):
                self.state = 176
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.BOOL) | (1 << IsiLangParser.ID) | (1 << IsiLangParser.NUMBER) | (1 << IsiLangParser.TEXT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 179
            self.match(IsiLangParser.FP)
            raise IsiSemanticException("Erro Semantico! Comando de selecao sem condicao de verificacao, ou condicao mal formulada!!")
            self.state = 181
            self.match(IsiLangParser.ACH)
            self.state = 183 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 182
                self.cmd()
                self.state = 185 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 187
            self.match(IsiLangParser.FCH)

            self.state = 188
            self.match(IsiLangParser.T__8)
            self.state = 189
            self.match(IsiLangParser.ACH)
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self.cmd()
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 195
            self.match(IsiLangParser.FCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdenquantoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def invalidcmdenquantocond(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdenquantocondContext,0)


        def invalidcmdenquantocmd(self):
            return self.getTypedRuleContext(IsiLangParser.InvalidcmdenquantocmdContext,0)


        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdenquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdenquanto" ):
                listener.enterInvalidcmdenquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdenquanto" ):
                listener.exitInvalidcmdenquanto(self)




    def invalidcmdenquanto(self):

        localctx = IsiLangParser.InvalidcmdenquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_invalidcmdenquanto)
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.invalidcmdenquantocond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.invalidcmdenquantocmd()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdenquantocondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self):
            return self.getToken(IsiLangParser.ACH, 0)

        def FCH(self):
            return self.getToken(IsiLangParser.FCH, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(IsiLangParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdenquantocond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdenquantocond" ):
                listener.enterInvalidcmdenquantocond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdenquantocond" ):
                listener.exitInvalidcmdenquantocond(self)




    def invalidcmdenquantocond(self):

        localctx = IsiLangParser.InvalidcmdenquantocondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_invalidcmdenquantocond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(IsiLangParser.T__9)
            self.state = 202
            self.match(IsiLangParser.AP)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.BOOL) | (1 << IsiLangParser.ID) | (1 << IsiLangParser.NUMBER) | (1 << IsiLangParser.TEXT))) != 0):
                self.state = 203
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.BOOL) | (1 << IsiLangParser.ID) | (1 << IsiLangParser.NUMBER) | (1 << IsiLangParser.TEXT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 206
            self.match(IsiLangParser.FP)
            raise IsiSemanticException("Erro Semantico! Comando Enquanto sem condicao de verificacao, ou condicao mal formulada!!")
            self.state = 208
            self.match(IsiLangParser.ACH)
            self.state = 210 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 209
                self.cmd()
                self.state = 212 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 214
            self.match(IsiLangParser.FCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidcmdenquantocmdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def termo(self):
            return self.getTypedRuleContext(IsiLangParser.TermoContext,0)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self):
            return self.getToken(IsiLangParser.ACH, 0)

        def FCH(self):
            return self.getToken(IsiLangParser.FCH, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidcmdenquantocmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidcmdenquantocmd" ):
                listener.enterInvalidcmdenquantocmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidcmdenquantocmd" ):
                listener.exitInvalidcmdenquantocmd(self)




    def invalidcmdenquantocmd(self):

        localctx = IsiLangParser.InvalidcmdenquantocmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_invalidcmdenquantocmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(IsiLangParser.T__9)
            self.state = 217
            self.match(IsiLangParser.AP)
            self.state = 218
            self.match(IsiLangParser.ID)
            self.state = 219
            self.match(IsiLangParser.OPREL)
            self.state = 220
            self.termo()
            self.state = 221
            self.match(IsiLangParser.FP)
            self.state = 222
            self.match(IsiLangParser.ACH)
            self.state = 223
            self.match(IsiLangParser.FCH)
            raise IsiSemanticException("Erro Semantico! Comando Enquanto sem utilizacao de comandos internos, looping sem nenhuma utilidade!!")
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdattribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def ATTR(self):
            return self.getToken(IsiLangParser.ATTR, 0)

        def expr(self):
            return self.getTypedRuleContext(IsiLangParser.ExprContext,0)


        def SC(self):
            return self.getToken(IsiLangParser.SC, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdattrib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdattrib" ):
                listener.enterCmdattrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdattrib" ):
                listener.exitCmdattrib(self)




    def cmdattrib(self):

        localctx = IsiLangParser.CmdattribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cmdattrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(IsiLangParser.ID)

            varName = self._ctx.getChild(-1).getText()
            self.checkVar(varName)
            self._exprID = varName
            self._exprType = self._isiProgram._varTable.get(varName).getTypeStr()

            self.state = 228
            self.match(IsiLangParser.ATTR)

            self._exprContent = ""
                           
            self.state = 230
            self.expr()
            self.state = 231
            self.match(IsiLangParser.SC)

            cmd = AttribCommand(self._exprID, self._exprContent)
            self._stack[-1].append(cmd)
                           
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdselecaoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.TermoContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.TermoContext,i)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.ACH)
            else:
                return self.getToken(IsiLangParser.ACH, i)

        def FCH(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.FCH)
            else:
                return self.getToken(IsiLangParser.FCH, i)

        def OPLOG(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OPLOG)
            else:
                return self.getToken(IsiLangParser.OPLOG, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdselecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdselecao" ):
                listener.enterCmdselecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdselecao" ):
                listener.exitCmdselecao(self)




    def cmdselecao(self):

        localctx = IsiLangParser.CmdselecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cmdselecao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(IsiLangParser.T__7)
            self.state = 235
            self.match(IsiLangParser.AP)
            self.state = 236
            self.match(IsiLangParser.ID)

            varName = self._ctx.getChild(-1).getText()
            self.checkVar(varName)
            self._exprDecision = varName
            self._exprType = self._isiProgram._varTable.get(varName).getTypeStr()

            self.state = 238
            self.match(IsiLangParser.OPREL)

            self._exprDecision += self._ctx.getChild(-1).getText()

            self.state = 240
            self.termo()

            self._exprDecision += self._ctx.getChild(-1).getText()

            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.OPLOG:
                self.state = 242
                self.match(IsiLangParser.OPLOG)

                self._exprDecision += self._ctx.getChild(-1).getText()

                self.state = 244
                self.termo()

                self._exprDecision += self._ctx.getChild(-1).getText()

                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 252
            self.match(IsiLangParser.FP)
            self.state = 253
            self.match(IsiLangParser.ACH)

            self._exprDecisionStack.append(self._exprDecision)
            self._elseCheck = False
            self._elseCheckStack.append(False)
            self._curThread = []
            self._stack.append(self._curThread)

            self.state = 256 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 255
                self.cmd()
                self.state = 258 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 260
            self.match(IsiLangParser.FCH)

            self._trueList = self._stack.pop()

            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 262
                self.match(IsiLangParser.T__8)
                self.state = 263
                self.match(IsiLangParser.ACH)

                self._elseCheck = True
                self._elseCheckStack[-1] = True
                self._curThread = []
                self._stack.append(self._curThread)


                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 265
                    self.cmd()
                    self.state = 268 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                        break

                self.state = 270
                self.match(IsiLangParser.FCH)

                self._falseList = self._stack.pop()
                cmd = DecisionCommand(self._exprDecisionStack.pop(), self._trueList, self._falseList)
                self._stack[-1].append(cmd)




            if(self._elseCheckStack.pop() == False):
                cmd = DecisionCommand(self._exprDecisionStack.pop(), self._trueList, [])
                self._stack[-1].append(cmd)
            else:
                self._elseCheck = False

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdenquantoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AP(self):
            return self.getToken(IsiLangParser.AP, 0)

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def OPREL(self):
            return self.getToken(IsiLangParser.OPREL, 0)

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.TermoContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.TermoContext,i)


        def FP(self):
            return self.getToken(IsiLangParser.FP, 0)

        def ACH(self):
            return self.getToken(IsiLangParser.ACH, 0)

        def FCH(self):
            return self.getToken(IsiLangParser.FCH, 0)

        def OPLOG(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OPLOG)
            else:
                return self.getToken(IsiLangParser.OPLOG, i)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.CmdContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.CmdContext,i)


        def getRuleIndex(self):
            return IsiLangParser.RULE_cmdenquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdenquanto" ):
                listener.enterCmdenquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdenquanto" ):
                listener.exitCmdenquanto(self)




    def cmdenquanto(self):

        localctx = IsiLangParser.CmdenquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cmdenquanto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(IsiLangParser.T__9)
            self.state = 278
            self.match(IsiLangParser.AP)
            self.state = 279
            self.match(IsiLangParser.ID)

            varName = self._ctx.getChild(-1).getText()
            self.checkVar(varName)
            self._exprDecision = varName
            self._exprType = self._isiProgram._varTable.get(varName).getTypeStr()

            self.state = 281
            self.match(IsiLangParser.OPREL)

            self._exprDecision += self._ctx.getChild(-1).getText()

            self.state = 283
            self.termo()

            self._exprDecision += self._ctx.getChild(-1).getText()

            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.OPLOG:
                self.state = 285
                self.match(IsiLangParser.OPLOG)

                self._exprDecision += self._ctx.getChild(-1).getText()

                self.state = 287
                self.termo()

                self._exprDecision += self._ctx.getChild(-1).getText()

                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(IsiLangParser.FP)
            self.state = 296
            self.match(IsiLangParser.ACH)

            self._exprDecisionStack.append(self._exprDecision)
            self._curThread = []
            self._stack.append(self._curThread)

            self.state = 299 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 298
                self.cmd()
                self.state = 301 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IsiLangParser.T__5) | (1 << IsiLangParser.T__6) | (1 << IsiLangParser.T__7) | (1 << IsiLangParser.T__8) | (1 << IsiLangParser.T__9) | (1 << IsiLangParser.ID))) != 0)):
                    break

            self.state = 303
            self.match(IsiLangParser.FCH)

            self._cmdList = self._stack.pop()
            cmd = WhileCommand(self._exprDecisionStack.pop(), self._cmdList)
            self._stack[-1].append(cmd)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IsiLangParser.TermoContext)
            else:
                return self.getTypedRuleContext(IsiLangParser.TermoContext,i)


        def OP(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OP)
            else:
                return self.getToken(IsiLangParser.OP, i)

        def OPLOG(self, i:int=None):
            if i is None:
                return self.getTokens(IsiLangParser.OPLOG)
            else:
                return self.getToken(IsiLangParser.OPLOG, i)

        def getRuleIndex(self):
            return IsiLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = IsiLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.termo()
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IsiLangParser.OP or _la==IsiLangParser.OPLOG:
                self.state = 313
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IsiLangParser.OP]:
                    self.state = 307
                    self.match(IsiLangParser.OP)

                    self._exprContent += self._ctx.getChild(-1).getText() 
                                      
                    self.state = 309
                    self.termo()
                    pass
                elif token in [IsiLangParser.OPLOG]:
                    self.state = 310
                    self.match(IsiLangParser.OPLOG)

                    self._exprContent += self._ctx.getChild(-1).getText() 
                                      
                    self.state = 312
                    self.termo()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 317
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IsiLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(IsiLangParser.NUMBER, 0)

        def TEXT(self):
            return self.getToken(IsiLangParser.TEXT, 0)

        def BOOL(self):
            return self.getToken(IsiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return IsiLangParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = IsiLangParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_termo)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IsiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(IsiLangParser.ID)

                varName = self._ctx.getChild(-1).getText()
                self.checkVar(varName)
                self._exprContent += varName
                self.checkVarType(self._isiProgram._varTable.get(varName))

                pass
            elif token in [IsiLangParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(IsiLangParser.NUMBER)

                varName = self._ctx.getChild(-1).getText()
                self._exprContent += varName
                self.checkVarType(IsiVariable(f"Número {varName}", IsiVariable.NUMBER, varName, False))
                              
                pass
            elif token in [IsiLangParser.TEXT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(IsiLangParser.TEXT)

                varName = self._ctx.getChild(-1).getText()
                self._exprContent += varName
                self.checkVarType(IsiVariable(f"Texto {varName}", IsiVariable.TEXT, varName, False))
                            
                pass
            elif token in [IsiLangParser.BOOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.match(IsiLangParser.BOOL)

                varName = self._ctx.getChild(-1).getText()
                self._exprContent += varName
                self.checkVarType(IsiVariable(f"Bool {varName}", IsiVariable.BOOL, varName, False))               

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvalidelseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IsiLangParser.RULE_invalidelse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInvalidelse" ):
                listener.enterInvalidelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInvalidelse" ):
                listener.exitInvalidelse(self)




    def invalidelse(self):

        localctx = IsiLangParser.InvalidelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_invalidelse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(IsiLangParser.T__8)

            raise IsiSemanticException("Erro Semantico! Palavra reservada SENAO utilizada erroneamente antes do SE!") 

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





