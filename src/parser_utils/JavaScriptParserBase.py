 
from antlr4 import *


class JavaScriptParserBase(Parser):
    def notImplemented(self):
        raise Exception("This parser_utils construction is not implemented!")

    def p(self, s : str) -> bool:
        return self.prev(s)

    def prev(self, s : str) -> bool:
        return self._input.LT(-1).getText().equals(s)

    def n(self, s : str) -> bool:
        return self.next(s)

    def next(self, s: str) -> bool:
        return self._input.LT(1).getText().equals(s)

    def notLineTerminator(self) -> bool:
        from .JavaScriptParser import JavaScriptParser
        return not self.here(JavaScriptParser.LineTerminator)

    def notOpenBraceAndNotFunction(self) -> bool:
        from .JavaScriptParser import JavaScriptParser

        nextTokenType = self._input.LT(1).type
        return nextTokenType != JavaScriptParser.OpenBrace and nextTokenType != JavaScriptParser.Function

    def closeBrace(self) -> bool:
        from .JavaScriptParser import JavaScriptParser

        return self._input.LT(1).type == JavaScriptParser.CloseBrace

    def here(self, tokenType: int) -> bool:
        """
        Returns {@code true} iff on the current index of the parser_utils's
        token stream a token of the given {@code type} exists on the
        {@code HIDDEN} channel.
        :param:type:
                   the type of the token on the {@code HIDDEN} channel
                   to check.
        :return:{@code true} iff on the current index of the parser_utils's
            token stream a token of the given {@code type} exists on the
            {@code HIDDEN} channel.
        """
        # Get the token ahead of the current index.
        assert isinstance(self.getCurrentToken(), Token)
        possibleIndexEosToken: Token = self.getCurrentToken().tokenIndex - 1
        ahead = self._input.get(possibleIndexEosToken)

        # Check if the token resides on the HIDDEN channel and if it's of the
        # provided type.
        return (ahead.channel == Lexer.HIDDEN) and (ahead.type == tokenType)

    def lineTerminatorAhead(self) -> bool:
        """
        Returns {@code true} iff on the current index of the parser_utils's
        token stream a token exists on the {@code HIDDEN} channel which
        either is a line terminator, or is a multi line comment that
        contains a line terminator.
        :return: {@code true} iff on the current index of the parser_utils's
        token stream a token exists on the {@code HIDDEN} channel which
        either is a line terminator, or is a multi line comment that
        contains a line terminator.
        """
        from .JavaScriptParser import JavaScriptParser

        # Get the token ahead of the current index.
        possibleIndexEosToken: Token = self.getCurrentToken().tokenIndex - 1
        ahead: Token = self._input.get(possibleIndexEosToken)

        if ahead.channel != Lexer.HIDDEN:
            # We're only interested in tokens on the HIDDEN channel.
            return False

        if ahead.type == JavaScriptParser.LineTerminator:
            # There is definitely a line terminator ahead.
            return True

        if ahead.type == JavaScriptParser.WhiteSpaces:
            # Get the token ahead of the current whitespaces.
            possibleIndexEosToken = self.getCurrentToken().tokenIndex - 2
            ahead = self._input.get(possibleIndexEosToken)

        # Get the token's text and type.
        text = ahead.text
        tokenType = ahead.type

        # Check if the token is, or contains a line terminator.
        return ((tokenType == JavaScriptParser.MultiLineComment and (text.contains("\r") or text.contains("\n"))) or
                (tokenType == JavaScriptParser.LineTerminator))