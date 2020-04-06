# Generated from js_grammar.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3j")
        buf.write("\u0283\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\5\2t\n")
        buf.write("\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u0090\n\4\3\5\3\5\5\5\u0094\n\5\3\5\3\5\3\6\6\6\u0099")
        buf.write("\n\6\r\6\16\6\u009a\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b\u00a4")
        buf.write("\n\b\f\b\16\b\u00a7\13\b\3\t\3\t\5\t\u00ab\n\t\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00bc\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00cf")
        buf.write("\n\16\3\16\3\16\5\16\u00d3\n\16\3\16\3\16\5\16\u00d7\n")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00e1")
        buf.write("\n\16\3\16\3\16\5\16\u00e5\n\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\5\16\u00fb\n\16\3\17\3\17\3")
        buf.write("\20\3\20\3\20\5\20\u0102\n\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\5\21\u0109\n\21\3\21\3\21\3\22\3\22\3\22\5\22\u0110\n")
        buf.write("\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\5\25\u0122\n\25\3\25\3")
        buf.write("\25\5\25\u0126\n\25\5\25\u0128\n\25\3\25\3\25\3\26\6\26")
        buf.write("\u012d\n\26\r\26\16\26\u012e\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u0135\n\27\3\30\3\30\3\30\5\30\u013a\n\30\3\31\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0152")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\5\37\u0164\n\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \7 \u016e\n \f \16 \u0171\13")
        buf.write(" \3!\5!\u0174\n!\3\"\6\"\u0177\n\"\r\"\16\"\u0178\3#\3")
        buf.write("#\5#\u017d\n#\3#\5#\u0180\n#\3#\5#\u0183\n#\3#\3#\3$\5")
        buf.write("$\u0188\n$\3$\3$\3$\5$\u018d\n$\3$\7$\u0190\n$\f$\16$")
        buf.write("\u0193\13$\3%\6%\u0196\n%\r%\16%\u0197\3&\3&\3&\3&\3&")
        buf.write("\5&\u019f\n&\3&\3&\5&\u01a3\n&\3\'\3\'\3\'\7\'\u01a8\n")
        buf.write("\'\f\'\16\'\u01ab\13\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01c0\n(\3)\3)\3)\5)\u01c5")
        buf.write("\n)\3*\3*\3+\3+\3+\3+\7+\u01cd\n+\f+\16+\u01d0\13+\3+")
        buf.write("\5+\u01d3\n+\5+\u01d5\n+\3+\3+\3,\5,\u01da\n,\3,\3,\5")
        buf.write(",\u01de\n,\3-\3-\3-\7-\u01e3\n-\f-\16-\u01e6\13-\3.\3")
        buf.write(".\3.\5.\u01eb\n.\3.\3.\5.\u01ef\n.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01f9\n.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0216\n")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u0259\n.\f.\16.")
        buf.write("\u025c\13.\3/\3/\3\60\3\60\5\60\u0262\n\60\3\61\3\61\3")
        buf.write("\62\3\62\5\62\u0268\n\62\3\63\3\63\3\63\5\63\u026d\n\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\38\58\u027f\n8\39\39\39\2\3Z:\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\16\4\2@AXX\3\2\27\31\3\2")
        buf.write("\23\24\3\2\32\34\3\2\35 \3\2!$\3\2*\64\5\2\3\3\65\66d")
        buf.write("d\4\2\678jj\3\2\65\66\3\29S\3\2Tb\2\u02b8\2s\3\2\2\2\4")
        buf.write("w\3\2\2\2\6\u008f\3\2\2\2\b\u0091\3\2\2\2\n\u0098\3\2")
        buf.write("\2\2\f\u009c\3\2\2\2\16\u009f\3\2\2\2\20\u00a8\3\2\2\2")
        buf.write("\22\u00ac\3\2\2\2\24\u00af\3\2\2\2\26\u00b1\3\2\2\2\30")
        buf.write("\u00b4\3\2\2\2\32\u00fa\3\2\2\2\34\u00fc\3\2\2\2\36\u00fe")
        buf.write("\3\2\2\2 \u0105\3\2\2\2\"\u010c\3\2\2\2$\u0113\3\2\2\2")
        buf.write("&\u0119\3\2\2\2(\u011f\3\2\2\2*\u012c\3\2\2\2,\u0130\3")
        buf.write("\2\2\2.\u0136\3\2\2\2\60\u013b\3\2\2\2\62\u013f\3\2\2")
        buf.write("\2\64\u0151\3\2\2\2\66\u0153\3\2\2\28\u0159\3\2\2\2:\u015c")
        buf.write("\3\2\2\2<\u015f\3\2\2\2>\u016a\3\2\2\2@\u0173\3\2\2\2")
        buf.write("B\u0176\3\2\2\2D\u017a\3\2\2\2F\u0187\3\2\2\2H\u0195\3")
        buf.write("\2\2\2J\u01a2\3\2\2\2L\u01a4\3\2\2\2N\u01bf\3\2\2\2P\u01c4")
        buf.write("\3\2\2\2R\u01c6\3\2\2\2T\u01c8\3\2\2\2V\u01d9\3\2\2\2")
        buf.write("X\u01df\3\2\2\2Z\u0215\3\2\2\2\\\u025d\3\2\2\2^\u0261")
        buf.write("\3\2\2\2`\u0263\3\2\2\2b\u0267\3\2\2\2d\u026c\3\2\2\2")
        buf.write("f\u026e\3\2\2\2h\u0270\3\2\2\2j\u0272\3\2\2\2l\u0276\3")
        buf.write("\2\2\2n\u027e\3\2\2\2p\u0280\3\2\2\2rt\5B\"\2sr\3\2\2")
        buf.write("\2st\3\2\2\2tu\3\2\2\2uv\7\2\2\3v\3\3\2\2\2wx\5\6\4\2")
        buf.write("x\5\3\2\2\2y\u0090\5\b\5\2z\u0090\5\f\7\2{\u0090\5\24")
        buf.write("\13\2|\u0090\5\30\r\2}\u0090\5\32\16\2~\u0090\5\36\20")
        buf.write("\2\177\u0090\5 \21\2\u0080\u0090\5\"\22\2\u0081\u0090")
        buf.write("\5$\23\2\u0082\u0090\5\60\31\2\u0083\u0084\5&\24\2\u0084")
        buf.write("\u0085\b\4\1\2\u0085\u0090\3\2\2\2\u0086\u0087\5\62\32")
        buf.write("\2\u0087\u0088\b\4\1\2\u0088\u0090\3\2\2\2\u0089\u008a")
        buf.write("\5\64\33\2\u008a\u008b\b\4\1\2\u008b\u0090\3\2\2\2\u008c")
        buf.write("\u008d\5:\36\2\u008d\u008e\b\4\1\2\u008e\u0090\3\2\2\2")
        buf.write("\u008fy\3\2\2\2\u008fz\3\2\2\2\u008f{\3\2\2\2\u008f|\3")
        buf.write("\2\2\2\u008f}\3\2\2\2\u008f~\3\2\2\2\u008f\177\3\2\2\2")
        buf.write("\u008f\u0080\3\2\2\2\u008f\u0081\3\2\2\2\u008f\u0082\3")
        buf.write("\2\2\2\u008f\u0083\3\2\2\2\u008f\u0086\3\2\2\2\u008f\u0089")
        buf.write("\3\2\2\2\u008f\u008c\3\2\2\2\u0090\7\3\2\2\2\u0091\u0093")
        buf.write("\7\t\2\2\u0092\u0094\5\n\6\2\u0093\u0092\3\2\2\2\u0093")
        buf.write("\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\7\n\2\2")
        buf.write("\u0096\t\3\2\2\2\u0097\u0099\5\6\4\2\u0098\u0097\3\2\2")
        buf.write("\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\13\3\2\2\2\u009c\u009d\5\16\b\2\u009d\u009e")
        buf.write("\5n8\2\u009e\r\3\2\2\2\u009f\u00a0\5\34\17\2\u00a0\u00a5")
        buf.write("\5\20\t\2\u00a1\u00a2\7\f\2\2\u00a2\u00a4\5\20\t\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2")
        buf.write("\u00a5\u00a6\3\2\2\2\u00a6\17\3\2\2\2\u00a7\u00a5\3\2")
        buf.write("\2\2\u00a8\u00aa\7c\2\2\u00a9\u00ab\5\22\n\2\u00aa\u00a9")
        buf.write("\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\21\3\2\2\2\u00ac\u00ad")
        buf.write("\7\r\2\2\u00ad\u00ae\5Z.\2\u00ae\23\3\2\2\2\u00af\u00b0")
        buf.write("\7\13\2\2\u00b0\25\3\2\2\2\u00b1\u00b2\5X-\2\u00b2\u00b3")
        buf.write("\5n8\2\u00b3\27\3\2\2\2\u00b4\u00b5\7O\2\2\u00b5\u00b6")
        buf.write("\7\7\2\2\u00b6\u00b7\5X-\2\u00b7\u00b8\7\b\2\2\u00b8\u00bb")
        buf.write("\5\6\4\2\u00b9\u00ba\7>\2\2\u00ba\u00bc\5\6\4\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\31\3\2\2\2\u00bd")
        buf.write("\u00be\7:\2\2\u00be\u00bf\5\6\4\2\u00bf\u00c0\7I\2\2\u00c0")
        buf.write("\u00c1\7\7\2\2\u00c1\u00c2\5X-\2\u00c2\u00c3\7\b\2\2\u00c3")
        buf.write("\u00c4\5n8\2\u00c4\u00fb\3\2\2\2\u00c5\u00c6\7I\2\2\u00c6")
        buf.write("\u00c7\7\7\2\2\u00c7\u00c8\5X-\2\u00c8\u00c9\7\b\2\2\u00c9")
        buf.write("\u00ca\5\6\4\2\u00ca\u00fb\3\2\2\2\u00cb\u00cc\7G\2\2")
        buf.write("\u00cc\u00ce\7\7\2\2\u00cd\u00cf\5X-\2\u00ce\u00cd\3\2")
        buf.write("\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d2")
        buf.write("\7\13\2\2\u00d1\u00d3\5X-\2\u00d2\u00d1\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\7\13\2")
        buf.write("\2\u00d5\u00d7\5X-\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\7\b\2\2\u00d9\u00fb")
        buf.write("\5\6\4\2\u00da\u00db\7G\2\2\u00db\u00dc\7\7\2\2\u00dc")
        buf.write("\u00dd\7@\2\2\u00dd\u00de\5\16\b\2\u00de\u00e0\7\13\2")
        buf.write("\2\u00df\u00e1\5X-\2\u00e0\u00df\3\2\2\2\u00e0\u00e1\3")
        buf.write("\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e4\7\13\2\2\u00e3")
        buf.write("\u00e5\5X-\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\u00e7\7\b\2\2\u00e7\u00e8\5\6\4\2")
        buf.write("\u00e8\u00fb\3\2\2\2\u00e9\u00ea\7G\2\2\u00ea\u00eb\7")
        buf.write("\7\2\2\u00eb\u00ec\5Z.\2\u00ec\u00ed\7R\2\2\u00ed\u00ee")
        buf.write("\5X-\2\u00ee\u00ef\7\b\2\2\u00ef\u00f0\5\6\4\2\u00f0\u00fb")
        buf.write("\3\2\2\2\u00f1\u00f2\7G\2\2\u00f2\u00f3\7\7\2\2\u00f3")
        buf.write("\u00f4\7@\2\2\u00f4\u00f5\5\20\t\2\u00f5\u00f6\7R\2\2")
        buf.write("\u00f6\u00f7\5X-\2\u00f7\u00f8\7\b\2\2\u00f8\u00f9\5\6")
        buf.write("\4\2\u00f9\u00fb\3\2\2\2\u00fa\u00bd\3\2\2\2\u00fa\u00c5")
        buf.write("\3\2\2\2\u00fa\u00cb\3\2\2\2\u00fa\u00da\3\2\2\2\u00fa")
        buf.write("\u00e9\3\2\2\2\u00fa\u00f1\3\2\2\2\u00fb\33\3\2\2\2\u00fc")
        buf.write("\u00fd\t\2\2\2\u00fd\35\3\2\2\2\u00fe\u0101\7F\2\2\u00ff")
        buf.write("\u0100\6\20\2\2\u0100\u0102\7c\2\2\u0101\u00ff\3\2\2\2")
        buf.write("\u0101\u0102\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\5")
        buf.write("n8\2\u0104\37\3\2\2\2\u0105\u0108\79\2\2\u0106\u0107\6")
        buf.write("\21\3\2\u0107\u0109\7c\2\2\u0108\u0106\3\2\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\5n8\2\u010b!")
        buf.write("\3\2\2\2\u010c\u010f\7D\2\2\u010d\u010e\6\22\4\2\u010e")
        buf.write("\u0110\5X-\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\5n8\2\u0112#\3\2\2\2\u0113")
        buf.write("\u0114\7M\2\2\u0114\u0115\7\7\2\2\u0115\u0116\5X-\2\u0116")
        buf.write("\u0117\7\b\2\2\u0117\u0118\5\6\4\2\u0118%\3\2\2\2\u0119")
        buf.write("\u011a\7H\2\2\u011a\u011b\7\7\2\2\u011b\u011c\5X-\2\u011c")
        buf.write("\u011d\7\b\2\2\u011d\u011e\5(\25\2\u011e\'\3\2\2\2\u011f")
        buf.write("\u0121\7\t\2\2\u0120\u0122\5*\26\2\u0121\u0120\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0127\3\2\2\2\u0123\u0125\5")
        buf.write(".\30\2\u0124\u0126\5*\26\2\u0125\u0124\3\2\2\2\u0125\u0126")
        buf.write("\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0123\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7\n\2\2")
        buf.write("\u012a)\3\2\2\2\u012b\u012d\5,\27\2\u012c\u012b\3\2\2")
        buf.write("\2\u012d\u012e\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f+\3\2\2\2\u0130\u0131\7=\2\2\u0131\u0132")
        buf.write("\5X-\2\u0132\u0134\7\17\2\2\u0133\u0135\5\n\6\2\u0134")
        buf.write("\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135-\3\2\2\2\u0136")
        buf.write("\u0137\7N\2\2\u0137\u0139\7\17\2\2\u0138\u013a\5\n\6\2")
        buf.write("\u0139\u0138\3\2\2\2\u0139\u013a\3\2\2\2\u013a/\3\2\2")
        buf.write("\2\u013b\u013c\7c\2\2\u013c\u013d\7\17\2\2\u013d\u013e")
        buf.write("\5\6\4\2\u013e\61\3\2\2\2\u013f\u0140\7P\2\2\u0140\u0141")
        buf.write("\6\32\5\2\u0141\u0142\5X-\2\u0142\u0143\5n8\2\u0143\63")
        buf.write("\3\2\2\2\u0144\u0145\7S\2\2\u0145\u0146\5\b\5\2\u0146")
        buf.write("\u0147\5\66\34\2\u0147\u0152\3\2\2\2\u0148\u0149\7S\2")
        buf.write("\2\u0149\u014a\5\b\5\2\u014a\u014b\58\35\2\u014b\u0152")
        buf.write("\3\2\2\2\u014c\u014d\7S\2\2\u014d\u014e\5\b\5\2\u014e")
        buf.write("\u014f\5\66\34\2\u014f\u0150\58\35\2\u0150\u0152\3\2\2")
        buf.write("\2\u0151\u0144\3\2\2\2\u0151\u0148\3\2\2\2\u0151\u014c")
        buf.write("\3\2\2\2\u0152\65\3\2\2\2\u0153\u0154\7B\2\2\u0154\u0155")
        buf.write("\7\7\2\2\u0155\u0156\7c\2\2\u0156\u0157\7\b\2\2\u0157")
        buf.write("\u0158\5\b\5\2\u0158\67\3\2\2\2\u0159\u015a\7C\2\2\u015a")
        buf.write("\u015b\5\b\5\2\u015b9\3\2\2\2\u015c\u015d\7J\2\2\u015d")
        buf.write("\u015e\5n8\2\u015e;\3\2\2\2\u015f\u0160\7K\2\2\u0160\u0161")
        buf.write("\7c\2\2\u0161\u0163\7\7\2\2\u0162\u0164\5> \2\u0163\u0162")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165")
        buf.write("\u0166\7\b\2\2\u0166\u0167\7\t\2\2\u0167\u0168\5@!\2\u0168")
        buf.write("\u0169\7\n\2\2\u0169=\3\2\2\2\u016a\u016f\7c\2\2\u016b")
        buf.write("\u016c\7\f\2\2\u016c\u016e\7c\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016e\u0171\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170?\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0174")
        buf.write("\5B\"\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("A\3\2\2\2\u0175\u0177\5\4\3\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179C\3\2\2\2\u017a\u017c\7\5\2\2\u017b\u017d\5F$\2")
        buf.write("\u017c\u017b\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3")
        buf.write("\2\2\2\u017e\u0180\7\f\2\2\u017f\u017e\3\2\2\2\u017f\u0180")
        buf.write("\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5H%\2\u0182\u0181")
        buf.write("\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0184\3\2\2\2\u0184")
        buf.write("\u0185\7\6\2\2\u0185E\3\2\2\2\u0186\u0188\5H%\2\u0187")
        buf.write("\u0186\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2")
        buf.write("\u0189\u0191\5Z.\2\u018a\u018c\7\f\2\2\u018b\u018d\5H")
        buf.write("%\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u0190\5Z.\2\u018f\u018a\3\2\2\2\u0190\u0193")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("G\3\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\7\f\2\2\u0195")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2")
        buf.write("\u0197\u0198\3\2\2\2\u0198I\3\2\2\2\u0199\u019a\7\t\2")
        buf.write("\2\u019a\u01a3\7\n\2\2\u019b\u019c\7\t\2\2\u019c\u019e")
        buf.write("\5L\'\2\u019d\u019f\7\f\2\2\u019e\u019d\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\7\n\2\2")
        buf.write("\u01a1\u01a3\3\2\2\2\u01a2\u0199\3\2\2\2\u01a2\u019b\3")
        buf.write("\2\2\2\u01a3K\3\2\2\2\u01a4\u01a9\5N(\2\u01a5\u01a6\7")
        buf.write("\f\2\2\u01a6\u01a8\5N(\2\u01a7\u01a5\3\2\2\2\u01a8\u01ab")
        buf.write("\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa")
        buf.write("M\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\5P)\2\u01ad")
        buf.write("\u01ae\7\17\2\2\u01ae\u01af\5Z.\2\u01af\u01c0\3\2\2\2")
        buf.write("\u01b0\u01b1\5j\66\2\u01b1\u01b2\7\7\2\2\u01b2\u01b3\7")
        buf.write("\b\2\2\u01b3\u01b4\7\t\2\2\u01b4\u01b5\5@!\2\u01b5\u01b6")
        buf.write("\7\n\2\2\u01b6\u01c0\3\2\2\2\u01b7\u01b8\5l\67\2\u01b8")
        buf.write("\u01b9\7\7\2\2\u01b9\u01ba\5R*\2\u01ba\u01bb\7\b\2\2\u01bb")
        buf.write("\u01bc\7\t\2\2\u01bc\u01bd\5@!\2\u01bd\u01be\7\n\2\2\u01be")
        buf.write("\u01c0\3\2\2\2\u01bf\u01ac\3\2\2\2\u01bf\u01b0\3\2\2\2")
        buf.write("\u01bf\u01b7\3\2\2\2\u01c0O\3\2\2\2\u01c1\u01c5\5b\62")
        buf.write("\2\u01c2\u01c5\7d\2\2\u01c3\u01c5\5`\61\2\u01c4\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("Q\3\2\2\2\u01c6\u01c7\7c\2\2\u01c7S\3\2\2\2\u01c8\u01d4")
        buf.write("\7\7\2\2\u01c9\u01ce\5V,\2\u01ca\u01cb\7\f\2\2\u01cb\u01cd")
        buf.write("\5V,\2\u01cc\u01ca\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d1\u01d3\7\f\2\2\u01d2\u01d1\3\2\2\2")
        buf.write("\u01d2\u01d3\3\2\2\2\u01d3\u01d5\3\2\2\2\u01d4\u01c9\3")
        buf.write("\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\7\b\2\2\u01d7U\3\2\2\2\u01d8\u01da\7i\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dd\3\2\2\2\u01db")
        buf.write("\u01de\5Z.\2\u01dc\u01de\7c\2\2\u01dd\u01db\3\2\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01deW\3\2\2\2\u01df\u01e4\5Z.\2\u01e0")
        buf.write("\u01e1\7\f\2\2\u01e1\u01e3\5Z.\2\u01e2\u01e0\3\2\2\2\u01e3")
        buf.write("\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5Y\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8\b.\1\2")
        buf.write("\u01e8\u01ea\7K\2\2\u01e9\u01eb\7c\2\2\u01ea\u01e9\3\2")
        buf.write("\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee")
        buf.write("\7\7\2\2\u01ed\u01ef\5> \2\u01ee\u01ed\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\7\b\2\2\u01f1")
        buf.write("\u01f2\7\t\2\2\u01f2\u01f3\5@!\2\u01f3\u01f4\7\n\2\2\u01f4")
        buf.write("\u0216\3\2\2\2\u01f5\u01f6\7?\2\2\u01f6\u01f8\5Z.\2\u01f7")
        buf.write("\u01f9\5T+\2\u01f8\u01f7\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u0216\3\2\2\2\u01fa\u01fb\7Q\2\2\u01fb\u0216\5Z. \u01fc")
        buf.write("\u01fd\7E\2\2\u01fd\u0216\5Z.\37\u01fe\u01ff\7<\2\2\u01ff")
        buf.write("\u0216\5Z.\36\u0200\u0201\7\21\2\2\u0201\u0216\5Z.\35")
        buf.write("\u0202\u0203\7\22\2\2\u0203\u0216\5Z.\34\u0204\u0205\7")
        buf.write("\23\2\2\u0205\u0216\5Z.\33\u0206\u0207\7\24\2\2\u0207")
        buf.write("\u0216\5Z.\32\u0208\u0209\7\25\2\2\u0209\u0216\5Z.\31")
        buf.write("\u020a\u020b\7\26\2\2\u020b\u0216\5Z.\30\u020c\u0216\7")
        buf.write("L\2\2\u020d\u0216\7c\2\2\u020e\u0216\5^\60\2\u020f\u0216")
        buf.write("\5D#\2\u0210\u0216\5J&\2\u0211\u0212\7\7\2\2\u0212\u0213")
        buf.write("\5X-\2\u0213\u0214\7\b\2\2\u0214\u0216\3\2\2\2\u0215\u01e7")
        buf.write("\3\2\2\2\u0215\u01f5\3\2\2\2\u0215\u01fa\3\2\2\2\u0215")
        buf.write("\u01fc\3\2\2\2\u0215\u01fe\3\2\2\2\u0215\u0200\3\2\2\2")
        buf.write("\u0215\u0202\3\2\2\2\u0215\u0204\3\2\2\2\u0215\u0206\3")
        buf.write("\2\2\2\u0215\u0208\3\2\2\2\u0215\u020a\3\2\2\2\u0215\u020c")
        buf.write("\3\2\2\2\u0215\u020d\3\2\2\2\u0215\u020e\3\2\2\2\u0215")
        buf.write("\u020f\3\2\2\2\u0215\u0210\3\2\2\2\u0215\u0211\3\2\2\2")
        buf.write("\u0216\u025a\3\2\2\2\u0217\u0218\f\27\2\2\u0218\u0219")
        buf.write("\t\3\2\2\u0219\u0259\5Z.\30\u021a\u021b\f\26\2\2\u021b")
        buf.write("\u021c\t\4\2\2\u021c\u0259\5Z.\27\u021d\u021e\f\25\2\2")
        buf.write("\u021e\u021f\t\5\2\2\u021f\u0259\5Z.\26\u0220\u0221\f")
        buf.write("\24\2\2\u0221\u0222\t\6\2\2\u0222\u0259\5Z.\25\u0223\u0224")
        buf.write("\f\23\2\2\u0224\u0225\7;\2\2\u0225\u0259\5Z.\24\u0226")
        buf.write("\u0227\f\22\2\2\u0227\u0228\7R\2\2\u0228\u0259\5Z.\23")
        buf.write("\u0229\u022a\f\21\2\2\u022a\u022b\t\7\2\2\u022b\u0259")
        buf.write("\5Z.\22\u022c\u022d\f\20\2\2\u022d\u022e\7%\2\2\u022e")
        buf.write("\u0259\5Z.\21\u022f\u0230\f\17\2\2\u0230\u0231\7&\2\2")
        buf.write("\u0231\u0259\5Z.\20\u0232\u0233\f\16\2\2\u0233\u0234\7")
        buf.write("\'\2\2\u0234\u0259\5Z.\17\u0235\u0236\f\r\2\2\u0236\u0237")
        buf.write("\7(\2\2\u0237\u0259\5Z.\16\u0238\u0239\f\f\2\2\u0239\u023a")
        buf.write("\7)\2\2\u023a\u0259\5Z.\r\u023b\u023c\f\13\2\2\u023c\u023d")
        buf.write("\7\16\2\2\u023d\u023e\5Z.\2\u023e\u023f\7\17\2\2\u023f")
        buf.write("\u0240\5Z.\f\u0240\u0259\3\2\2\2\u0241\u0242\f\n\2\2\u0242")
        buf.write("\u0243\7\r\2\2\u0243\u0259\5Z.\13\u0244\u0245\f\t\2\2")
        buf.write("\u0245\u0246\5\\/\2\u0246\u0247\5Z.\n\u0247\u0259\3\2")
        buf.write("\2\2\u0248\u0249\f&\2\2\u0249\u024a\7\5\2\2\u024a\u024b")
        buf.write("\5X-\2\u024b\u024c\7\6\2\2\u024c\u0259\3\2\2\2\u024d\u024e")
        buf.write("\f%\2\2\u024e\u024f\7\20\2\2\u024f\u0259\5b\62\2\u0250")
        buf.write("\u0251\f$\2\2\u0251\u0259\5T+\2\u0252\u0253\f\"\2\2\u0253")
        buf.write("\u0254\6.\31\2\u0254\u0259\7\21\2\2\u0255\u0256\f!\2\2")
        buf.write("\u0256\u0257\6.\33\2\u0257\u0259\7\22\2\2\u0258\u0217")
        buf.write("\3\2\2\2\u0258\u021a\3\2\2\2\u0258\u021d\3\2\2\2\u0258")
        buf.write("\u0220\3\2\2\2\u0258\u0223\3\2\2\2\u0258\u0226\3\2\2\2")
        buf.write("\u0258\u0229\3\2\2\2\u0258\u022c\3\2\2\2\u0258\u022f\3")
        buf.write("\2\2\2\u0258\u0232\3\2\2\2\u0258\u0235\3\2\2\2\u0258\u0238")
        buf.write("\3\2\2\2\u0258\u023b\3\2\2\2\u0258\u0241\3\2\2\2\u0258")
        buf.write("\u0244\3\2\2\2\u0258\u0248\3\2\2\2\u0258\u024d\3\2\2\2")
        buf.write("\u0258\u0250\3\2\2\2\u0258\u0252\3\2\2\2\u0258\u0255\3")
        buf.write("\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258\3\2\2\2\u025a\u025b")
        buf.write("\3\2\2\2\u025b[\3\2\2\2\u025c\u025a\3\2\2\2\u025d\u025e")
        buf.write("\t\b\2\2\u025e]\3\2\2\2\u025f\u0262\t\t\2\2\u0260\u0262")
        buf.write("\5`\61\2\u0261\u025f\3\2\2\2\u0261\u0260\3\2\2\2\u0262")
        buf.write("_\3\2\2\2\u0263\u0264\t\n\2\2\u0264a\3\2\2\2\u0265\u0268")
        buf.write("\7c\2\2\u0266\u0268\5d\63\2\u0267\u0265\3\2\2\2\u0267")
        buf.write("\u0266\3\2\2\2\u0268c\3\2\2\2\u0269\u026d\5f\64\2\u026a")
        buf.write("\u026d\5h\65\2\u026b\u026d\t\13\2\2\u026c\u0269\3\2\2")
        buf.write("\2\u026c\u026a\3\2\2\2\u026c\u026b\3\2\2\2\u026de\3\2")
        buf.write("\2\2\u026e\u026f\t\f\2\2\u026fg\3\2\2\2\u0270\u0271\t")
        buf.write("\r\2\2\u0271i\3\2\2\2\u0272\u0273\6\66\34\2\u0273\u0274")
        buf.write("\7c\2\2\u0274\u0275\5P)\2\u0275k\3\2\2\2\u0276\u0277\6")
        buf.write("\67\35\2\u0277\u0278\7c\2\2\u0278\u0279\5P)\2\u0279m\3")
        buf.write("\2\2\2\u027a\u027f\7\13\2\2\u027b\u027f\7\2\2\3\u027c")
        buf.write("\u027f\68\36\2\u027d\u027f\68\37\2\u027e\u027a\3\2\2\2")
        buf.write("\u027e\u027b\3\2\2\2\u027e\u027c\3\2\2\2\u027e\u027d\3")
        buf.write("\2\2\2\u027fo\3\2\2\2\u0280\u0281\7\2\2\3\u0281q\3\2\2")
        buf.write("\29s\u008f\u0093\u009a\u00a5\u00aa\u00bb\u00ce\u00d2\u00d6")
        buf.write("\u00e0\u00e4\u00fa\u0101\u0108\u010f\u0121\u0125\u0127")
        buf.write("\u012e\u0134\u0139\u0151\u0163\u016f\u0173\u0178\u017c")
        buf.write("\u017f\u0182\u0187\u018c\u0191\u0197\u019e\u01a2\u01a9")
        buf.write("\u01bf\u01c4\u01ce\u01d2\u01d4\u01d9\u01dd\u01e4\u01ea")
        buf.write("\u01ee\u01f8\u0215\u0258\u025a\u0261\u0267\u026c\u027e")
        return buf.getvalue()


class js_grammarParser ( Parser ):

    grammarFileName = "js_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'?'", 
                     "':'", "'.'", "'++'", "'--'", "'+'", "'-'", "'~'", 
                     "'!'", "'*'", "'/'", "'%'", "'>>'", "'<<'", "'>>>'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'==='", 
                     "'!=='", "'&'", "'^'", "'|'", "'&&'", "'||'", "'*='", 
                     "'/='", "'%='", "'+='", "'-='", "'<<='", "'>>='", "'>>>='", 
                     "'&='", "'^='", "'|='", "'null'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'break'", "'do'", "'instanceof'", "'typeof'", 
                     "'case'", "'else'", "'new'", "'var'", "'let'", "'catch'", 
                     "'finally'", "'return'", "'void'", "'continue'", "'for'", 
                     "'switch'", "'while'", "'debugger'", "'function'", 
                     "'this'", "'with'", "'default'", "'if'", "'throw'", 
                     "'delete'", "'in'", "'try'", "'class'", "'enum'", "'extends'", 
                     "'super'", "'const'", "'export'", "'import'" ]

    symbolicNames = [ "<INVALID>", "RegularExpressionLiteral", "LineTerminator", 
                      "OpenBracket", "CloseBracket", "OpenParen", "CloseParen", 
                      "OpenBrace", "CloseBrace", "SemiColon", "Comma", "Assign", 
                      "QuestionMark", "Colon", "Dot", "PlusPlus", "MinusMinus", 
                      "Plus", "Minus", "BitNot", "Not", "Multiply", "Divide", 
                      "Modulus", "RightShiftArithmetic", "LeftShiftArithmetic", 
                      "RightShiftLogical", "LessThan", "MoreThan", "LessThanEquals", 
                      "GreaterThanEquals", "Equals", "NotEquals", "IdentityEquals", 
                      "IdentityNotEquals", "BitAnd", "BitXOr", "BitOr", 
                      "And", "Or", "MultiplyAssign", "DivideAssign", "ModulusAssign", 
                      "PlusAssign", "MinusAssign", "LeftShiftArithmeticAssign", 
                      "RightShiftArithmeticAssign", "RightShiftLogicalAssign", 
                      "BitAndAssign", "BitXorAssign", "BitOrAssign", "NullLiteral", 
                      "BooleanLiteral", "DecimalLiteral", "HexIntegerLiteral", 
                      "Break", "Do", "Instanceof", "Typeof", "Case", "Else", 
                      "New", "Var", "Let", "Catch", "Finally", "Return", 
                      "Void", "Continue", "For", "Switch", "While", "Debugger", 
                      "Function", "This", "With", "Default", "If", "Throw", 
                      "Delete", "In", "Try", "Class", "Enum", "Extends", 
                      "Super", "Const", "Export", "Import", "Implements", 
                      "Private", "Public", "Interface", "Package", "Protected", 
                      "Static", "Yield", "Identifier", "StringLiteral", 
                      "WhiteSpaces", "MultiLineComment", "SingleLineComment", 
                      "UnexpectedCharacter", "Ellipsis", "OctalIntegerLiteral" ]

    RULE_program = 0
    RULE_sourceElement = 1
    RULE_statement = 2
    RULE_block = 3
    RULE_statementList = 4
    RULE_variableStatement = 5
    RULE_variableDeclarationList = 6
    RULE_variableDeclaration = 7
    RULE_initialiser = 8
    RULE_emptyStatement = 9
    RULE_expressionStatement = 10
    RULE_ifStatement = 11
    RULE_iterationStatement = 12
    RULE_varModifier = 13
    RULE_continueStatement = 14
    RULE_breakStatement = 15
    RULE_returnStatement = 16
    RULE_withStatement = 17
    RULE_switchStatement = 18
    RULE_caseBlock = 19
    RULE_caseClauses = 20
    RULE_caseClause = 21
    RULE_defaultClause = 22
    RULE_labelledStatement = 23
    RULE_throwStatement = 24
    RULE_tryStatement = 25
    RULE_catchProduction = 26
    RULE_finallyProduction = 27
    RULE_debuggerStatement = 28
    RULE_functionDeclaration = 29
    RULE_formalParameterList = 30
    RULE_functionBody = 31
    RULE_sourceElements = 32
    RULE_arrayLiteral = 33
    RULE_elementList = 34
    RULE_elision = 35
    RULE_objectLiteral = 36
    RULE_propertyNameAndValueList = 37
    RULE_propertyAssignment = 38
    RULE_propertyName = 39
    RULE_propertySetParameterList = 40
    RULE_arguments = 41
    RULE_argument = 42
    RULE_expressionSequence = 43
    RULE_singleExpression = 44
    RULE_assignmentOperator = 45
    RULE_literal = 46
    RULE_numericLiteral = 47
    RULE_identifierName = 48
    RULE_reservedWord = 49
    RULE_keyword = 50
    RULE_futureReservedWord = 51
    RULE_getter = 52
    RULE_setter = 53
    RULE_eos = 54
    RULE_eof = 55

    ruleNames =  [ "program", "sourceElement", "statement", "block", "statementList", 
                   "variableStatement", "variableDeclarationList", "variableDeclaration", 
                   "initialiser", "emptyStatement", "expressionStatement", 
                   "ifStatement", "iterationStatement", "varModifier", "continueStatement", 
                   "breakStatement", "returnStatement", "withStatement", 
                   "switchStatement", "caseBlock", "caseClauses", "caseClause", 
                   "defaultClause", "labelledStatement", "throwStatement", 
                   "tryStatement", "catchProduction", "finallyProduction", 
                   "debuggerStatement", "functionDeclaration", "formalParameterList", 
                   "functionBody", "sourceElements", "arrayLiteral", "elementList", 
                   "elision", "objectLiteral", "propertyNameAndValueList", 
                   "propertyAssignment", "propertyName", "propertySetParameterList", 
                   "arguments", "argument", "expressionSequence", "singleExpression", 
                   "assignmentOperator", "literal", "numericLiteral", "identifierName", 
                   "reservedWord", "keyword", "futureReservedWord", "getter", 
                   "setter", "eos", "eof" ]

    EOF = Token.EOF
    RegularExpressionLiteral=1
    LineTerminator=2
    OpenBracket=3
    CloseBracket=4
    OpenParen=5
    CloseParen=6
    OpenBrace=7
    CloseBrace=8
    SemiColon=9
    Comma=10
    Assign=11
    QuestionMark=12
    Colon=13
    Dot=14
    PlusPlus=15
    MinusMinus=16
    Plus=17
    Minus=18
    BitNot=19
    Not=20
    Multiply=21
    Divide=22
    Modulus=23
    RightShiftArithmetic=24
    LeftShiftArithmetic=25
    RightShiftLogical=26
    LessThan=27
    MoreThan=28
    LessThanEquals=29
    GreaterThanEquals=30
    Equals=31
    NotEquals=32
    IdentityEquals=33
    IdentityNotEquals=34
    BitAnd=35
    BitXOr=36
    BitOr=37
    And=38
    Or=39
    MultiplyAssign=40
    DivideAssign=41
    ModulusAssign=42
    PlusAssign=43
    MinusAssign=44
    LeftShiftArithmeticAssign=45
    RightShiftArithmeticAssign=46
    RightShiftLogicalAssign=47
    BitAndAssign=48
    BitXorAssign=49
    BitOrAssign=50
    NullLiteral=51
    BooleanLiteral=52
    DecimalLiteral=53
    HexIntegerLiteral=54
    Break=55
    Do=56
    Instanceof=57
    Typeof=58
    Case=59
    Else=60
    New=61
    Var=62
    Let=63
    Catch=64
    Finally=65
    Return=66
    Void=67
    Continue=68
    For=69
    Switch=70
    While=71
    Debugger=72
    Function=73
    This=74
    With=75
    Default=76
    If=77
    Throw=78
    Delete=79
    In=80
    Try=81
    Class=82
    Enum=83
    Extends=84
    Super=85
    Const=86
    Export=87
    Import=88
    Implements=89
    Private=90
    Public=91
    Interface=92
    Package=93
    Protected=94
    Static=95
    Yield=96
    Identifier=97
    StringLiteral=98
    WhiteSpaces=99
    MultiLineComment=100
    SingleLineComment=101
    UnexpectedCharacter=102
    Ellipsis=103
    OctalIntegerLiteral=104

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



      
      
        private ITokenStream _input => this.InputStream as ITokenStream;
       
        private bool here(int type) {
            // Get the token ahead of the current index.
            int possibleIndexEosToken = this.CurrentToken.TokenIndex - 1;
            IToken ahead = _input.Get(possibleIndexEosToken);
            // Check if the token resides on the Hidden channel and if it's of the
            // provided type.
            return (ahead.Channel == Lexer.Hidden) && (ahead.Type == type);
        }


        private bool lineTerminatorAhead() {
            // Get the token ahead of the current index.
            int possibleIndexEosToken = this.CurrentToken.TokenIndex - 1;
            IToken ahead = _input.Get(possibleIndexEosToken);
            if (ahead.Channel != Lexer.Hidden) {
                // We're only interested in tokens on the Hidden channel.
                return false;
            }

            if (ahead.Type == LineTerminator) {
                // There is definitely a line terminator ahead.
                return true;
            }

            if (ahead.Type == WhiteSpaces) {
                // Get the token ahead of the current whitespaces.
                possibleIndexEosToken = this.CurrentToken.TokenIndex - 2;
                ahead = _input.Get(possibleIndexEosToken);
            }

            // Get the token's text and type.
            string text = ahead.Text;
            int type = ahead.Type;

            // Check if the token is, or contains a line terminator.
            return (type == MultiLineComment && (text.Contains("\r") || text.Contains("\n"))) ||
                    (type == LineTerminator);
        }                                
        
        private void notImplemented()
        {
            throw new NotImplementedException("This lexem construction is not implemented");
        }



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(js_grammarParser.EOF, 0)

        def sourceElements(self):
            return self.getTypedRuleContext(js_grammarParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = js_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0):
                self.state = 112
                self.sourceElements()


            self.state = 115
            self.match(js_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_sourceElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElement" ):
                listener.enterSourceElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElement" ):
                listener.exitSourceElement(self)




    def sourceElement(self):

        localctx = js_grammarParser.SourceElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sourceElement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(js_grammarParser.BlockContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(js_grammarParser.VariableStatementContext,0)


        def emptyStatement(self):
            return self.getTypedRuleContext(js_grammarParser.EmptyStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(js_grammarParser.IfStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(js_grammarParser.IterationStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(js_grammarParser.ContinueStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(js_grammarParser.BreakStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(js_grammarParser.ReturnStatementContext,0)


        def withStatement(self):
            return self.getTypedRuleContext(js_grammarParser.WithStatementContext,0)


        def labelledStatement(self):
            return self.getTypedRuleContext(js_grammarParser.LabelledStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(js_grammarParser.SwitchStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(js_grammarParser.ThrowStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(js_grammarParser.TryStatementContext,0)


        def debuggerStatement(self):
            return self.getTypedRuleContext(js_grammarParser.DebuggerStatementContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = js_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.OpenBrace]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.block()
                pass
            elif token in [js_grammarParser.Var, js_grammarParser.Let, js_grammarParser.Const]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.variableStatement()
                pass
            elif token in [js_grammarParser.SemiColon]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                self.emptyStatement()
                pass
            elif token in [js_grammarParser.If]:
                self.enterOuterAlt(localctx, 4)
                self.state = 122
                self.ifStatement()
                pass
            elif token in [js_grammarParser.Do, js_grammarParser.For, js_grammarParser.While]:
                self.enterOuterAlt(localctx, 5)
                self.state = 123
                self.iterationStatement()
                pass
            elif token in [js_grammarParser.Continue]:
                self.enterOuterAlt(localctx, 6)
                self.state = 124
                self.continueStatement()
                pass
            elif token in [js_grammarParser.Break]:
                self.enterOuterAlt(localctx, 7)
                self.state = 125
                self.breakStatement()
                pass
            elif token in [js_grammarParser.Return]:
                self.enterOuterAlt(localctx, 8)
                self.state = 126
                self.returnStatement()
                pass
            elif token in [js_grammarParser.With]:
                self.enterOuterAlt(localctx, 9)
                self.state = 127
                self.withStatement()
                pass
            elif token in [js_grammarParser.Identifier]:
                self.enterOuterAlt(localctx, 10)
                self.state = 128
                self.labelledStatement()
                pass
            elif token in [js_grammarParser.Switch]:
                self.enterOuterAlt(localctx, 11)
                self.state = 129
                self.switchStatement()
                notImplemented();
                pass
            elif token in [js_grammarParser.Throw]:
                self.enterOuterAlt(localctx, 12)
                self.state = 132
                self.throwStatement()
                notImplemented();
                pass
            elif token in [js_grammarParser.Try]:
                self.enterOuterAlt(localctx, 13)
                self.state = 135
                self.tryStatement()
                notImplemented();
                pass
            elif token in [js_grammarParser.Debugger]:
                self.enterOuterAlt(localctx, 14)
                self.state = 138
                self.debuggerStatement()
                notImplemented();
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


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def statementList(self):
            return self.getTypedRuleContext(js_grammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = js_grammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(js_grammarParser.OpenBrace)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0):
                self.state = 144
                self.statementList()


            self.state = 147
            self.match(js_grammarParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return js_grammarParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = js_grammarParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.statement()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarationList(self):
            return self.getTypedRuleContext(js_grammarParser.VariableDeclarationListContext,0)


        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_variableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableStatement" ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableStatement" ):
                listener.exitVariableStatement(self)




    def variableStatement(self):

        localctx = js_grammarParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.variableDeclarationList()
            self.state = 155
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varModifier(self):
            return self.getTypedRuleContext(js_grammarParser.VarModifierContext,0)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.VariableDeclarationContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_variableDeclarationList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarationList" ):
                listener.enterVariableDeclarationList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarationList" ):
                listener.exitVariableDeclarationList(self)




    def variableDeclarationList(self):

        localctx = js_grammarParser.VariableDeclarationListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclarationList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.varModifier()
            self.state = 158
            self.variableDeclaration()
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 159
                    self.match(js_grammarParser.Comma)
                    self.state = 160
                    self.variableDeclaration() 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def initialiser(self):
            return self.getTypedRuleContext(js_grammarParser.InitialiserContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = js_grammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(js_grammarParser.Identifier)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 167
                self.initialiser()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitialiserContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assign(self):
            return self.getToken(js_grammarParser.Assign, 0)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_initialiser

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInitialiser" ):
                listener.enterInitialiser(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInitialiser" ):
                listener.exitInitialiser(self)




    def initialiser(self):

        localctx = js_grammarParser.InitialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(js_grammarParser.Assign)
            self.state = 171
            self.singleExpression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(js_grammarParser.SemiColon, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_emptyStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)




    def emptyStatement(self):

        localctx = js_grammarParser.EmptyStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_emptyStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(js_grammarParser.SemiColon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)




    def expressionStatement(self):

        localctx = js_grammarParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.expressionSequence()
            self.state = 176
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(js_grammarParser.If, 0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.StatementContext,i)


        def Else(self):
            return self.getToken(js_grammarParser.Else, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = js_grammarParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(js_grammarParser.If)
            self.state = 179
            self.match(js_grammarParser.OpenParen)
            self.state = 180
            self.expressionSequence()
            self.state = 181
            self.match(js_grammarParser.CloseParen)
            self.state = 182
            self.statement()
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 183
                self.match(js_grammarParser.Else)
                self.state = 184
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return js_grammarParser.RULE_iterationStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DoStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Do(self):
            return self.getToken(js_grammarParser.Do, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)

        def While(self):
            return self.getToken(js_grammarParser.While, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoStatement" ):
                listener.enterDoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoStatement" ):
                listener.exitDoStatement(self)


    class ForVarStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(js_grammarParser.For, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def Var(self):
            return self.getToken(js_grammarParser.Var, 0)
        def variableDeclarationList(self):
            return self.getTypedRuleContext(js_grammarParser.VariableDeclarationListContext,0)

        def SemiColon(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.SemiColon)
            else:
                return self.getToken(js_grammarParser.SemiColon, i)
        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarStatement" ):
                listener.enterForVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarStatement" ):
                listener.exitForVarStatement(self)


    class ForVarInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(js_grammarParser.For, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def Var(self):
            return self.getToken(js_grammarParser.Var, 0)
        def variableDeclaration(self):
            return self.getTypedRuleContext(js_grammarParser.VariableDeclarationContext,0)

        def In(self):
            return self.getToken(js_grammarParser.In, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForVarInStatement" ):
                listener.enterForVarInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForVarInStatement" ):
                listener.exitForVarInStatement(self)


    class WhileStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def While(self):
            return self.getToken(js_grammarParser.While, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)


    class ForStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(js_grammarParser.For, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def SemiColon(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.SemiColon)
            else:
                return self.getToken(js_grammarParser.SemiColon, i)
        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)

        def expressionSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.ExpressionSequenceContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)


    class ForInStatementContext(IterationStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.IterationStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def For(self):
            return self.getToken(js_grammarParser.For, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def In(self):
            return self.getToken(js_grammarParser.In, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInStatement" ):
                listener.enterForInStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInStatement" ):
                listener.exitForInStatement(self)



    def iterationStatement(self):

        localctx = js_grammarParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = js_grammarParser.DoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(js_grammarParser.Do)
                self.state = 188
                self.statement()
                self.state = 189
                self.match(js_grammarParser.While)
                self.state = 190
                self.match(js_grammarParser.OpenParen)
                self.state = 191
                self.expressionSequence()
                self.state = 192
                self.match(js_grammarParser.CloseParen)
                self.state = 193
                self.eos()
                pass

            elif la_ == 2:
                localctx = js_grammarParser.WhileStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.match(js_grammarParser.While)
                self.state = 196
                self.match(js_grammarParser.OpenParen)
                self.state = 197
                self.expressionSequence()
                self.state = 198
                self.match(js_grammarParser.CloseParen)
                self.state = 199
                self.statement()
                pass

            elif la_ == 3:
                localctx = js_grammarParser.ForStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(js_grammarParser.For)
                self.state = 202
                self.match(js_grammarParser.OpenParen)
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                    self.state = 203
                    self.expressionSequence()


                self.state = 206
                self.match(js_grammarParser.SemiColon)
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                    self.state = 207
                    self.expressionSequence()


                self.state = 210
                self.match(js_grammarParser.SemiColon)
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                    self.state = 211
                    self.expressionSequence()


                self.state = 214
                self.match(js_grammarParser.CloseParen)
                self.state = 215
                self.statement()
                pass

            elif la_ == 4:
                localctx = js_grammarParser.ForVarStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                self.match(js_grammarParser.For)
                self.state = 217
                self.match(js_grammarParser.OpenParen)
                self.state = 218
                self.match(js_grammarParser.Var)
                self.state = 219
                self.variableDeclarationList()
                self.state = 220
                self.match(js_grammarParser.SemiColon)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                    self.state = 221
                    self.expressionSequence()


                self.state = 224
                self.match(js_grammarParser.SemiColon)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                    self.state = 225
                    self.expressionSequence()


                self.state = 228
                self.match(js_grammarParser.CloseParen)
                self.state = 229
                self.statement()
                pass

            elif la_ == 5:
                localctx = js_grammarParser.ForInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 231
                self.match(js_grammarParser.For)
                self.state = 232
                self.match(js_grammarParser.OpenParen)
                self.state = 233
                self.singleExpression(0)
                self.state = 234
                self.match(js_grammarParser.In)
                self.state = 235
                self.expressionSequence()
                self.state = 236
                self.match(js_grammarParser.CloseParen)
                self.state = 237
                self.statement()
                pass

            elif la_ == 6:
                localctx = js_grammarParser.ForVarInStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(js_grammarParser.For)
                self.state = 240
                self.match(js_grammarParser.OpenParen)
                self.state = 241
                self.match(js_grammarParser.Var)
                self.state = 242
                self.variableDeclaration()
                self.state = 243
                self.match(js_grammarParser.In)
                self.state = 244
                self.expressionSequence()
                self.state = 245
                self.match(js_grammarParser.CloseParen)
                self.state = 246
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarModifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Var(self):
            return self.getToken(js_grammarParser.Var, 0)

        def Let(self):
            return self.getToken(js_grammarParser.Let, 0)

        def Const(self):
            return self.getToken(js_grammarParser.Const, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_varModifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarModifier" ):
                listener.enterVarModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarModifier" ):
                listener.exitVarModifier(self)




    def varModifier(self):

        localctx = js_grammarParser.VarModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            _la = self._input.LA(1)
            if not(((((_la - 62)) & ~0x3f) == 0 and ((1 << (_la - 62)) & ((1 << (js_grammarParser.Var - 62)) | (1 << (js_grammarParser.Let - 62)) | (1 << (js_grammarParser.Const - 62)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Continue(self):
            return self.getToken(js_grammarParser.Continue, 0)

        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = js_grammarParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(js_grammarParser.Continue)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 253
                if not !here(LineTerminator):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "!here(LineTerminator)")
                self.state = 254
                self.match(js_grammarParser.Identifier)


            self.state = 257
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(js_grammarParser.Break, 0)

        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = js_grammarParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(js_grammarParser.Break)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 260
                if not !here(LineTerminator):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "!here(LineTerminator)")
                self.state = 261
                self.match(js_grammarParser.Identifier)


            self.state = 264
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Return(self):
            return self.getToken(js_grammarParser.Return, 0)

        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = js_grammarParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(js_grammarParser.Return)
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 267
                if not !here(LineTerminator):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "!here(LineTerminator)")
                self.state = 268
                self.expressionSequence()


            self.state = 271
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def With(self):
            return self.getToken(js_grammarParser.With, 0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_withStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithStatement" ):
                listener.enterWithStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithStatement" ):
                listener.exitWithStatement(self)




    def withStatement(self):

        localctx = js_grammarParser.WithStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_withStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(js_grammarParser.With)
            self.state = 274
            self.match(js_grammarParser.OpenParen)
            self.state = 275
            self.expressionSequence()
            self.state = 276
            self.match(js_grammarParser.CloseParen)
            self.state = 277
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Switch(self):
            return self.getToken(js_grammarParser.Switch, 0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def caseBlock(self):
            return self.getTypedRuleContext(js_grammarParser.CaseBlockContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)




    def switchStatement(self):

        localctx = js_grammarParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_switchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(js_grammarParser.Switch)
            self.state = 280
            self.match(js_grammarParser.OpenParen)
            self.state = 281
            self.expressionSequence()
            self.state = 282
            self.match(js_grammarParser.CloseParen)
            self.state = 283
            self.caseBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def caseClauses(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.CaseClausesContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.CaseClausesContext,i)


        def defaultClause(self):
            return self.getTypedRuleContext(js_grammarParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_caseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseBlock" ):
                listener.enterCaseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseBlock" ):
                listener.exitCaseBlock(self)




    def caseBlock(self):

        localctx = js_grammarParser.CaseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_caseBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(js_grammarParser.OpenBrace)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Case:
                self.state = 286
                self.caseClauses()


            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Default:
                self.state = 289
                self.defaultClause()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==js_grammarParser.Case:
                    self.state = 290
                    self.caseClauses()




            self.state = 295
            self.match(js_grammarParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.CaseClauseContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.CaseClauseContext,i)


        def getRuleIndex(self):
            return js_grammarParser.RULE_caseClauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClauses" ):
                listener.enterCaseClauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClauses" ):
                listener.exitCaseClauses(self)




    def caseClauses(self):

        localctx = js_grammarParser.CaseClausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_caseClauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 297
                self.caseClause()
                self.state = 300 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==js_grammarParser.Case):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Case(self):
            return self.getToken(js_grammarParser.Case, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def Colon(self):
            return self.getToken(js_grammarParser.Colon, 0)

        def statementList(self):
            return self.getTypedRuleContext(js_grammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_caseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseClause" ):
                listener.enterCaseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseClause" ):
                listener.exitCaseClause(self)




    def caseClause(self):

        localctx = js_grammarParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(js_grammarParser.Case)
            self.state = 303
            self.expressionSequence()
            self.state = 304
            self.match(js_grammarParser.Colon)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0):
                self.state = 305
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Default(self):
            return self.getToken(js_grammarParser.Default, 0)

        def Colon(self):
            return self.getToken(js_grammarParser.Colon, 0)

        def statementList(self):
            return self.getTypedRuleContext(js_grammarParser.StatementListContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_defaultClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultClause" ):
                listener.enterDefaultClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultClause" ):
                listener.exitDefaultClause(self)




    def defaultClause(self):

        localctx = js_grammarParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(js_grammarParser.Default)
            self.state = 309
            self.match(js_grammarParser.Colon)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0):
                self.state = 310
                self.statementList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def Colon(self):
            return self.getToken(js_grammarParser.Colon, 0)

        def statement(self):
            return self.getTypedRuleContext(js_grammarParser.StatementContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_labelledStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelledStatement" ):
                listener.enterLabelledStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelledStatement" ):
                listener.exitLabelledStatement(self)




    def labelledStatement(self):

        localctx = js_grammarParser.LabelledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_labelledStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(js_grammarParser.Identifier)
            self.state = 314
            self.match(js_grammarParser.Colon)
            self.state = 315
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Throw(self):
            return self.getToken(js_grammarParser.Throw, 0)

        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = js_grammarParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_throwStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(js_grammarParser.Throw)
            self.state = 318
            if not !here(LineTerminator):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "!here(LineTerminator)")
            self.state = 319
            self.expressionSequence()
            self.state = 320
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Try(self):
            return self.getToken(js_grammarParser.Try, 0)

        def block(self):
            return self.getTypedRuleContext(js_grammarParser.BlockContext,0)


        def catchProduction(self):
            return self.getTypedRuleContext(js_grammarParser.CatchProductionContext,0)


        def finallyProduction(self):
            return self.getTypedRuleContext(js_grammarParser.FinallyProductionContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = js_grammarParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_tryStatement)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.match(js_grammarParser.Try)
                self.state = 323
                self.block()
                self.state = 324
                self.catchProduction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(js_grammarParser.Try)
                self.state = 327
                self.block()
                self.state = 328
                self.finallyProduction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 330
                self.match(js_grammarParser.Try)
                self.state = 331
                self.block()
                self.state = 332
                self.catchProduction()
                self.state = 333
                self.finallyProduction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Catch(self):
            return self.getToken(js_grammarParser.Catch, 0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def block(self):
            return self.getTypedRuleContext(js_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_catchProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchProduction" ):
                listener.enterCatchProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchProduction" ):
                listener.exitCatchProduction(self)




    def catchProduction(self):

        localctx = js_grammarParser.CatchProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_catchProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(js_grammarParser.Catch)
            self.state = 338
            self.match(js_grammarParser.OpenParen)
            self.state = 339
            self.match(js_grammarParser.Identifier)
            self.state = 340
            self.match(js_grammarParser.CloseParen)
            self.state = 341
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyProductionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Finally(self):
            return self.getToken(js_grammarParser.Finally, 0)

        def block(self):
            return self.getTypedRuleContext(js_grammarParser.BlockContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_finallyProduction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyProduction" ):
                listener.enterFinallyProduction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyProduction" ):
                listener.exitFinallyProduction(self)




    def finallyProduction(self):

        localctx = js_grammarParser.FinallyProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_finallyProduction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(js_grammarParser.Finally)
            self.state = 344
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DebuggerStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Debugger(self):
            return self.getToken(js_grammarParser.Debugger, 0)

        def eos(self):
            return self.getTypedRuleContext(js_grammarParser.EosContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_debuggerStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDebuggerStatement" ):
                listener.enterDebuggerStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDebuggerStatement" ):
                listener.exitDebuggerStatement(self)




    def debuggerStatement(self):

        localctx = js_grammarParser.DebuggerStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_debuggerStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(js_grammarParser.Debugger)
            self.state = 347
            self.eos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Function(self):
            return self.getToken(js_grammarParser.Function, 0)

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)

        def functionBody(self):
            return self.getTypedRuleContext(js_grammarParser.FunctionBodyContext,0)


        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def formalParameterList(self):
            return self.getTypedRuleContext(js_grammarParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = js_grammarParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(js_grammarParser.Function)
            self.state = 350
            self.match(js_grammarParser.Identifier)
            self.state = 351
            self.match(js_grammarParser.OpenParen)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Identifier:
                self.state = 352
                self.formalParameterList()


            self.state = 355
            self.match(js_grammarParser.CloseParen)
            self.state = 356
            self.match(js_grammarParser.OpenBrace)
            self.state = 357
            self.functionBody()
            self.state = 358
            self.match(js_grammarParser.CloseBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Identifier)
            else:
                return self.getToken(js_grammarParser.Identifier, i)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = js_grammarParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_formalParameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(js_grammarParser.Identifier)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==js_grammarParser.Comma:
                self.state = 361
                self.match(js_grammarParser.Comma)
                self.state = 362
                self.match(js_grammarParser.Identifier)
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElements(self):
            return self.getTypedRuleContext(js_grammarParser.SourceElementsContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)




    def functionBody(self):

        localctx = js_grammarParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0):
                self.state = 368
                self.sourceElements()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sourceElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SourceElementContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SourceElementContext,i)


        def getRuleIndex(self):
            return js_grammarParser.RULE_sourceElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceElements" ):
                listener.enterSourceElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceElements" ):
                listener.exitSourceElements(self)




    def sourceElements(self):

        localctx = js_grammarParser.SourceElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sourceElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 371
                self.sourceElement()
                self.state = 374 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.SemiColon) | (1 << js_grammarParser.Break) | (1 << js_grammarParser.Do) | (1 << js_grammarParser.Var) | (1 << js_grammarParser.Let))) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & ((1 << (js_grammarParser.Return - 66)) | (1 << (js_grammarParser.Continue - 66)) | (1 << (js_grammarParser.For - 66)) | (1 << (js_grammarParser.Switch - 66)) | (1 << (js_grammarParser.While - 66)) | (1 << (js_grammarParser.Debugger - 66)) | (1 << (js_grammarParser.With - 66)) | (1 << (js_grammarParser.If - 66)) | (1 << (js_grammarParser.Throw - 66)) | (1 << (js_grammarParser.Try - 66)) | (1 << (js_grammarParser.Const - 66)) | (1 << (js_grammarParser.Identifier - 66)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBracket(self):
            return self.getToken(js_grammarParser.OpenBracket, 0)

        def CloseBracket(self):
            return self.getToken(js_grammarParser.CloseBracket, 0)

        def elementList(self):
            return self.getTypedRuleContext(js_grammarParser.ElementListContext,0)


        def Comma(self):
            return self.getToken(js_grammarParser.Comma, 0)

        def elision(self):
            return self.getTypedRuleContext(js_grammarParser.ElisionContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)




    def arrayLiteral(self):

        localctx = js_grammarParser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(js_grammarParser.OpenBracket)
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 377
                self.elementList()


            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(js_grammarParser.Comma)


            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Comma:
                self.state = 383
                self.elision()


            self.state = 386
            self.match(js_grammarParser.CloseBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)


        def elision(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.ElisionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.ElisionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_elementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementList" ):
                listener.enterElementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementList" ):
                listener.exitElementList(self)




    def elementList(self):

        localctx = js_grammarParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Comma:
                self.state = 388
                self.elision()


            self.state = 391
            self.singleExpression(0)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 392
                    self.match(js_grammarParser.Comma)
                    self.state = 394
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==js_grammarParser.Comma:
                        self.state = 393
                        self.elision()


                    self.state = 396
                    self.singleExpression(0) 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_elision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElision" ):
                listener.enterElision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElision" ):
                listener.exitElision(self)




    def elision(self):

        localctx = js_grammarParser.ElisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 402
                self.match(js_grammarParser.Comma)
                self.state = 405 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==js_grammarParser.Comma):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def propertyNameAndValueList(self):
            return self.getTypedRuleContext(js_grammarParser.PropertyNameAndValueListContext,0)


        def Comma(self):
            return self.getToken(js_grammarParser.Comma, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_objectLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteral" ):
                listener.enterObjectLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteral" ):
                listener.exitObjectLiteral(self)




    def objectLiteral(self):

        localctx = js_grammarParser.ObjectLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_objectLiteral)
        self._la = 0 # Token type
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.match(js_grammarParser.OpenBrace)
                self.state = 408
                self.match(js_grammarParser.CloseBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 409
                self.match(js_grammarParser.OpenBrace)
                self.state = 410
                self.propertyNameAndValueList()
                self.state = 412
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==js_grammarParser.Comma:
                    self.state = 411
                    self.match(js_grammarParser.Comma)


                self.state = 414
                self.match(js_grammarParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyNameAndValueListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def propertyAssignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.PropertyAssignmentContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.PropertyAssignmentContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_propertyNameAndValueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyNameAndValueList" ):
                listener.enterPropertyNameAndValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyNameAndValueList" ):
                listener.exitPropertyNameAndValueList(self)




    def propertyNameAndValueList(self):

        localctx = js_grammarParser.PropertyNameAndValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_propertyNameAndValueList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.propertyAssignment()
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419
                    self.match(js_grammarParser.Comma)
                    self.state = 420
                    self.propertyAssignment() 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyAssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return js_grammarParser.RULE_propertyAssignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PropertyExpressionAssignmentContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def propertyName(self):
            return self.getTypedRuleContext(js_grammarParser.PropertyNameContext,0)

        def Colon(self):
            return self.getToken(js_grammarParser.Colon, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyExpressionAssignment" ):
                listener.enterPropertyExpressionAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyExpressionAssignment" ):
                listener.exitPropertyExpressionAssignment(self)


    class PropertySetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setter(self):
            return self.getTypedRuleContext(js_grammarParser.SetterContext,0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def propertySetParameterList(self):
            return self.getTypedRuleContext(js_grammarParser.PropertySetParameterListContext,0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(js_grammarParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertySetter" ):
                listener.enterPropertySetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertySetter" ):
                listener.exitPropertySetter(self)


    class PropertyGetterContext(PropertyAssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.PropertyAssignmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def getter(self):
            return self.getTypedRuleContext(js_grammarParser.GetterContext,0)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(js_grammarParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyGetter" ):
                listener.enterPropertyGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyGetter" ):
                listener.exitPropertyGetter(self)



    def propertyAssignment(self):

        localctx = js_grammarParser.PropertyAssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_propertyAssignment)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                localctx = js_grammarParser.PropertyExpressionAssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.propertyName()
                self.state = 427
                self.match(js_grammarParser.Colon)
                self.state = 428
                self.singleExpression(0)
                pass

            elif la_ == 2:
                localctx = js_grammarParser.PropertyGetterContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.getter()
                self.state = 431
                self.match(js_grammarParser.OpenParen)
                self.state = 432
                self.match(js_grammarParser.CloseParen)
                self.state = 433
                self.match(js_grammarParser.OpenBrace)
                self.state = 434
                self.functionBody()
                self.state = 435
                self.match(js_grammarParser.CloseBrace)
                pass

            elif la_ == 3:
                localctx = js_grammarParser.PropertySetterContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.setter()
                self.state = 438
                self.match(js_grammarParser.OpenParen)
                self.state = 439
                self.propertySetParameterList()
                self.state = 440
                self.match(js_grammarParser.CloseParen)
                self.state = 441
                self.match(js_grammarParser.OpenBrace)
                self.state = 442
                self.functionBody()
                self.state = 443
                self.match(js_grammarParser.CloseBrace)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropertyNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifierName(self):
            return self.getTypedRuleContext(js_grammarParser.IdentifierNameContext,0)


        def StringLiteral(self):
            return self.getToken(js_grammarParser.StringLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(js_grammarParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_propertyName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertyName" ):
                listener.enterPropertyName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertyName" ):
                listener.exitPropertyName(self)




    def propertyName(self):

        localctx = js_grammarParser.PropertyNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_propertyName)
        try:
            self.state = 450
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.NullLiteral, js_grammarParser.BooleanLiteral, js_grammarParser.Break, js_grammarParser.Do, js_grammarParser.Instanceof, js_grammarParser.Typeof, js_grammarParser.Case, js_grammarParser.Else, js_grammarParser.New, js_grammarParser.Var, js_grammarParser.Let, js_grammarParser.Catch, js_grammarParser.Finally, js_grammarParser.Return, js_grammarParser.Void, js_grammarParser.Continue, js_grammarParser.For, js_grammarParser.Switch, js_grammarParser.While, js_grammarParser.Debugger, js_grammarParser.Function, js_grammarParser.This, js_grammarParser.With, js_grammarParser.Default, js_grammarParser.If, js_grammarParser.Throw, js_grammarParser.Delete, js_grammarParser.In, js_grammarParser.Try, js_grammarParser.Class, js_grammarParser.Enum, js_grammarParser.Extends, js_grammarParser.Super, js_grammarParser.Const, js_grammarParser.Export, js_grammarParser.Import, js_grammarParser.Implements, js_grammarParser.Private, js_grammarParser.Public, js_grammarParser.Interface, js_grammarParser.Package, js_grammarParser.Protected, js_grammarParser.Static, js_grammarParser.Yield, js_grammarParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.identifierName()
                pass
            elif token in [js_grammarParser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(js_grammarParser.StringLiteral)
                pass
            elif token in [js_grammarParser.DecimalLiteral, js_grammarParser.HexIntegerLiteral, js_grammarParser.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.numericLiteral()
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


    class PropertySetParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_propertySetParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropertySetParameterList" ):
                listener.enterPropertySetParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropertySetParameterList" ):
                listener.exitPropertySetParameterList(self)




    def propertySetParameterList(self):

        localctx = js_grammarParser.PropertySetParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_propertySetParameterList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(js_grammarParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)

        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.ArgumentContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = js_grammarParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(js_grammarParser.OpenParen)
            self.state = 466
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.OpenBracket) | (1 << js_grammarParser.OpenParen) | (1 << js_grammarParser.OpenBrace) | (1 << js_grammarParser.PlusPlus) | (1 << js_grammarParser.MinusMinus) | (1 << js_grammarParser.Plus) | (1 << js_grammarParser.Minus) | (1 << js_grammarParser.BitNot) | (1 << js_grammarParser.Not) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral) | (1 << js_grammarParser.DecimalLiteral) | (1 << js_grammarParser.HexIntegerLiteral) | (1 << js_grammarParser.Typeof) | (1 << js_grammarParser.New))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (js_grammarParser.Void - 67)) | (1 << (js_grammarParser.Function - 67)) | (1 << (js_grammarParser.This - 67)) | (1 << (js_grammarParser.Delete - 67)) | (1 << (js_grammarParser.Identifier - 67)) | (1 << (js_grammarParser.StringLiteral - 67)) | (1 << (js_grammarParser.Ellipsis - 67)) | (1 << (js_grammarParser.OctalIntegerLiteral - 67)))) != 0):
                self.state = 455
                self.argument()
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 456
                        self.match(js_grammarParser.Comma)
                        self.state = 457
                        self.argument() 
                    self.state = 462
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                self.state = 464
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==js_grammarParser.Comma:
                    self.state = 463
                    self.match(js_grammarParser.Comma)




            self.state = 468
            self.match(js_grammarParser.CloseParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def Ellipsis(self):
            return self.getToken(js_grammarParser.Ellipsis, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = js_grammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==js_grammarParser.Ellipsis:
                self.state = 470
                self.match(js_grammarParser.Ellipsis)


            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 473
                self.singleExpression(0)
                pass

            elif la_ == 2:
                self.state = 474
                self.match(js_grammarParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionSequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(js_grammarParser.Comma)
            else:
                return self.getToken(js_grammarParser.Comma, i)

        def getRuleIndex(self):
            return js_grammarParser.RULE_expressionSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionSequence" ):
                listener.enterExpressionSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionSequence" ):
                listener.exitExpressionSequence(self)




    def expressionSequence(self):

        localctx = js_grammarParser.ExpressionSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressionSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.singleExpression(0)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 478
                    self.match(js_grammarParser.Comma)
                    self.state = 479
                    self.singleExpression(0) 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return js_grammarParser.RULE_singleExpression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TernaryExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def QuestionMark(self):
            return self.getToken(js_grammarParser.QuestionMark, 0)
        def Colon(self):
            return self.getToken(js_grammarParser.Colon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryExpression" ):
                listener.enterTernaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryExpression" ):
                listener.exitTernaryExpression(self)


    class LogicalAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def And(self):
            return self.getToken(js_grammarParser.And, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)


    class PreIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PlusPlus(self):
            return self.getToken(js_grammarParser.PlusPlus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrementExpression" ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrementExpression" ):
                listener.exitPreIncrementExpression(self)


    class ObjectLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def objectLiteral(self):
            return self.getTypedRuleContext(js_grammarParser.ObjectLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectLiteralExpression" ):
                listener.enterObjectLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectLiteralExpression" ):
                listener.exitObjectLiteralExpression(self)


    class InExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def In(self):
            return self.getToken(js_grammarParser.In, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInExpression" ):
                listener.enterInExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInExpression" ):
                listener.exitInExpression(self)


    class LogicalOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Or(self):
            return self.getToken(js_grammarParser.Or, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)


    class NotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Not(self):
            return self.getToken(js_grammarParser.Not, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)


    class PreDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MinusMinus(self):
            return self.getToken(js_grammarParser.MinusMinus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecreaseExpression" ):
                listener.enterPreDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecreaseExpression" ):
                listener.exitPreDecreaseExpression(self)


    class ArgumentsExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(js_grammarParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentsExpression" ):
                listener.enterArgumentsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentsExpression" ):
                listener.exitArgumentsExpression(self)


    class ThisExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def This(self):
            return self.getToken(js_grammarParser.This, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThisExpression" ):
                listener.enterThisExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThisExpression" ):
                listener.exitThisExpression(self)


    class FunctionExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Function(self):
            return self.getToken(js_grammarParser.Function, 0)
        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def OpenBrace(self):
            return self.getToken(js_grammarParser.OpenBrace, 0)
        def functionBody(self):
            return self.getTypedRuleContext(js_grammarParser.FunctionBodyContext,0)

        def CloseBrace(self):
            return self.getToken(js_grammarParser.CloseBrace, 0)
        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)
        def formalParameterList(self):
            return self.getTypedRuleContext(js_grammarParser.FormalParameterListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpression" ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpression" ):
                listener.exitFunctionExpression(self)


    class UnaryMinusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Minus(self):
            return self.getToken(js_grammarParser.Minus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpression" ):
                listener.enterUnaryMinusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpression" ):
                listener.exitUnaryMinusExpression(self)


    class AssignmentExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Assign(self):
            return self.getToken(js_grammarParser.Assign, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)


    class PostDecreaseExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def MinusMinus(self):
            return self.getToken(js_grammarParser.MinusMinus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecreaseExpression" ):
                listener.enterPostDecreaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecreaseExpression" ):
                listener.exitPostDecreaseExpression(self)


    class TypeofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Typeof(self):
            return self.getToken(js_grammarParser.Typeof, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeofExpression" ):
                listener.enterTypeofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeofExpression" ):
                listener.exitTypeofExpression(self)


    class InstanceofExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Instanceof(self):
            return self.getToken(js_grammarParser.Instanceof, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceofExpression" ):
                listener.enterInstanceofExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceofExpression" ):
                listener.exitInstanceofExpression(self)


    class UnaryPlusExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Plus(self):
            return self.getToken(js_grammarParser.Plus, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPlusExpression" ):
                listener.enterUnaryPlusExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPlusExpression" ):
                listener.exitUnaryPlusExpression(self)


    class DeleteExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Delete(self):
            return self.getToken(js_grammarParser.Delete, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteExpression" ):
                listener.enterDeleteExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteExpression" ):
                listener.exitDeleteExpression(self)


    class EqualityExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Equals(self):
            return self.getToken(js_grammarParser.Equals, 0)
        def NotEquals(self):
            return self.getToken(js_grammarParser.NotEquals, 0)
        def IdentityEquals(self):
            return self.getToken(js_grammarParser.IdentityEquals, 0)
        def IdentityNotEquals(self):
            return self.getToken(js_grammarParser.IdentityNotEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)


    class BitXOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def BitXOr(self):
            return self.getToken(js_grammarParser.BitXOr, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitXOrExpression" ):
                listener.enterBitXOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitXOrExpression" ):
                listener.exitBitXOrExpression(self)


    class MultiplicativeExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Multiply(self):
            return self.getToken(js_grammarParser.Multiply, 0)
        def Divide(self):
            return self.getToken(js_grammarParser.Divide, 0)
        def Modulus(self):
            return self.getToken(js_grammarParser.Modulus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)


    class BitShiftExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def LeftShiftArithmetic(self):
            return self.getToken(js_grammarParser.LeftShiftArithmetic, 0)
        def RightShiftArithmetic(self):
            return self.getToken(js_grammarParser.RightShiftArithmetic, 0)
        def RightShiftLogical(self):
            return self.getToken(js_grammarParser.RightShiftLogical, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitShiftExpression" ):
                listener.enterBitShiftExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitShiftExpression" ):
                listener.exitBitShiftExpression(self)


    class ParenthesizedExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.exp = None # ExpressionSequenceContext
            self.copyFrom(ctx)

        def OpenParen(self):
            return self.getToken(js_grammarParser.OpenParen, 0)
        def CloseParen(self):
            return self.getToken(js_grammarParser.CloseParen, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)


    class AdditiveExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def Plus(self):
            return self.getToken(js_grammarParser.Plus, 0)
        def Minus(self):
            return self.getToken(js_grammarParser.Minus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)


    class RelationalExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def LessThan(self):
            return self.getToken(js_grammarParser.LessThan, 0)
        def MoreThan(self):
            return self.getToken(js_grammarParser.MoreThan, 0)
        def LessThanEquals(self):
            return self.getToken(js_grammarParser.LessThanEquals, 0)
        def GreaterThanEquals(self):
            return self.getToken(js_grammarParser.GreaterThanEquals, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)


    class PostIncrementExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def PlusPlus(self):
            return self.getToken(js_grammarParser.PlusPlus, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrementExpression" ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrementExpression" ):
                listener.exitPostIncrementExpression(self)


    class BitNotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BitNot(self):
            return self.getToken(js_grammarParser.BitNot, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitNotExpression" ):
                listener.enterBitNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitNotExpression" ):
                listener.exitBitNotExpression(self)


    class NewExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def New(self):
            return self.getToken(js_grammarParser.New, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def arguments(self):
            return self.getTypedRuleContext(js_grammarParser.ArgumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewExpression" ):
                listener.enterNewExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewExpression" ):
                listener.exitNewExpression(self)


    class LiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(js_grammarParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpression" ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpression" ):
                listener.exitLiteralExpression(self)


    class ArrayLiteralExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def arrayLiteral(self):
            return self.getTypedRuleContext(js_grammarParser.ArrayLiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteralExpression" ):
                listener.enterArrayLiteralExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteralExpression" ):
                listener.exitArrayLiteralExpression(self)


    class MemberDotExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def Dot(self):
            return self.getToken(js_grammarParser.Dot, 0)
        def identifierName(self):
            return self.getTypedRuleContext(js_grammarParser.IdentifierNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberDotExpression" ):
                listener.enterMemberDotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberDotExpression" ):
                listener.exitMemberDotExpression(self)


    class MemberIndexExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)

        def OpenBracket(self):
            return self.getToken(js_grammarParser.OpenBracket, 0)
        def expressionSequence(self):
            return self.getTypedRuleContext(js_grammarParser.ExpressionSequenceContext,0)

        def CloseBracket(self):
            return self.getToken(js_grammarParser.CloseBracket, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberIndexExpression" ):
                listener.enterMemberIndexExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberIndexExpression" ):
                listener.exitMemberIndexExpression(self)


    class IdentifierExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)


    class BitAndExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def BitAnd(self):
            return self.getToken(js_grammarParser.BitAnd, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitAndExpression" ):
                listener.enterBitAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitAndExpression" ):
                listener.exitBitAndExpression(self)


    class BitOrExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def BitOr(self):
            return self.getToken(js_grammarParser.BitOr, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitOrExpression" ):
                listener.enterBitOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitOrExpression" ):
                listener.exitBitOrExpression(self)


    class AssignmentOperatorExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def singleExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(js_grammarParser.SingleExpressionContext)
            else:
                return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,i)

        def assignmentOperator(self):
            return self.getTypedRuleContext(js_grammarParser.AssignmentOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperatorExpression" ):
                listener.enterAssignmentOperatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperatorExpression" ):
                listener.exitAssignmentOperatorExpression(self)


    class VoidExpressionContext(SingleExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a js_grammarParser.SingleExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Void(self):
            return self.getToken(js_grammarParser.Void, 0)
        def singleExpression(self):
            return self.getTypedRuleContext(js_grammarParser.SingleExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidExpression" ):
                listener.enterVoidExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidExpression" ):
                listener.exitVoidExpression(self)



    def singleExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = js_grammarParser.SingleExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_singleExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.Function]:
                localctx = js_grammarParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 486
                self.match(js_grammarParser.Function)
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==js_grammarParser.Identifier:
                    self.state = 487
                    self.match(js_grammarParser.Identifier)


                self.state = 490
                self.match(js_grammarParser.OpenParen)
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==js_grammarParser.Identifier:
                    self.state = 491
                    self.formalParameterList()


                self.state = 494
                self.match(js_grammarParser.CloseParen)
                self.state = 495
                self.match(js_grammarParser.OpenBrace)
                self.state = 496
                self.functionBody()
                self.state = 497
                self.match(js_grammarParser.CloseBrace)
                pass
            elif token in [js_grammarParser.New]:
                localctx = js_grammarParser.NewExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 499
                self.match(js_grammarParser.New)
                self.state = 500
                self.singleExpression(0)
                self.state = 502
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 501
                    self.arguments()


                pass
            elif token in [js_grammarParser.Delete]:
                localctx = js_grammarParser.DeleteExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 504
                self.match(js_grammarParser.Delete)
                self.state = 505
                self.singleExpression(30)
                pass
            elif token in [js_grammarParser.Void]:
                localctx = js_grammarParser.VoidExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 506
                self.match(js_grammarParser.Void)
                self.state = 507
                self.singleExpression(29)
                pass
            elif token in [js_grammarParser.Typeof]:
                localctx = js_grammarParser.TypeofExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 508
                self.match(js_grammarParser.Typeof)
                self.state = 509
                self.singleExpression(28)
                pass
            elif token in [js_grammarParser.PlusPlus]:
                localctx = js_grammarParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 510
                self.match(js_grammarParser.PlusPlus)
                self.state = 511
                self.singleExpression(27)
                pass
            elif token in [js_grammarParser.MinusMinus]:
                localctx = js_grammarParser.PreDecreaseExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 512
                self.match(js_grammarParser.MinusMinus)
                self.state = 513
                self.singleExpression(26)
                pass
            elif token in [js_grammarParser.Plus]:
                localctx = js_grammarParser.UnaryPlusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 514
                self.match(js_grammarParser.Plus)
                self.state = 515
                self.singleExpression(25)
                pass
            elif token in [js_grammarParser.Minus]:
                localctx = js_grammarParser.UnaryMinusExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 516
                self.match(js_grammarParser.Minus)
                self.state = 517
                self.singleExpression(24)
                pass
            elif token in [js_grammarParser.BitNot]:
                localctx = js_grammarParser.BitNotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 518
                self.match(js_grammarParser.BitNot)
                self.state = 519
                self.singleExpression(23)
                pass
            elif token in [js_grammarParser.Not]:
                localctx = js_grammarParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 520
                self.match(js_grammarParser.Not)
                self.state = 521
                self.singleExpression(22)
                pass
            elif token in [js_grammarParser.This]:
                localctx = js_grammarParser.ThisExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 522
                self.match(js_grammarParser.This)
                pass
            elif token in [js_grammarParser.Identifier]:
                localctx = js_grammarParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 523
                self.match(js_grammarParser.Identifier)
                pass
            elif token in [js_grammarParser.RegularExpressionLiteral, js_grammarParser.NullLiteral, js_grammarParser.BooleanLiteral, js_grammarParser.DecimalLiteral, js_grammarParser.HexIntegerLiteral, js_grammarParser.StringLiteral, js_grammarParser.OctalIntegerLiteral]:
                localctx = js_grammarParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 524
                self.literal()
                pass
            elif token in [js_grammarParser.OpenBracket]:
                localctx = js_grammarParser.ArrayLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 525
                self.arrayLiteral()
                pass
            elif token in [js_grammarParser.OpenBrace]:
                localctx = js_grammarParser.ObjectLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 526
                self.objectLiteral()
                pass
            elif token in [js_grammarParser.OpenParen]:
                localctx = js_grammarParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 527
                self.match(js_grammarParser.OpenParen)
                self.state = 528
                localctx.exp = self.expressionSequence()
                self.state = 529
                self.match(js_grammarParser.CloseParen)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 598
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
                    if la_ == 1:
                        localctx = js_grammarParser.MultiplicativeExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 533
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 534
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.Multiply) | (1 << js_grammarParser.Divide) | (1 << js_grammarParser.Modulus))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 535
                        self.singleExpression(22)
                        pass

                    elif la_ == 2:
                        localctx = js_grammarParser.AdditiveExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 536
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 537
                        _la = self._input.LA(1)
                        if not(_la==js_grammarParser.Plus or _la==js_grammarParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 538
                        self.singleExpression(21)
                        pass

                    elif la_ == 3:
                        localctx = js_grammarParser.BitShiftExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 539
                        if not self.precpred(self._ctx, 19):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 19)")
                        self.state = 540
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RightShiftArithmetic) | (1 << js_grammarParser.LeftShiftArithmetic) | (1 << js_grammarParser.RightShiftLogical))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 541
                        self.singleExpression(20)
                        pass

                    elif la_ == 4:
                        localctx = js_grammarParser.RelationalExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 542
                        if not self.precpred(self._ctx, 18):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 18)")
                        self.state = 543
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.LessThan) | (1 << js_grammarParser.MoreThan) | (1 << js_grammarParser.LessThanEquals) | (1 << js_grammarParser.GreaterThanEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 544
                        self.singleExpression(19)
                        pass

                    elif la_ == 5:
                        localctx = js_grammarParser.InstanceofExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 545
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 546
                        self.match(js_grammarParser.Instanceof)
                        self.state = 547
                        self.singleExpression(18)
                        pass

                    elif la_ == 6:
                        localctx = js_grammarParser.InExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 548
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 549
                        self.match(js_grammarParser.In)
                        self.state = 550
                        self.singleExpression(17)
                        pass

                    elif la_ == 7:
                        localctx = js_grammarParser.EqualityExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 551
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 552
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.Equals) | (1 << js_grammarParser.NotEquals) | (1 << js_grammarParser.IdentityEquals) | (1 << js_grammarParser.IdentityNotEquals))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 553
                        self.singleExpression(16)
                        pass

                    elif la_ == 8:
                        localctx = js_grammarParser.BitAndExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 554
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 555
                        self.match(js_grammarParser.BitAnd)
                        self.state = 556
                        self.singleExpression(15)
                        pass

                    elif la_ == 9:
                        localctx = js_grammarParser.BitXOrExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 557
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 558
                        self.match(js_grammarParser.BitXOr)
                        self.state = 559
                        self.singleExpression(14)
                        pass

                    elif la_ == 10:
                        localctx = js_grammarParser.BitOrExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 560
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 561
                        self.match(js_grammarParser.BitOr)
                        self.state = 562
                        self.singleExpression(13)
                        pass

                    elif la_ == 11:
                        localctx = js_grammarParser.LogicalAndExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 563
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 564
                        self.match(js_grammarParser.And)
                        self.state = 565
                        self.singleExpression(12)
                        pass

                    elif la_ == 12:
                        localctx = js_grammarParser.LogicalOrExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 566
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 567
                        self.match(js_grammarParser.Or)
                        self.state = 568
                        self.singleExpression(11)
                        pass

                    elif la_ == 13:
                        localctx = js_grammarParser.TernaryExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 569
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 570
                        self.match(js_grammarParser.QuestionMark)
                        self.state = 571
                        self.singleExpression(0)
                        self.state = 572
                        self.match(js_grammarParser.Colon)
                        self.state = 573
                        self.singleExpression(10)
                        pass

                    elif la_ == 14:
                        localctx = js_grammarParser.AssignmentExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 575
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 576
                        self.match(js_grammarParser.Assign)
                        self.state = 577
                        self.singleExpression(9)
                        pass

                    elif la_ == 15:
                        localctx = js_grammarParser.AssignmentOperatorExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 578
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 579
                        self.assignmentOperator()
                        self.state = 580
                        self.singleExpression(8)
                        pass

                    elif la_ == 16:
                        localctx = js_grammarParser.MemberIndexExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 582
                        if not self.precpred(self._ctx, 36):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 36)")
                        self.state = 583
                        self.match(js_grammarParser.OpenBracket)
                        self.state = 584
                        self.expressionSequence()
                        self.state = 585
                        self.match(js_grammarParser.CloseBracket)
                        pass

                    elif la_ == 17:
                        localctx = js_grammarParser.MemberDotExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 587
                        if not self.precpred(self._ctx, 35):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 35)")
                        self.state = 588
                        self.match(js_grammarParser.Dot)
                        self.state = 589
                        self.identifierName()
                        pass

                    elif la_ == 18:
                        localctx = js_grammarParser.ArgumentsExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 590
                        if not self.precpred(self._ctx, 34):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 34)")
                        self.state = 591
                        self.arguments()
                        pass

                    elif la_ == 19:
                        localctx = js_grammarParser.PostIncrementExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 592
                        if not self.precpred(self._ctx, 32):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 32)")
                        self.state = 593
                        if not !here(LineTerminator):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "!here(LineTerminator)")
                        self.state = 594
                        self.match(js_grammarParser.PlusPlus)
                        pass

                    elif la_ == 20:
                        localctx = js_grammarParser.PostDecreaseExpressionContext(self, js_grammarParser.SingleExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_singleExpression)
                        self.state = 595
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 596
                        if not !here(LineTerminator):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "!here(LineTerminator)")
                        self.state = 597
                        self.match(js_grammarParser.MinusMinus)
                        pass

             
                self.state = 602
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MultiplyAssign(self):
            return self.getToken(js_grammarParser.MultiplyAssign, 0)

        def DivideAssign(self):
            return self.getToken(js_grammarParser.DivideAssign, 0)

        def ModulusAssign(self):
            return self.getToken(js_grammarParser.ModulusAssign, 0)

        def PlusAssign(self):
            return self.getToken(js_grammarParser.PlusAssign, 0)

        def MinusAssign(self):
            return self.getToken(js_grammarParser.MinusAssign, 0)

        def LeftShiftArithmeticAssign(self):
            return self.getToken(js_grammarParser.LeftShiftArithmeticAssign, 0)

        def RightShiftArithmeticAssign(self):
            return self.getToken(js_grammarParser.RightShiftArithmeticAssign, 0)

        def RightShiftLogicalAssign(self):
            return self.getToken(js_grammarParser.RightShiftLogicalAssign, 0)

        def BitAndAssign(self):
            return self.getToken(js_grammarParser.BitAndAssign, 0)

        def BitXorAssign(self):
            return self.getToken(js_grammarParser.BitXorAssign, 0)

        def BitOrAssign(self):
            return self.getToken(js_grammarParser.BitOrAssign, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)




    def assignmentOperator(self):

        localctx = js_grammarParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 603
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.MultiplyAssign) | (1 << js_grammarParser.DivideAssign) | (1 << js_grammarParser.ModulusAssign) | (1 << js_grammarParser.PlusAssign) | (1 << js_grammarParser.MinusAssign) | (1 << js_grammarParser.LeftShiftArithmeticAssign) | (1 << js_grammarParser.RightShiftArithmeticAssign) | (1 << js_grammarParser.RightShiftLogicalAssign) | (1 << js_grammarParser.BitAndAssign) | (1 << js_grammarParser.BitXorAssign) | (1 << js_grammarParser.BitOrAssign))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NullLiteral(self):
            return self.getToken(js_grammarParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(js_grammarParser.BooleanLiteral, 0)

        def StringLiteral(self):
            return self.getToken(js_grammarParser.StringLiteral, 0)

        def RegularExpressionLiteral(self):
            return self.getToken(js_grammarParser.RegularExpressionLiteral, 0)

        def numericLiteral(self):
            return self.getTypedRuleContext(js_grammarParser.NumericLiteralContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = js_grammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 607
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.RegularExpressionLiteral, js_grammarParser.NullLiteral, js_grammarParser.BooleanLiteral, js_grammarParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << js_grammarParser.RegularExpressionLiteral) | (1 << js_grammarParser.NullLiteral) | (1 << js_grammarParser.BooleanLiteral))) != 0) or _la==js_grammarParser.StringLiteral):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [js_grammarParser.DecimalLiteral, js_grammarParser.HexIntegerLiteral, js_grammarParser.OctalIntegerLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.numericLiteral()
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


    class NumericLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(js_grammarParser.DecimalLiteral, 0)

        def HexIntegerLiteral(self):
            return self.getToken(js_grammarParser.HexIntegerLiteral, 0)

        def OctalIntegerLiteral(self):
            return self.getToken(js_grammarParser.OctalIntegerLiteral, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_numericLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericLiteral" ):
                listener.enterNumericLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericLiteral" ):
                listener.exitNumericLiteral(self)




    def numericLiteral(self):

        localctx = js_grammarParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (js_grammarParser.DecimalLiteral - 53)) | (1 << (js_grammarParser.HexIntegerLiteral - 53)) | (1 << (js_grammarParser.OctalIntegerLiteral - 53)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def reservedWord(self):
            return self.getTypedRuleContext(js_grammarParser.ReservedWordContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_identifierName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierName" ):
                listener.enterIdentifierName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierName" ):
                listener.exitIdentifierName(self)




    def identifierName(self):

        localctx = js_grammarParser.IdentifierNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_identifierName)
        try:
            self.state = 613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 611
                self.match(js_grammarParser.Identifier)
                pass
            elif token in [js_grammarParser.NullLiteral, js_grammarParser.BooleanLiteral, js_grammarParser.Break, js_grammarParser.Do, js_grammarParser.Instanceof, js_grammarParser.Typeof, js_grammarParser.Case, js_grammarParser.Else, js_grammarParser.New, js_grammarParser.Var, js_grammarParser.Let, js_grammarParser.Catch, js_grammarParser.Finally, js_grammarParser.Return, js_grammarParser.Void, js_grammarParser.Continue, js_grammarParser.For, js_grammarParser.Switch, js_grammarParser.While, js_grammarParser.Debugger, js_grammarParser.Function, js_grammarParser.This, js_grammarParser.With, js_grammarParser.Default, js_grammarParser.If, js_grammarParser.Throw, js_grammarParser.Delete, js_grammarParser.In, js_grammarParser.Try, js_grammarParser.Class, js_grammarParser.Enum, js_grammarParser.Extends, js_grammarParser.Super, js_grammarParser.Const, js_grammarParser.Export, js_grammarParser.Import, js_grammarParser.Implements, js_grammarParser.Private, js_grammarParser.Public, js_grammarParser.Interface, js_grammarParser.Package, js_grammarParser.Protected, js_grammarParser.Static, js_grammarParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 612
                self.reservedWord()
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


    class ReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(js_grammarParser.KeywordContext,0)


        def futureReservedWord(self):
            return self.getTypedRuleContext(js_grammarParser.FutureReservedWordContext,0)


        def NullLiteral(self):
            return self.getToken(js_grammarParser.NullLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(js_grammarParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_reservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReservedWord" ):
                listener.enterReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReservedWord" ):
                listener.exitReservedWord(self)




    def reservedWord(self):

        localctx = js_grammarParser.ReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_reservedWord)
        self._la = 0 # Token type
        try:
            self.state = 618
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [js_grammarParser.Break, js_grammarParser.Do, js_grammarParser.Instanceof, js_grammarParser.Typeof, js_grammarParser.Case, js_grammarParser.Else, js_grammarParser.New, js_grammarParser.Var, js_grammarParser.Let, js_grammarParser.Catch, js_grammarParser.Finally, js_grammarParser.Return, js_grammarParser.Void, js_grammarParser.Continue, js_grammarParser.For, js_grammarParser.Switch, js_grammarParser.While, js_grammarParser.Debugger, js_grammarParser.Function, js_grammarParser.This, js_grammarParser.With, js_grammarParser.Default, js_grammarParser.If, js_grammarParser.Throw, js_grammarParser.Delete, js_grammarParser.In, js_grammarParser.Try]:
                self.enterOuterAlt(localctx, 1)
                self.state = 615
                self.keyword()
                pass
            elif token in [js_grammarParser.Class, js_grammarParser.Enum, js_grammarParser.Extends, js_grammarParser.Super, js_grammarParser.Const, js_grammarParser.Export, js_grammarParser.Import, js_grammarParser.Implements, js_grammarParser.Private, js_grammarParser.Public, js_grammarParser.Interface, js_grammarParser.Package, js_grammarParser.Protected, js_grammarParser.Static, js_grammarParser.Yield]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.futureReservedWord()
                pass
            elif token in [js_grammarParser.NullLiteral, js_grammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 617
                _la = self._input.LA(1)
                if not(_la==js_grammarParser.NullLiteral or _la==js_grammarParser.BooleanLiteral):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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


    class KeywordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Break(self):
            return self.getToken(js_grammarParser.Break, 0)

        def Do(self):
            return self.getToken(js_grammarParser.Do, 0)

        def Instanceof(self):
            return self.getToken(js_grammarParser.Instanceof, 0)

        def Typeof(self):
            return self.getToken(js_grammarParser.Typeof, 0)

        def Case(self):
            return self.getToken(js_grammarParser.Case, 0)

        def Else(self):
            return self.getToken(js_grammarParser.Else, 0)

        def New(self):
            return self.getToken(js_grammarParser.New, 0)

        def Var(self):
            return self.getToken(js_grammarParser.Var, 0)

        def Catch(self):
            return self.getToken(js_grammarParser.Catch, 0)

        def Finally(self):
            return self.getToken(js_grammarParser.Finally, 0)

        def Return(self):
            return self.getToken(js_grammarParser.Return, 0)

        def Void(self):
            return self.getToken(js_grammarParser.Void, 0)

        def Continue(self):
            return self.getToken(js_grammarParser.Continue, 0)

        def For(self):
            return self.getToken(js_grammarParser.For, 0)

        def Switch(self):
            return self.getToken(js_grammarParser.Switch, 0)

        def While(self):
            return self.getToken(js_grammarParser.While, 0)

        def Debugger(self):
            return self.getToken(js_grammarParser.Debugger, 0)

        def Function(self):
            return self.getToken(js_grammarParser.Function, 0)

        def This(self):
            return self.getToken(js_grammarParser.This, 0)

        def With(self):
            return self.getToken(js_grammarParser.With, 0)

        def Default(self):
            return self.getToken(js_grammarParser.Default, 0)

        def If(self):
            return self.getToken(js_grammarParser.If, 0)

        def Throw(self):
            return self.getToken(js_grammarParser.Throw, 0)

        def Delete(self):
            return self.getToken(js_grammarParser.Delete, 0)

        def In(self):
            return self.getToken(js_grammarParser.In, 0)

        def Try(self):
            return self.getToken(js_grammarParser.Try, 0)

        def Let(self):
            return self.getToken(js_grammarParser.Let, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)




    def keyword(self):

        localctx = js_grammarParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 620
            _la = self._input.LA(1)
            if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & ((1 << (js_grammarParser.Break - 55)) | (1 << (js_grammarParser.Do - 55)) | (1 << (js_grammarParser.Instanceof - 55)) | (1 << (js_grammarParser.Typeof - 55)) | (1 << (js_grammarParser.Case - 55)) | (1 << (js_grammarParser.Else - 55)) | (1 << (js_grammarParser.New - 55)) | (1 << (js_grammarParser.Var - 55)) | (1 << (js_grammarParser.Let - 55)) | (1 << (js_grammarParser.Catch - 55)) | (1 << (js_grammarParser.Finally - 55)) | (1 << (js_grammarParser.Return - 55)) | (1 << (js_grammarParser.Void - 55)) | (1 << (js_grammarParser.Continue - 55)) | (1 << (js_grammarParser.For - 55)) | (1 << (js_grammarParser.Switch - 55)) | (1 << (js_grammarParser.While - 55)) | (1 << (js_grammarParser.Debugger - 55)) | (1 << (js_grammarParser.Function - 55)) | (1 << (js_grammarParser.This - 55)) | (1 << (js_grammarParser.With - 55)) | (1 << (js_grammarParser.Default - 55)) | (1 << (js_grammarParser.If - 55)) | (1 << (js_grammarParser.Throw - 55)) | (1 << (js_grammarParser.Delete - 55)) | (1 << (js_grammarParser.In - 55)) | (1 << (js_grammarParser.Try - 55)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FutureReservedWordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Class(self):
            return self.getToken(js_grammarParser.Class, 0)

        def Enum(self):
            return self.getToken(js_grammarParser.Enum, 0)

        def Extends(self):
            return self.getToken(js_grammarParser.Extends, 0)

        def Super(self):
            return self.getToken(js_grammarParser.Super, 0)

        def Const(self):
            return self.getToken(js_grammarParser.Const, 0)

        def Export(self):
            return self.getToken(js_grammarParser.Export, 0)

        def Import(self):
            return self.getToken(js_grammarParser.Import, 0)

        def Implements(self):
            return self.getToken(js_grammarParser.Implements, 0)

        def Private(self):
            return self.getToken(js_grammarParser.Private, 0)

        def Public(self):
            return self.getToken(js_grammarParser.Public, 0)

        def Interface(self):
            return self.getToken(js_grammarParser.Interface, 0)

        def Package(self):
            return self.getToken(js_grammarParser.Package, 0)

        def Protected(self):
            return self.getToken(js_grammarParser.Protected, 0)

        def Static(self):
            return self.getToken(js_grammarParser.Static, 0)

        def Yield(self):
            return self.getToken(js_grammarParser.Yield, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_futureReservedWord

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFutureReservedWord" ):
                listener.enterFutureReservedWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFutureReservedWord" ):
                listener.exitFutureReservedWord(self)




    def futureReservedWord(self):

        localctx = js_grammarParser.FutureReservedWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_futureReservedWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            _la = self._input.LA(1)
            if not(((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (js_grammarParser.Class - 82)) | (1 << (js_grammarParser.Enum - 82)) | (1 << (js_grammarParser.Extends - 82)) | (1 << (js_grammarParser.Super - 82)) | (1 << (js_grammarParser.Const - 82)) | (1 << (js_grammarParser.Export - 82)) | (1 << (js_grammarParser.Import - 82)) | (1 << (js_grammarParser.Implements - 82)) | (1 << (js_grammarParser.Private - 82)) | (1 << (js_grammarParser.Public - 82)) | (1 << (js_grammarParser.Interface - 82)) | (1 << (js_grammarParser.Package - 82)) | (1 << (js_grammarParser.Protected - 82)) | (1 << (js_grammarParser.Static - 82)) | (1 << (js_grammarParser.Yield - 82)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(js_grammarParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_getter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetter" ):
                listener.enterGetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetter" ):
                listener.exitGetter(self)




    def getter(self):

        localctx = js_grammarParser.GetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_getter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            if not _input.LT(1).Text.Equals("get"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "_input.LT(1).Text.Equals(\"get\")")
            self.state = 625
            self.match(js_grammarParser.Identifier)
            self.state = 626
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(js_grammarParser.Identifier, 0)

        def propertyName(self):
            return self.getTypedRuleContext(js_grammarParser.PropertyNameContext,0)


        def getRuleIndex(self):
            return js_grammarParser.RULE_setter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetter" ):
                listener.enterSetter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetter" ):
                listener.exitSetter(self)




    def setter(self):

        localctx = js_grammarParser.SetterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_setter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            if not _input.LT(1).Text.Equals("set"):
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, "_input.LT(1).Text.Equals(\"set\")")
            self.state = 629
            self.match(js_grammarParser.Identifier)
            self.state = 630
            self.propertyName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SemiColon(self):
            return self.getToken(js_grammarParser.SemiColon, 0)

        def EOF(self):
            return self.getToken(js_grammarParser.EOF, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_eos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEos" ):
                listener.enterEos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEos" ):
                listener.exitEos(self)




    def eos(self):

        localctx = js_grammarParser.EosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_eos)
        try:
            self.state = 636
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 632
                self.match(js_grammarParser.SemiColon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
                self.match(js_grammarParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 634
                if not lineTerminatorAhead():
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "lineTerminatorAhead()")
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 635
                if not _input.LT(1).Type == CloseBrace:
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "_input.LT(1).Type == CloseBrace")
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EofContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(js_grammarParser.EOF, 0)

        def getRuleIndex(self):
            return js_grammarParser.RULE_eof

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEof" ):
                listener.enterEof(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEof" ):
                listener.exitEof(self)




    def eof(self):

        localctx = js_grammarParser.EofContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_eof)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            self.match(js_grammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.continueStatement_sempred
        self._predicates[15] = self.breakStatement_sempred
        self._predicates[16] = self.returnStatement_sempred
        self._predicates[24] = self.throwStatement_sempred
        self._predicates[44] = self.singleExpression_sempred
        self._predicates[52] = self.getter_sempred
        self._predicates[53] = self.setter_sempred
        self._predicates[54] = self.eos_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def continueStatement_sempred(self, localctx:ContinueStatementContext, predIndex:int):
            if predIndex == 0:
                return !here(LineTerminator)
         

    def breakStatement_sempred(self, localctx:BreakStatementContext, predIndex:int):
            if predIndex == 1:
                return !here(LineTerminator)
         

    def returnStatement_sempred(self, localctx:ReturnStatementContext, predIndex:int):
            if predIndex == 2:
                return !here(LineTerminator)
         

    def throwStatement_sempred(self, localctx:ThrowStatementContext, predIndex:int):
            if predIndex == 3:
                return !here(LineTerminator)
         

    def singleExpression_sempred(self, localctx:SingleExpressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 19)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 18)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 36)
         

            if predIndex == 20:
                return self.precpred(self._ctx, 35)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 34)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 32)
         

            if predIndex == 23:
                return !here(LineTerminator)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 25:
                return !here(LineTerminator)
         

    def getter_sempred(self, localctx:GetterContext, predIndex:int):
            if predIndex == 26:
                return _input.LT(1).Text.Equals("get")
         

    def setter_sempred(self, localctx:SetterContext, predIndex:int):
            if predIndex == 27:
                return _input.LT(1).Text.Equals("set")
         

    def eos_sempred(self, localctx:EosContext, predIndex:int):
            if predIndex == 28:
                return lineTerminatorAhead()
         

            if predIndex == 29:
                return _input.LT(1).Type == CloseBrace
         




