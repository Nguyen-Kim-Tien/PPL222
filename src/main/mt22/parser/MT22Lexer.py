# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5\13\u0101\n")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u0109\n\f\f\f\16\f\u010c")
        buf.write("\13\f\3\r\3\r\3\r\3\r\7\r\u0112\n\r\f\r\16\r\u0115\13")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u011d\n\16\f\16\16")
        buf.write("\16\u0120\13\16\3\16\3\16\6\16\u0124\n\16\r\16\16\16\u0125")
        buf.write("\7\16\u0128\n\16\f\16\16\16\u012b\13\16\3\16\5\16\u012e")
        buf.write("\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u013d\n\17\3\17\3\17\3\20\3\20\7")
        buf.write("\20\u0143\n\20\f\20\16\20\u0146\13\20\3\21\3\21\5\21\u014a")
        buf.write("\n\21\3\21\6\21\u014d\n\21\r\21\16\21\u014e\3\22\3\22")
        buf.write("\5\22\u0153\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\25\3\25\3\25\7\25\u0163\n\25\f\25")
        buf.write("\16\25\u0166\13\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+")
        buf.write("\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3F\3F\3G\6G\u0221\nG\rG\16G\u0222")
        buf.write("\3G\7G\u0226\nG\fG\16G\u0229\13G\3H\6H\u022c\nH\rH\16")
        buf.write("H\u022d\3H\3H\3I\3I\3I\7I\u0235\nI\fI\16I\u0238\13I\3")
        buf.write("I\5I\u023b\nI\3I\3I\3J\3J\3J\7J\u0242\nJ\fJ\16J\u0245")
        buf.write("\13J\3J\3J\3J\3K\3K\3K\4\u0113\u0236\2L\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\2\31\2\33\r\35\16")
        buf.write("\37\2!\2#\17%\2\'\2)\20+\2-\2/\2\61\2\63\21\65\22\67\23")
        buf.write("9\24;\25=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37Q S!U")
        buf.write("\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64{\65")
        buf.write("}\66\177\67\u00818\u00839\u0085:\u0087;\u0089<\u008b=")
        buf.write("\u008d>\u008f?\u0091@\u0093A\u0095B\3\2\20\4\2\f\f\17")
        buf.write("\17\3\2\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f\17\17$$\n")
        buf.write("\2$$))^^ddhhppttvv\3\2$$\3\2))\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\13\f\17\17\"\"\4\3\f\f\17\17\4\2$$^^\2\u0258\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2#\3\2\2\2")
        buf.write("\2)\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u0097\3\2\2\2\5\u00a3")
        buf.write("\3\2\2\2\7\u00b0\3\2\2\2\t\u00ba\3\2\2\2\13\u00c5\3\2")
        buf.write("\2\2\r\u00d2\3\2\2\2\17\u00dd\3\2\2\2\21\u00e9\3\2\2\2")
        buf.write("\23\u00ef\3\2\2\2\25\u0100\3\2\2\2\27\u0104\3\2\2\2\31")
        buf.write("\u010d\3\2\2\2\33\u012d\3\2\2\2\35\u013c\3\2\2\2\37\u0140")
        buf.write("\3\2\2\2!\u0147\3\2\2\2#\u0152\3\2\2\2%\u0154\3\2\2\2")
        buf.write("\'\u015a\3\2\2\2)\u015f\3\2\2\2+\u016a\3\2\2\2-\u016d")
        buf.write("\3\2\2\2/\u0170\3\2\2\2\61\u0172\3\2\2\2\63\u0174\3\2")
        buf.write("\2\2\65\u0179\3\2\2\2\67\u017f\3\2\2\29\u0187\3\2\2\2")
        buf.write(";\u018c\3\2\2\2=\u0192\3\2\2\2?\u0198\3\2\2\2A\u019f\3")
        buf.write("\2\2\2C\u01a3\3\2\2\2E\u01ab\3\2\2\2G\u01af\3\2\2\2I\u01b6")
        buf.write("\3\2\2\2K\u01bf\3\2\2\2M\u01c2\3\2\2\2O\u01cb\3\2\2\2")
        buf.write("Q\u01ce\3\2\2\2S\u01d3\3\2\2\2U\u01d6\3\2\2\2W\u01dc\3")
        buf.write("\2\2\2Y\u01e4\3\2\2\2[\u01e6\3\2\2\2]\u01e8\3\2\2\2_\u01ea")
        buf.write("\3\2\2\2a\u01ec\3\2\2\2c\u01ee\3\2\2\2e\u01f0\3\2\2\2")
        buf.write("g\u01f2\3\2\2\2i\u01f5\3\2\2\2k\u01f8\3\2\2\2m\u01fa\3")
        buf.write("\2\2\2o\u01fd\3\2\2\2q\u0200\3\2\2\2s\u0203\3\2\2\2u\u0206")
        buf.write("\3\2\2\2w\u0209\3\2\2\2y\u020b\3\2\2\2{\u020d\3\2\2\2")
        buf.write("}\u020f\3\2\2\2\177\u0211\3\2\2\2\u0081\u0213\3\2\2\2")
        buf.write("\u0083\u0215\3\2\2\2\u0085\u0217\3\2\2\2\u0087\u0219\3")
        buf.write("\2\2\2\u0089\u021b\3\2\2\2\u008b\u021d\3\2\2\2\u008d\u0220")
        buf.write("\3\2\2\2\u008f\u022b\3\2\2\2\u0091\u0231\3\2\2\2\u0093")
        buf.write("\u023e\3\2\2\2\u0095\u0249\3\2\2\2\u0097\u0098\7t\2\2")
        buf.write("\u0098\u0099\7g\2\2\u0099\u009a\7c\2\2\u009a\u009b\7f")
        buf.write("\2\2\u009b\u009c\7K\2\2\u009c\u009d\7p\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7i\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\u00a2\7t\2\2\u00a2\4\3\2\2\2\u00a3\u00a4")
        buf.write("\7r\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9\7K\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write("\7i\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7t\2\2\u00af\6")
        buf.write("\3\2\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7f\2\2\u00b4\u00b5\7H\2\2\u00b5\u00b6")
        buf.write("\7n\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7c\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\b\3\2\2\2\u00ba\u00bb\7y\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7v\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\u00c0\7H\2\2\u00c0\u00c1\7n\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7v\2\2\u00c4\n")
        buf.write("\3\2\2\2\u00c5\u00c6\7r\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb")
        buf.write("\7D\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\f\3\2\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7")
        buf.write("\7U\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7i\2\2\u00dc\16")
        buf.write("\3\2\2\2\u00dd\u00de\7r\2\2\u00de\u00df\7t\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3")
        buf.write("\7U\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7i\2\2\u00e8\20")
        buf.write("\3\2\2\2\u00e9\u00ea\7u\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec")
        buf.write("\7r\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7t\2\2\u00ee\22")
        buf.write("\3\2\2\2\u00ef\u00f0\7r\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f3\7x\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7p\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7\7F\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8\u00f9\7h\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7v\2\2\u00fd\24")
        buf.write("\3\2\2\2\u00fe\u0101\5\27\f\2\u00ff\u0101\5\31\r\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0103\b\13\2\2\u0103\26\3\2\2\2\u0104\u0105\7\61")
        buf.write("\2\2\u0105\u0106\7\61\2\2\u0106\u010a\3\2\2\2\u0107\u0109")
        buf.write("\n\2\2\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\30\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010d\u010e\7\61\2\2\u010e\u010f\7,\2\2")
        buf.write("\u010f\u0113\3\2\2\2\u0110\u0112\13\2\2\2\u0111\u0110")
        buf.write("\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0114\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u0113\3\2\2\2")
        buf.write("\u0116\u0117\7,\2\2\u0117\u0118\7\61\2\2\u0118\32\3\2")
        buf.write("\2\2\u0119\u012e\7\62\2\2\u011a\u011e\t\3\2\2\u011b\u011d")
        buf.write("\t\4\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0129\3\2\2\2")
        buf.write("\u0120\u011e\3\2\2\2\u0121\u0123\7a\2\2\u0122\u0124\t")
        buf.write("\4\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0123")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0121\3\2\2\2\u0128\u012b\3\2\2\2\u0129\u0127\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2\u012b\u0129\3")
        buf.write("\2\2\2\u012c\u012e\b\16\3\2\u012d\u0119\3\2\2\2\u012d")
        buf.write("\u011a\3\2\2\2\u012e\34\3\2\2\2\u012f\u0130\5\33\16\2")
        buf.write("\u0130\u0131\5\37\20\2\u0131\u0132\5!\21\2\u0132\u013d")
        buf.write("\3\2\2\2\u0133\u0134\5\33\16\2\u0134\u0135\5\37\20\2\u0135")
        buf.write("\u013d\3\2\2\2\u0136\u0137\5\33\16\2\u0137\u0138\5!\21")
        buf.write("\2\u0138\u013d\3\2\2\2\u0139\u013a\5\37\20\2\u013a\u013b")
        buf.write("\5!\21\2\u013b\u013d\3\2\2\2\u013c\u012f\3\2\2\2\u013c")
        buf.write("\u0133\3\2\2\2\u013c\u0136\3\2\2\2\u013c\u0139\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\b\17\4\2\u013f\36\3\2")
        buf.write("\2\2\u0140\u0144\5w<\2\u0141\u0143\t\4\2\2\u0142\u0141")
        buf.write("\3\2\2\2\u0143\u0146\3\2\2\2\u0144\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145 \3\2\2\2\u0146\u0144\3\2\2\2\u0147")
        buf.write("\u0149\t\5\2\2\u0148\u014a\t\6\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014c\3\2\2\2\u014b\u014d\t")
        buf.write("\4\2\2\u014c\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\"\3\2\2\2\u0150\u0153")
        buf.write("\5%\23\2\u0151\u0153\5\'\24\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0151\3\2\2\2\u0153$\3\2\2\2\u0154\u0155\7h\2\2\u0155")
        buf.write("\u0156\7c\2\2\u0156\u0157\7n\2\2\u0157\u0158\7u\2\2\u0158")
        buf.write("\u0159\7g\2\2\u0159&\3\2\2\2\u015a\u015b\7v\2\2\u015b")
        buf.write("\u015c\7t\2\2\u015c\u015d\7w\2\2\u015d\u015e\7g\2\2\u015e")
        buf.write("(\3\2\2\2\u015f\u0164\5/\30\2\u0160\u0163\5-\27\2\u0161")
        buf.write("\u0163\n\7\2\2\u0162\u0160\3\2\2\2\u0162\u0161\3\2\2\2")
        buf.write("\u0163\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0168")
        buf.write("\5/\30\2\u0168\u0169\b\25\5\2\u0169*\3\2\2\2\u016a\u016b")
        buf.write("\7^\2\2\u016b\u016c\n\b\2\2\u016c,\3\2\2\2\u016d\u016e")
        buf.write("\7^\2\2\u016e\u016f\t\b\2\2\u016f.\3\2\2\2\u0170\u0171")
        buf.write("\t\t\2\2\u0171\60\3\2\2\2\u0172\u0173\t\n\2\2\u0173\62")
        buf.write("\3\2\2\2\u0174\u0175\7c\2\2\u0175\u0176\7w\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177\u0178\7q\2\2\u0178\64\3\2\2\2\u0179\u017a")
        buf.write("\7d\2\2\u017a\u017b\7t\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7c\2\2\u017d\u017e\7m\2\2\u017e\66\3\2\2\2\u017f\u0180")
        buf.write("\7k\2\2\u0180\u0181\7p\2\2\u0181\u0182\7v\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7i\2\2\u0184\u0185\7g\2\2\u0185\u0186")
        buf.write("\7t\2\2\u01868\3\2\2\2\u0187\u0188\7x\2\2\u0188\u0189")
        buf.write("\7q\2\2\u0189\u018a\7k\2\2\u018a\u018b\7f\2\2\u018b:\3")
        buf.write("\2\2\2\u018c\u018d\7c\2\2\u018d\u018e\7t\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018f\u0190\7c\2\2\u0190\u0191\7{\2\2\u0191<\3")
        buf.write("\2\2\2\u0192\u0193\7h\2\2\u0193\u0194\7n\2\2\u0194\u0195")
        buf.write("\7q\2\2\u0195\u0196\7c\2\2\u0196\u0197\7v\2\2\u0197>\3")
        buf.write("\2\2\2\u0198\u0199\7t\2\2\u0199\u019a\7g\2\2\u019a\u019b")
        buf.write("\7v\2\2\u019b\u019c\7w\2\2\u019c\u019d\7t\2\2\u019d\u019e")
        buf.write("\7p\2\2\u019e@\3\2\2\2\u019f\u01a0\7q\2\2\u01a0\u01a1")
        buf.write("\7w\2\2\u01a1\u01a2\7v\2\2\u01a2B\3\2\2\2\u01a3\u01a4")
        buf.write("\7d\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7")
        buf.write("\7n\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa")
        buf.write("\7p\2\2\u01aaD\3\2\2\2\u01ab\u01ac\7h\2\2\u01ac\u01ad")
        buf.write("\7q\2\2\u01ad\u01ae\7t\2\2\u01aeF\3\2\2\2\u01af\u01b0")
        buf.write("\7u\2\2\u01b0\u01b1\7v\2\2\u01b1\u01b2\7t\2\2\u01b2\u01b3")
        buf.write("\7k\2\2\u01b3\u01b4\7p\2\2\u01b4\u01b5\7i\2\2\u01b5H\3")
        buf.write("\2\2\2\u01b6\u01b7\7e\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9")
        buf.write("\7p\2\2\u01b9\u01ba\7v\2\2\u01ba\u01bb\7k\2\2\u01bb\u01bc")
        buf.write("\7p\2\2\u01bc\u01bd\7w\2\2\u01bd\u01be\7g\2\2\u01beJ\3")
        buf.write("\2\2\2\u01bf\u01c0\7f\2\2\u01c0\u01c1\7q\2\2\u01c1L\3")
        buf.write("\2\2\2\u01c2\u01c3\7h\2\2\u01c3\u01c4\7w\2\2\u01c4\u01c5")
        buf.write("\7p\2\2\u01c5\u01c6\7e\2\2\u01c6\u01c7\7v\2\2\u01c7\u01c8")
        buf.write("\7k\2\2\u01c8\u01c9\7q\2\2\u01c9\u01ca\7p\2\2\u01caN\3")
        buf.write("\2\2\2\u01cb\u01cc\7q\2\2\u01cc\u01cd\7h\2\2\u01cdP\3")
        buf.write("\2\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1")
        buf.write("\7u\2\2\u01d1\u01d2\7g\2\2\u01d2R\3\2\2\2\u01d3\u01d4")
        buf.write("\7k\2\2\u01d4\u01d5\7h\2\2\u01d5T\3\2\2\2\u01d6\u01d7")
        buf.write("\7y\2\2\u01d7\u01d8\7j\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da")
        buf.write("\7n\2\2\u01da\u01db\7g\2\2\u01dbV\3\2\2\2\u01dc\u01dd")
        buf.write("\7k\2\2\u01dd\u01de\7p\2\2\u01de\u01df\7j\2\2\u01df\u01e0")
        buf.write("\7g\2\2\u01e0\u01e1\7t\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3")
        buf.write("\7v\2\2\u01e3X\3\2\2\2\u01e4\u01e5\7-\2\2\u01e5Z\3\2\2")
        buf.write("\2\u01e6\u01e7\7/\2\2\u01e7\\\3\2\2\2\u01e8\u01e9\7,\2")
        buf.write("\2\u01e9^\3\2\2\2\u01ea\u01eb\7\61\2\2\u01eb`\3\2\2\2")
        buf.write("\u01ec\u01ed\7\'\2\2\u01edb\3\2\2\2\u01ee\u01ef\7>\2\2")
        buf.write("\u01efd\3\2\2\2\u01f0\u01f1\7@\2\2\u01f1f\3\2\2\2\u01f2")
        buf.write("\u01f3\7>\2\2\u01f3\u01f4\7?\2\2\u01f4h\3\2\2\2\u01f5")
        buf.write("\u01f6\7@\2\2\u01f6\u01f7\7?\2\2\u01f7j\3\2\2\2\u01f8")
        buf.write("\u01f9\7#\2\2\u01f9l\3\2\2\2\u01fa\u01fb\7(\2\2\u01fb")
        buf.write("\u01fc\7(\2\2\u01fcn\3\2\2\2\u01fd\u01fe\7~\2\2\u01fe")
        buf.write("\u01ff\7~\2\2\u01ffp\3\2\2\2\u0200\u0201\7?\2\2\u0201")
        buf.write("\u0202\7?\2\2\u0202r\3\2\2\2\u0203\u0204\7#\2\2\u0204")
        buf.write("\u0205\7?\2\2\u0205t\3\2\2\2\u0206\u0207\7<\2\2\u0207")
        buf.write("\u0208\7<\2\2\u0208v\3\2\2\2\u0209\u020a\7\60\2\2\u020a")
        buf.write("x\3\2\2\2\u020b\u020c\7.\2\2\u020cz\3\2\2\2\u020d\u020e")
        buf.write("\7=\2\2\u020e|\3\2\2\2\u020f\u0210\7?\2\2\u0210~\3\2\2")
        buf.write("\2\u0211\u0212\7<\2\2\u0212\u0080\3\2\2\2\u0213\u0214")
        buf.write("\7*\2\2\u0214\u0082\3\2\2\2\u0215\u0216\7+\2\2\u0216\u0084")
        buf.write("\3\2\2\2\u0217\u0218\7]\2\2\u0218\u0086\3\2\2\2\u0219")
        buf.write("\u021a\7_\2\2\u021a\u0088\3\2\2\2\u021b\u021c\7}\2\2\u021c")
        buf.write("\u008a\3\2\2\2\u021d\u021e\7\177\2\2\u021e\u008c\3\2\2")
        buf.write("\2\u021f\u0221\t\13\2\2\u0220\u021f\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223")
        buf.write("\u0227\3\2\2\2\u0224\u0226\t\f\2\2\u0225\u0224\3\2\2\2")
        buf.write("\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3")
        buf.write("\2\2\2\u0228\u008e\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022c")
        buf.write("\t\r\2\2\u022b\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u0230\bH\2\2\u0230\u0090\3\2\2\2\u0231\u0236\5")
        buf.write("/\30\2\u0232\u0235\n\t\2\2\u0233\u0235\5-\27\2\u0234\u0232")
        buf.write("\3\2\2\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u023a\3\2\2\2")
        buf.write("\u0238\u0236\3\2\2\2\u0239\u023b\t\16\2\2\u023a\u0239")
        buf.write("\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023d\bI\6\2\u023d")
        buf.write("\u0092\3\2\2\2\u023e\u0243\5/\30\2\u023f\u0242\n\17\2")
        buf.write("\2\u0240\u0242\5-\27\2\u0241\u023f\3\2\2\2\u0241\u0240")
        buf.write("\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243")
        buf.write("\u0244\3\2\2\2\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0246\u0247\5+\26\2\u0247\u0248\bJ\7\2\u0248\u0094\3")
        buf.write("\2\2\2\u0249\u024a\13\2\2\2\u024a\u024b\bK\b\2\u024b\u0096")
        buf.write("\3\2\2\2\31\2\u0100\u010a\u0113\u011e\u0125\u0129\u012d")
        buf.write("\u013c\u0144\u0149\u014e\u0152\u0162\u0164\u0222\u0227")
        buf.write("\u022d\u0234\u0236\u023a\u0241\u0243\t\b\2\2\3\16\2\3")
        buf.write("\17\3\3\25\4\3I\5\3J\6\3K\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    READINTEGER = 1
    PRINTINTEGER = 2
    READFLOAT = 3
    WRITEFLOAT = 4
    PRINTBOOLEAN = 5
    READSTRING = 6
    PRINTSTRING = 7
    SUPER = 8
    PREVENTDEFAULT = 9
    COMMENT = 10
    INTLIT = 11
    FLOATLIT = 12
    BOOLEANLIT = 13
    STRINGLIT = 14
    AUTO = 15
    BREAK = 16
    INTEGER = 17
    VOID = 18
    ARRAY = 19
    FLOAT = 20
    RETURN = 21
    OUT = 22
    BOOLEAN = 23
    FOR = 24
    STRING = 25
    CONTINUE = 26
    DO = 27
    FUNCTION = 28
    OF = 29
    ELSE = 30
    IF = 31
    WHILE = 32
    INHERIT = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    MOD = 38
    LESS = 39
    GT = 40
    LTE = 41
    GTE = 42
    NOT = 43
    AND = 44
    OR = 45
    EQ = 46
    NOT_EQ = 47
    CONCAT = 48
    DOT = 49
    CM = 50
    SM = 51
    ASSIGN = 52
    CL = 53
    LB = 54
    RB = 55
    LSB = 56
    RSB = 57
    LCB = 58
    RCB = 59
    ID = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'printBoolean'", "'readString'", "'printString'", "'super'", 
            "'preventDefault'", "'auto'", "'break'", "'integer'", "'void'", 
            "'array'", "'float'", "'return'", "'out'", "'boolean'", "'for'", 
            "'string'", "'continue'", "'do'", "'function'", "'of'", "'else'", 
            "'if'", "'while'", "'inherit'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'<'", "'>'", "'<='", "'>='", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'::'", "'.'", "','", "';'", "'='", "':'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "READINTEGER", "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", "PRINTBOOLEAN", 
            "READSTRING", "PRINTSTRING", "SUPER", "PREVENTDEFAULT", "COMMENT", 
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "AUTO", "BREAK", 
            "INTEGER", "VOID", "ARRAY", "FLOAT", "RETURN", "OUT", "BOOLEAN", 
            "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", 
            "IF", "WHILE", "INHERIT", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "LESS", "GT", "LTE", "GTE", "NOT", "AND", "OR", "EQ", "NOT_EQ", 
            "CONCAT", "DOT", "CM", "SM", "ASSIGN", "CL", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "READINTEGER", "PRINTINTEGER", "READFLOAT", "WRITEFLOAT", 
                  "PRINTBOOLEAN", "READSTRING", "PRINTSTRING", "SUPER", 
                  "PREVENTDEFAULT", "COMMENT", "LINE_CMT", "BLOCK_CMT", 
                  "INTLIT", "FLOATLIT", "DECPART", "EXPPART", "BOOLEANLIT", 
                  "FALSE", "TRUE", "STRINGLIT", "NOT_ESC", "ESC", "DOUBLE_QUOTE", 
                  "SINGLE_QUOTE", "AUTO", "BREAK", "INTEGER", "VOID", "ARRAY", 
                  "FLOAT", "RETURN", "OUT", "BOOLEAN", "FOR", "STRING", 
                  "CONTINUE", "DO", "FUNCTION", "OF", "ELSE", "IF", "WHILE", 
                  "INHERIT", "ADD", "SUB", "MUL", "DIV", "MOD", "LESS", 
                  "GT", "LTE", "GTE", "NOT", "AND", "OR", "EQ", "NOT_EQ", 
                  "CONCAT", "DOT", "CM", "SM", "ASSIGN", "CL", "LB", "RB", 
                  "LSB", "RSB", "LCB", "RCB", "ID", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.INTLIT_action 
            actions[13] = self.FLOATLIT_action 
            actions[19] = self.STRINGLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=str(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            s = self.text
            if s[len(s) - 1] == '\n' or s[len(s) - 1] == '\r':
                raise UncloseString(self.text[1:-1])
            raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
            		
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


