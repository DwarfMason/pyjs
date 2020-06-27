from src.FileParser import parse_file
from src.ast_printer.ast_printer import get_ast, print_ast

parsed_tuple = parse_file("test.js")
parse_tree = parsed_tuple[1]
ast_tree = get_ast(parse_tree)
print_ast(ast_tree)
