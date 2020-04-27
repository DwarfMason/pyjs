from antlr4 import *
import sys
from src.parser.JavaScriptLexer import JavaScriptLexer
from src.parser.JavaScriptParser import JavaScriptParser
from src.parser.JavaScriptParserListener import JavaScriptParserListener


class HelloPrintListener(JavaScriptParserListener):
    def enterHi(self):
        print("\nSuccess!")

def main():
    lexer = JavaScriptLexer(StdinStream()) #Input your text, then press enter and ctrl+d to test
    stream = CommonTokenStream(lexer)
    parser = JavaScriptParser(stream)
    tree = parser.program()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
