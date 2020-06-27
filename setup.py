import os

os.system('pip install -r requirements.txt')
os.system('antlr4 -Dlanguage=Python3 src/parser_utils/JavaScriptLexer.g4 src/parser_utils/JavaScriptParser.g4')
