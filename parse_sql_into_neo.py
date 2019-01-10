from antlr4 import *
from gen.Tsql.TSqlLexer import TSqlLexer
from gen.Tsql.TSqlParserListener import TSqlParserListener
from gen.Tsql.TSqlParser import TSqlParser


def main():

    # if we get a batch of files, then we can try to loop through
    # the entire set of files... not ready fo that yet.

    # import os
    # filenames = os.listdir('./grammars/tsql/examples')
    # for filename in filenames:
    #
    #     lexer = TSqlLexer(FileStream('./grammars/tsql/examples/'+filename))

    lexer = TSqlLexer(FileStream('./grammars/tsql/examples/big_select.sql'))
    stream = CommonTokenStream(lexer)
    parser = TSqlParser(stream)
    tree = parser.tsql_file()
    printer = TSqlParserListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()