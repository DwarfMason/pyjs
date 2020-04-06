/*
 * The MIT License (MIT)
 *
 * Copyright (c) 2014 by Bart Kiers (original author) and Alexandre Vitorelli (contributor -> ported to CSharp)
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */
grammar js_grammar;

@parser::members {
  
  
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
        throw new NotImplementedException("This lexem construction doesn't supported");
    }
}


@lexer::members {
     
    private IToken lastToken = null;
     
    public override IToken NextToken() {
        
        // Get the next token.
        IToken next = base.NextToken();
        
        if (next.Channel == Lexer.DefaultTokenChannel) {
            // Keep track of the last token on the default channel.                                              
            this.lastToken = next;
        }
        
        return next;
    }

    private bool isRegexPossible() {
                                       
        if (this.lastToken == null) {
            // No token has been produced yet: at the start of the input,
            // no division is possible, so a regex literal _is_ possible.
            return true;
        }
        
        switch (this.lastToken.Type) {
            case Identifier:
            case NullLiteral:
            case BooleanLiteral:
            case This:
            case CloseBracket:
            case CloseParen:
            case DecimalLiteral:
            case HexIntegerLiteral:
            case OctalIntegerLiteral2:
            case BinaryIntegerLiteral: 
            case BigHexIntegerLiteral: 
            case BigOctalIntegerLiteral:
            case BigBinaryIntegerLiteral:
            case BigDecimalIntegerLiteral:
            case StringLiteral:
            case PlusPlus:
            case MinusMinus:
                // After any of the tokens above, no regex literal can follow.
                return false;
            default:
                // In all other cases, a regex literal _is_ possible.
                return true;
        }
    }
    
    private void notImplemented()
    {
        throw new NotImplementedException("This grammar construction doesn't supported");
    }
}

program
    : sourceElements? EOF
    ;

sourceElement
    :statement
    ;

statement
 : block
 | variableStatement
 | emptyStatement
 | ifStatement
 | iterationStatement
 | continueStatement
 | breakStatement
 | returnStatement
 | withStatement
 | labelledStatement
 | switchStatement {notImplemented();}
 | throwStatement {notImplemented();}
 | tryStatement {notImplemented();}
 | debuggerStatement {notImplemented();}
 ;

block
 : '{' statementList? '}'
 ;

statementList
 : statement+
 ;

/// VariableStatement :
///     var VariableDeclarationList ;
variableStatement
    : variableDeclarationList eos
    ;

variableDeclarationList
    : varModifier variableDeclaration (',' variableDeclaration)*
    ;

variableDeclaration
    : Identifier initialiser?
    ;

initialiser
 : '=' singleExpression
 ;

emptyStatement
 : SemiColon
 ;

expressionStatement
 : expressionSequence eos
 ;

/// IfStatement :
///     if ( Expression ) Statement else Statement
///     if ( Expression ) Statement
ifStatement
 : If '(' expressionSequence ')' statement ( Else statement )?
 ;

iterationStatement
 : Do statement While '(' expressionSequence ')' eos                                                 # DoStatement
 | While '(' expressionSequence ')' statement                                                        # WhileStatement
 | For '(' expressionSequence? ';' expressionSequence? ';' expressionSequence? ')' statement         # ForStatement
 | For '(' Var variableDeclarationList ';' expressionSequence? ';' expressionSequence? ')' statement # ForVarStatement
 | For '(' singleExpression In expressionSequence ')' statement                                      # ForInStatement
 | For '(' Var variableDeclaration In expressionSequence ')' statement                               # ForVarInStatement
 ;

 varModifier  // let, const - ECMAScript 6
    : Var
    | Let
    | Const
    ;

continueStatement
 : Continue ({!here(LineTerminator)}? Identifier)? eos
 ;

breakStatement
 : Break ({!here(LineTerminator)}? Identifier)? eos
 ;

/// ReturnStatement :
///     return ;
///     return [no LineTerminator here] Expression ;
returnStatement
 : Return ({!here(LineTerminator)}? expressionSequence)? eos
 ;

/// WithStatement :
///     with ( Expression ) Statement
withStatement
 : With '(' expressionSequence ')' statement
 ;

/// SwitchStatement :
///     switch ( Expression ) CaseBlock
switchStatement
 : Switch '(' expressionSequence ')' caseBlock
 ;

/// CaseBlock :
///     { CaseClauses? }
///     { CaseClauses? DefaultClause CaseClauses? }
caseBlock
 : '{' caseClauses? ( defaultClause caseClauses? )? '}'
 ;

/// CaseClauses :
///     CaseClause
///     CaseClauses CaseClause
caseClauses
 : caseClause+
 ;

/// CaseClause :
///     case Expression ':' StatementList?
caseClause
 : Case expressionSequence ':' statementList?
 ;

/// DefaultClause :
///     default ':' StatementList?
defaultClause
 : Default ':' statementList?
 ;

/// LabelledStatement :
///     Identifier ':' Statement
labelledStatement
 : Identifier ':' statement
 ;

/// ThrowStatement :
///     throw [no LineTerminator here] Expression ;
throwStatement
 : Throw {!here(LineTerminator)}? expressionSequence eos
 ;

/// TryStatement :
///     try Block Catch
///     try Block Finally
///     try Block Catch Finally
tryStatement
 : Try block catchProduction
 | Try block finallyProduction
 | Try block catchProduction finallyProduction
 ;

/// Catch :
///     catch ( Identifier ) Block
catchProduction
 : Catch '(' Identifier ')' block
 ;

/// Finally :
///     finally Block
finallyProduction
 : Finally block
 ;

/// DebuggerStatement :
///     debugger ;
debuggerStatement
 : Debugger eos
 ;

/// FunctionDeclaration :
///     function Identifier ( FormalParameterList? ) { FunctionBody }
functionDeclaration
 : Function Identifier '(' formalParameterList? ')' '{' functionBody '}'
 ;

/// FormalParameterList :
///     Identifier
///     FormalParameterList , Identifier
formalParameterList
 : Identifier ( ',' Identifier )*
 ;

/// FunctionBody :
///     SourceElements?
functionBody
 : sourceElements?
 ;

 sourceElements
    : sourceElement+
    ;

/// ArrayLiteral :
///     [ Elision? ]
///     [ ElementList ]
///     [ ElementList , Elision? ]
arrayLiteral
 : '[' elementList? ','? elision? ']'
 ;

/// ElementList :
///     Elision? AssignmentExpression
///     ElementList , Elision? AssignmentExpression
elementList
 : elision? singleExpression ( ',' elision? singleExpression )*
 ;

/// Elision :
///     ,
///     Elision ,
elision
 : ','+
 ;

/// ObjectLiteral :
///     { }
///     { PropertyNameAndValueList }
///     { PropertyNameAndValueList , }
objectLiteral
 : '{' '}'
 | '{' propertyNameAndValueList ','? '}'
 ;

/// PropertyNameAndValueList :
///     PropertyAssignment
///     PropertyNameAndValueList , PropertyAssignment
propertyNameAndValueList
 : propertyAssignment ( ',' propertyAssignment )*
 ;

/// PropertyAssignment :
///     PropertyName : AssignmentExpression
///     get PropertyName ( ) { FunctionBody }
///     set PropertyName ( PropertySetParameterList ) { FunctionBody }
propertyAssignment
 : propertyName ':' singleExpression                            # PropertyExpressionAssignment
 | getter '(' ')' '{' functionBody '}'                          # PropertyGetter
 | setter '(' propertySetParameterList ')' '{' functionBody '}' # PropertySetter
 ;           

/// PropertyName :
///     IdentifierName
///     StringLiteral
///     NumericLiteral
propertyName
 : identifierName
 | StringLiteral
 | numericLiteral
 ;

/// PropertySetParameterList :
///     Identifier
propertySetParameterList
 : Identifier
 ;

/// Arguments :
///     ( )
///     ( ArgumentList )
arguments
 : '('(argument (',' argument)* ','?)?')'
 ;

 argument
    : Ellipsis? (singleExpression | Identifier)
    ;

expressionSequence
 : singleExpression ( ',' singleExpression )*
 ;

singleExpression
 : Function Identifier? '(' formalParameterList? ')' '{' functionBody '}' # FunctionExpression
 | singleExpression '[' expressionSequence ']'                            # MemberIndexExpression
 | singleExpression '.' identifierName                                    # MemberDotExpression
 | singleExpression arguments                                             # ArgumentsExpression
 | New singleExpression arguments?                                        # NewExpression
 | singleExpression {!here(LineTerminator)}? '++'                         # PostIncrementExpression
 | singleExpression {!here(LineTerminator)}? '--'                         # PostDecreaseExpression
 | Delete singleExpression                                                # DeleteExpression
 | Void singleExpression                                                  # VoidExpression
 | Typeof singleExpression                                                # TypeofExpression
 | '++' singleExpression                                                  # PreIncrementExpression
 | '--' singleExpression                                                  # PreDecreaseExpression
 | '+' singleExpression                                                   # UnaryPlusExpression
 | '-' singleExpression                                                   # UnaryMinusExpression
 | '~' singleExpression                                                   # BitNotExpression
 | '!' singleExpression                                                   # NotExpression
 | singleExpression ( '*' | '/' | '%' ) singleExpression                  # MultiplicativeExpression
 | singleExpression ( '+' | '-' ) singleExpression                        # AdditiveExpression
 | singleExpression ( '<<' | '>>' | '>>>' ) singleExpression              # BitShiftExpression
 | singleExpression ( '<' | '>' | '<=' | '>=' ) singleExpression          # RelationalExpression
 | singleExpression Instanceof singleExpression                           # InstanceofExpression
 | singleExpression In singleExpression                                   # InExpression
 | singleExpression ( '==' | '!=' | '===' | '!==' ) singleExpression      # EqualityExpression
 | singleExpression '&' singleExpression                                  # BitAndExpression
 | singleExpression '^' singleExpression                                  # BitXOrExpression
 | singleExpression '|' singleExpression                                  # BitOrExpression
 | singleExpression '&&' singleExpression                                 # LogicalAndExpression
 | singleExpression '||' singleExpression                                 # LogicalOrExpression
 | singleExpression '?' singleExpression ':' singleExpression             # TernaryExpression
 | singleExpression '=' singleExpression                                  # AssignmentExpression
 | singleExpression assignmentOperator singleExpression                   # AssignmentOperatorExpression
 | This                                                                   # ThisExpression
 | Identifier                                                             # IdentifierExpression
 | literal                                                                # LiteralExpression
 | arrayLiteral                                                           # ArrayLiteralExpression
 | objectLiteral                                                          # ObjectLiteralExpression
 | '(' exp=expressionSequence ')'                                             # ParenthesizedExpression
 ;

/// AssignmentOperator : one of
///     *=   /=  %=  +=  -=  <<= >>= >>>=    &=  ^=  |=
assignmentOperator
 : '*=' 
 | '/=' 
 | '%=' 
 | '+=' 
 | '-=' 
 | '<<=' 
 | '>>=' 
 | '>>>=' 
 | '&=' 
 | '^=' 
 | '|='
 ;

literal
 : ( NullLiteral 
   | BooleanLiteral
   | StringLiteral
   | RegularExpressionLiteral
   )
 | numericLiteral
 ;

numericLiteral
 : DecimalLiteral
 | HexIntegerLiteral
 | OctalIntegerLiteral
 ;

identifierName
 : Identifier
 | reservedWord
 ;

reservedWord
 : keyword
 | futureReservedWord
 | ( NullLiteral
   | BooleanLiteral
   )
 ;

keyword
 : Break
 | Do
 | Instanceof
 | Typeof
 | Case
 | Else
 | New
 | Var
 | Catch
 | Finally
 | Return
 | Void
 | Continue
 | For
 | Switch
 | While
 | Debugger
 | Function
 | This
 | With
 | Default
 | If
 | Throw
 | Delete
 | In
 | Try
 | Let
 ;

futureReservedWord
 : Class
 | Enum
 | Extends
 | Super
 | Const
 | Export
 | Import
 | Implements
 | Private
 | Public
 | Interface
 | Package
 | Protected
 | Static
 | Yield
 ;

getter
 : {_input.LT(1).Text.Equals("get")}? Identifier propertyName
 ;

setter
 : {_input.LT(1).Text.Equals("set")}? Identifier propertyName
 ;

eos
 : SemiColon
 | EOF
 | {lineTerminatorAhead()}?
 | {_input.LT(1).Type == CloseBrace}?
 ;

eof
 : EOF
 ;

/// RegularExpressionLiteral ::
///     / RegularExpressionBody / RegularExpressionFlags
RegularExpressionLiteral
 : {isRegexPossible()}? '/' RegularExpressionBody '/' RegularExpressionFlags
 ;

/// 7.3 Line Terminators
LineTerminator
 : [\r\n] -> channel(HIDDEN)
 ;

OpenBracket                : '[';
CloseBracket               : ']';
OpenParen                  : '(';
CloseParen                 : ')';
OpenBrace                  : '{';
CloseBrace                 : '}';
SemiColon                  : ';';
Comma                      : ',';
Assign                     : '=';
QuestionMark               : '?';
Colon                      : ':';
Dot                        : '.';
PlusPlus                   : '++';
MinusMinus                 : '--';
Plus                       : '+';
Minus                      : '-';
BitNot                     : '~';
Not                        : '!';
Multiply                   : '*';
Divide                     : '/';
Modulus                    : '%';
RightShiftArithmetic       : '>>';
LeftShiftArithmetic        : '<<';
RightShiftLogical          : '>>>';
LessThan                   : '<';
MoreThan                   : '>';
LessThanEquals             : '<=';
GreaterThanEquals          : '>=';
Equals                     : '==';
NotEquals                  : '!=';
IdentityEquals             : '===';
IdentityNotEquals          : '!==';
BitAnd                     : '&';
BitXOr                     : '^';
BitOr                      : '|';
And                        : '&&';
Or                         : '||';
MultiplyAssign             : '*=';
DivideAssign               : '/='; 
ModulusAssign              : '%='; 
PlusAssign                 : '+='; 
MinusAssign                : '-='; 
LeftShiftArithmeticAssign  : '<<='; 
RightShiftArithmeticAssign : '>>='; 
RightShiftLogicalAssign    : '>>>='; 
BitAndAssign               : '&='; 
BitXorAssign               : '^='; 
BitOrAssign                : '|=';

/// 7.8.1 Null Literals
NullLiteral
 : 'null'
 ;

/// 7.8.2 Boolean Literals
BooleanLiteral
 : 'true'
 | 'false'
 ;

/// 7.8.3 Numeric Literals
DecimalLiteral
 : DecimalIntegerLiteral '.' DecimalDigit* ExponentPart?
 | '.' DecimalDigit+ ExponentPart?
 | DecimalIntegerLiteral ExponentPart?
 ;

/// 7.8.3 Numeric Literals
HexIntegerLiteral
 : '0' [xX] HexDigit+
 ;

/// 7.6.1.1 Keywords
Break      : 'break';
Do         : 'do';
Instanceof : 'instanceof';
Typeof     : 'typeof';
Case       : 'case';
Else       : 'else';
New        : 'new';
Var        : 'var';
Let        : 'let';
Catch      : 'catch' {notImplemented();};
Finally    : 'finally' {notImplemented();};
Return     : 'return';
Void       : 'void';
Continue   : 'continue';
For        : 'for';
Switch     : 'switch' {notImplemented();};
While      : 'while';
Debugger   : 'debugger';
Function   : 'function';
This       : 'this';
With       : 'with' {notImplemented();};
Default    : 'default';
If         : 'if';
Throw      : 'throw' {notImplemented();};
Delete     : 'delete';
In         : 'in';
Try        : 'try' {notImplemented();};

/// 7.6.1.2 Future Reserved Words
Class   : 'class';
Enum    : 'enum';
Extends : 'extends';
Super   : 'super';
Const   : 'const';
Export  : 'export';
Import  : 'import';

/// The following tokens are also considered to be FutureReservedWords 
/// when parsing strict mode  
Implements : {strictMode}? 'implements' {notImplemented();};
Private    : {strictMode}? 'private' {notImplemented();};
Public     : {strictMode}? 'public' {notImplemented();};
Interface  : {strictMode}? 'interface' {notImplemented();};
Package    : {strictMode}? 'package' {notImplemented();};
Protected  : {strictMode}? 'protected' {notImplemented();};
Static     : {strictMode}? 'static' {notImplemented();};
Yield      : {strictMode}? 'yield' {notImplemented();};

/// 7.6 Identifier Names and Identifiers
Identifier
 : IdentifierStart IdentifierPart*
 ;

/// 7.8.4 String Literals
StringLiteral
 : '"' DoubleStringCharacter* '"'
 | '\'' SingleStringCharacter* '\''
 ;

WhiteSpaces
 : [\t]+ -> channel(HIDDEN)
 ;

/// 7.4 Comments
MultiLineComment
 : '/*' .*? '*/' -> channel(HIDDEN)
 ;

SingleLineComment
 : '//' ~[\r\n]* -> channel(HIDDEN)
 ;

UnexpectedCharacter
 : .
 ;

fragment DoubleStringCharacter
 : ~["\\\r\n]
 | '\\' EscapeSequence
 | LineContinuation
 ;
fragment SingleStringCharacter
 : ~['\\\r\n]
 | '\\' EscapeSequence
 | LineContinuation
 ;
fragment EscapeSequence
 : CharacterEscapeSequence
 | '0' // no digit ahead! TODO
 | HexEscapeSequence
 | UnicodeEscapeSequence
 ;
fragment CharacterEscapeSequence
 : SingleEscapeCharacter
 | NonEscapeCharacter
 ;
fragment HexEscapeSequence
 : 'x' HexDigit HexDigit
 ;
fragment UnicodeEscapeSequence
 : 'u' HexDigit HexDigit HexDigit HexDigit
 ;
fragment SingleEscapeCharacter
 : ['"\\bfnrtv]
 ;

fragment NonEscapeCharacter
 : ~['"\\bfnrtv0-9xu\r\n]
 ;
fragment EscapeCharacter
 : SingleEscapeCharacter
 | DecimalDigit
 | [xu]
 ;
fragment LineContinuation
 : '\\' LineTerminatorSequence 
 ;
fragment LineTerminatorSequence
 : '\r\n'
 | LineTerminator
 ;
fragment DecimalDigit
 : [0-9]
 ;
fragment HexDigit
 : [0-9a-fA-F]
 ;
fragment OctalDigit
 : [0-7]
 ;
fragment DecimalIntegerLiteral
 : '0'
 | [1-9] DecimalDigit*
 ;
fragment ExponentPart
 : [eE] [+-]? DecimalDigit+
 ;
fragment IdentifierStart
 :  [$_a-zA-Z]
 | '\\' UnicodeEscapeSequence
 ;
fragment IdentifierPart
 : IdentifierStart
 | DecimalDigit
 ;

/// RegularExpressionBody ::
///     RegularExpressionFirstChar RegularExpressionChars
///
/// RegularExpressionChars ::
///     [empty]
///     RegularExpressionChars RegularExpressionChar
fragment RegularExpressionBody
 : RegularExpressionFirstChar RegularExpressionChar*
 ;
/// RegularExpressionFlags ::
///     [empty]
///     RegularExpressionFlags IdentifierPart
fragment RegularExpressionFlags
 : IdentifierPart*
 ;
/// RegularExpressionFirstChar ::
///     RegularExpressionNonTerminator but not one of * or \ or / or [
///     RegularExpressionBackslashSequence
///     RegularExpressionClass
fragment RegularExpressionFirstChar
 : ~[\r\n\\/[]
 | RegularExpressionBackslashSequence
 | RegularExpressionClass
 ;
/// RegularExpressionChar ::
///     RegularExpressionNonTerminator but not \ or / or [
///     RegularExpressionBackslashSequence
///     RegularExpressionClass
fragment RegularExpressionChar
 : ~[\r\n\\/[]
 | RegularExpressionBackslashSequence
 | RegularExpressionClass
 ;
/// RegularExpressionNonTerminator ::
///     SourceCharacter but not LineTerminator
fragment RegularExpressionNonTerminator
 : ~[\r\n]
 ;
/// RegularExpressionBackslashSequence ::
///     \ RegularExpressionNonTerminator
fragment RegularExpressionBackslashSequence
 : '\\' RegularExpressionNonTerminator
 ;
 
/// RegularExpressionClass ::
///     [ RegularExpressionClassChars ]
///
/// RegularExpressionClassChars ::
///     [empty]
///     RegularExpressionClassChars RegularExpressionClassChar
fragment RegularExpressionClass
  : '[' RegularExpressionClassChar* ']'
  ;
 
/// RegularExpressionClassChar ::
///     RegularExpressionNonTerminator but not ] or \
///     RegularExpressionBackslashSequence
fragment RegularExpressionClassChar
 : ~[\r\n\]\\]
 | RegularExpressionBackslashSequence
 ;
