import os

os.system('pip install -r requirements.txt')
os.system('antlr4 -Dlanguage=Python3 src/parser/JavaScriptLexer.g4 src/parser/JavaScriptParser.g4')
