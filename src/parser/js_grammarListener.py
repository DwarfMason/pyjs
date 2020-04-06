# Generated from js_grammar.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .js_grammarParser import js_grammarParser
else:
    from js_grammarParser import js_grammarParser

# This class defines a complete listener for a parse tree produced by js_grammarParser.
class js_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by js_grammarParser#program.
    def enterProgram(self, ctx:js_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by js_grammarParser#program.
    def exitProgram(self, ctx:js_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by js_grammarParser#sourceElement.
    def enterSourceElement(self, ctx:js_grammarParser.SourceElementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#sourceElement.
    def exitSourceElement(self, ctx:js_grammarParser.SourceElementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#statement.
    def enterStatement(self, ctx:js_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#statement.
    def exitStatement(self, ctx:js_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#block.
    def enterBlock(self, ctx:js_grammarParser.BlockContext):
        pass

    # Exit a parse tree produced by js_grammarParser#block.
    def exitBlock(self, ctx:js_grammarParser.BlockContext):
        pass


    # Enter a parse tree produced by js_grammarParser#statementList.
    def enterStatementList(self, ctx:js_grammarParser.StatementListContext):
        pass

    # Exit a parse tree produced by js_grammarParser#statementList.
    def exitStatementList(self, ctx:js_grammarParser.StatementListContext):
        pass


    # Enter a parse tree produced by js_grammarParser#importStatement.
    def enterImportStatement(self, ctx:js_grammarParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#importStatement.
    def exitImportStatement(self, ctx:js_grammarParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#importFromBlock.
    def enterImportFromBlock(self, ctx:js_grammarParser.ImportFromBlockContext):
        pass

    # Exit a parse tree produced by js_grammarParser#importFromBlock.
    def exitImportFromBlock(self, ctx:js_grammarParser.ImportFromBlockContext):
        pass


    # Enter a parse tree produced by js_grammarParser#moduleItems.
    def enterModuleItems(self, ctx:js_grammarParser.ModuleItemsContext):
        pass

    # Exit a parse tree produced by js_grammarParser#moduleItems.
    def exitModuleItems(self, ctx:js_grammarParser.ModuleItemsContext):
        pass


    # Enter a parse tree produced by js_grammarParser#importDefault.
    def enterImportDefault(self, ctx:js_grammarParser.ImportDefaultContext):
        pass

    # Exit a parse tree produced by js_grammarParser#importDefault.
    def exitImportDefault(self, ctx:js_grammarParser.ImportDefaultContext):
        pass


    # Enter a parse tree produced by js_grammarParser#importNamespace.
    def enterImportNamespace(self, ctx:js_grammarParser.ImportNamespaceContext):
        pass

    # Exit a parse tree produced by js_grammarParser#importNamespace.
    def exitImportNamespace(self, ctx:js_grammarParser.ImportNamespaceContext):
        pass


    # Enter a parse tree produced by js_grammarParser#importFrom.
    def enterImportFrom(self, ctx:js_grammarParser.ImportFromContext):
        pass

    # Exit a parse tree produced by js_grammarParser#importFrom.
    def exitImportFrom(self, ctx:js_grammarParser.ImportFromContext):
        pass


    # Enter a parse tree produced by js_grammarParser#aliasName.
    def enterAliasName(self, ctx:js_grammarParser.AliasNameContext):
        pass

    # Exit a parse tree produced by js_grammarParser#aliasName.
    def exitAliasName(self, ctx:js_grammarParser.AliasNameContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ExportDeclaration.
    def enterExportDeclaration(self, ctx:js_grammarParser.ExportDeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ExportDeclaration.
    def exitExportDeclaration(self, ctx:js_grammarParser.ExportDeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ExportDefaultDeclaration.
    def enterExportDefaultDeclaration(self, ctx:js_grammarParser.ExportDefaultDeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ExportDefaultDeclaration.
    def exitExportDefaultDeclaration(self, ctx:js_grammarParser.ExportDefaultDeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#exportFromBlock.
    def enterExportFromBlock(self, ctx:js_grammarParser.ExportFromBlockContext):
        pass

    # Exit a parse tree produced by js_grammarParser#exportFromBlock.
    def exitExportFromBlock(self, ctx:js_grammarParser.ExportFromBlockContext):
        pass


    # Enter a parse tree produced by js_grammarParser#declaration.
    def enterDeclaration(self, ctx:js_grammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#declaration.
    def exitDeclaration(self, ctx:js_grammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#variableStatement.
    def enterVariableStatement(self, ctx:js_grammarParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#variableStatement.
    def exitVariableStatement(self, ctx:js_grammarParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:js_grammarParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by js_grammarParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:js_grammarParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by js_grammarParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:js_grammarParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:js_grammarParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#emptyStatement.
    def enterEmptyStatement(self, ctx:js_grammarParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#emptyStatement.
    def exitEmptyStatement(self, ctx:js_grammarParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#expressionStatement.
    def enterExpressionStatement(self, ctx:js_grammarParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#expressionStatement.
    def exitExpressionStatement(self, ctx:js_grammarParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ifStatement.
    def enterIfStatement(self, ctx:js_grammarParser.IfStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ifStatement.
    def exitIfStatement(self, ctx:js_grammarParser.IfStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#DoStatement.
    def enterDoStatement(self, ctx:js_grammarParser.DoStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#DoStatement.
    def exitDoStatement(self, ctx:js_grammarParser.DoStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#WhileStatement.
    def enterWhileStatement(self, ctx:js_grammarParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#WhileStatement.
    def exitWhileStatement(self, ctx:js_grammarParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ForStatement.
    def enterForStatement(self, ctx:js_grammarParser.ForStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ForStatement.
    def exitForStatement(self, ctx:js_grammarParser.ForStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ForInStatement.
    def enterForInStatement(self, ctx:js_grammarParser.ForInStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ForInStatement.
    def exitForInStatement(self, ctx:js_grammarParser.ForInStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#varModifier.
    def enterVarModifier(self, ctx:js_grammarParser.VarModifierContext):
        pass

    # Exit a parse tree produced by js_grammarParser#varModifier.
    def exitVarModifier(self, ctx:js_grammarParser.VarModifierContext):
        pass


    # Enter a parse tree produced by js_grammarParser#continueStatement.
    def enterContinueStatement(self, ctx:js_grammarParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#continueStatement.
    def exitContinueStatement(self, ctx:js_grammarParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#breakStatement.
    def enterBreakStatement(self, ctx:js_grammarParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#breakStatement.
    def exitBreakStatement(self, ctx:js_grammarParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#returnStatement.
    def enterReturnStatement(self, ctx:js_grammarParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#returnStatement.
    def exitReturnStatement(self, ctx:js_grammarParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#yieldStatement.
    def enterYieldStatement(self, ctx:js_grammarParser.YieldStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#yieldStatement.
    def exitYieldStatement(self, ctx:js_grammarParser.YieldStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#withStatement.
    def enterWithStatement(self, ctx:js_grammarParser.WithStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#withStatement.
    def exitWithStatement(self, ctx:js_grammarParser.WithStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#switchStatement.
    def enterSwitchStatement(self, ctx:js_grammarParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#switchStatement.
    def exitSwitchStatement(self, ctx:js_grammarParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#caseBlock.
    def enterCaseBlock(self, ctx:js_grammarParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by js_grammarParser#caseBlock.
    def exitCaseBlock(self, ctx:js_grammarParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by js_grammarParser#caseClauses.
    def enterCaseClauses(self, ctx:js_grammarParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by js_grammarParser#caseClauses.
    def exitCaseClauses(self, ctx:js_grammarParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by js_grammarParser#caseClause.
    def enterCaseClause(self, ctx:js_grammarParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by js_grammarParser#caseClause.
    def exitCaseClause(self, ctx:js_grammarParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by js_grammarParser#defaultClause.
    def enterDefaultClause(self, ctx:js_grammarParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by js_grammarParser#defaultClause.
    def exitDefaultClause(self, ctx:js_grammarParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by js_grammarParser#labelledStatement.
    def enterLabelledStatement(self, ctx:js_grammarParser.LabelledStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#labelledStatement.
    def exitLabelledStatement(self, ctx:js_grammarParser.LabelledStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#throwStatement.
    def enterThrowStatement(self, ctx:js_grammarParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#throwStatement.
    def exitThrowStatement(self, ctx:js_grammarParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#tryStatement.
    def enterTryStatement(self, ctx:js_grammarParser.TryStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#tryStatement.
    def exitTryStatement(self, ctx:js_grammarParser.TryStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#catchProduction.
    def enterCatchProduction(self, ctx:js_grammarParser.CatchProductionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#catchProduction.
    def exitCatchProduction(self, ctx:js_grammarParser.CatchProductionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#finallyProduction.
    def enterFinallyProduction(self, ctx:js_grammarParser.FinallyProductionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#finallyProduction.
    def exitFinallyProduction(self, ctx:js_grammarParser.FinallyProductionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx:js_grammarParser.DebuggerStatementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx:js_grammarParser.DebuggerStatementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:js_grammarParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:js_grammarParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:js_grammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by js_grammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:js_grammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by js_grammarParser#classTail.
    def enterClassTail(self, ctx:js_grammarParser.ClassTailContext):
        pass

    # Exit a parse tree produced by js_grammarParser#classTail.
    def exitClassTail(self, ctx:js_grammarParser.ClassTailContext):
        pass


    # Enter a parse tree produced by js_grammarParser#classElement.
    def enterClassElement(self, ctx:js_grammarParser.ClassElementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#classElement.
    def exitClassElement(self, ctx:js_grammarParser.ClassElementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#methodDefinition.
    def enterMethodDefinition(self, ctx:js_grammarParser.MethodDefinitionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#methodDefinition.
    def exitMethodDefinition(self, ctx:js_grammarParser.MethodDefinitionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#formalParameterList.
    def enterFormalParameterList(self, ctx:js_grammarParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by js_grammarParser#formalParameterList.
    def exitFormalParameterList(self, ctx:js_grammarParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by js_grammarParser#formalParameterArg.
    def enterFormalParameterArg(self, ctx:js_grammarParser.FormalParameterArgContext):
        pass

    # Exit a parse tree produced by js_grammarParser#formalParameterArg.
    def exitFormalParameterArg(self, ctx:js_grammarParser.FormalParameterArgContext):
        pass


    # Enter a parse tree produced by js_grammarParser#lastFormalParameterArg.
    def enterLastFormalParameterArg(self, ctx:js_grammarParser.LastFormalParameterArgContext):
        pass

    # Exit a parse tree produced by js_grammarParser#lastFormalParameterArg.
    def exitLastFormalParameterArg(self, ctx:js_grammarParser.LastFormalParameterArgContext):
        pass


    # Enter a parse tree produced by js_grammarParser#functionBody.
    def enterFunctionBody(self, ctx:js_grammarParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by js_grammarParser#functionBody.
    def exitFunctionBody(self, ctx:js_grammarParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by js_grammarParser#sourceElements.
    def enterSourceElements(self, ctx:js_grammarParser.SourceElementsContext):
        pass

    # Exit a parse tree produced by js_grammarParser#sourceElements.
    def exitSourceElements(self, ctx:js_grammarParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by js_grammarParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:js_grammarParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by js_grammarParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:js_grammarParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by js_grammarParser#elementList.
    def enterElementList(self, ctx:js_grammarParser.ElementListContext):
        pass

    # Exit a parse tree produced by js_grammarParser#elementList.
    def exitElementList(self, ctx:js_grammarParser.ElementListContext):
        pass


    # Enter a parse tree produced by js_grammarParser#arrayElement.
    def enterArrayElement(self, ctx:js_grammarParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by js_grammarParser#arrayElement.
    def exitArrayElement(self, ctx:js_grammarParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by js_grammarParser#objectLiteral.
    def enterObjectLiteral(self, ctx:js_grammarParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by js_grammarParser#objectLiteral.
    def exitObjectLiteral(self, ctx:js_grammarParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:js_grammarParser.PropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:js_grammarParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ComputedPropertyExpressionAssignment.
    def enterComputedPropertyExpressionAssignment(self, ctx:js_grammarParser.ComputedPropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ComputedPropertyExpressionAssignment.
    def exitComputedPropertyExpressionAssignment(self, ctx:js_grammarParser.ComputedPropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by js_grammarParser#FunctionProperty.
    def enterFunctionProperty(self, ctx:js_grammarParser.FunctionPropertyContext):
        pass

    # Exit a parse tree produced by js_grammarParser#FunctionProperty.
    def exitFunctionProperty(self, ctx:js_grammarParser.FunctionPropertyContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PropertyGetter.
    def enterPropertyGetter(self, ctx:js_grammarParser.PropertyGetterContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PropertyGetter.
    def exitPropertyGetter(self, ctx:js_grammarParser.PropertyGetterContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PropertySetter.
    def enterPropertySetter(self, ctx:js_grammarParser.PropertySetterContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PropertySetter.
    def exitPropertySetter(self, ctx:js_grammarParser.PropertySetterContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PropertyShorthand.
    def enterPropertyShorthand(self, ctx:js_grammarParser.PropertyShorthandContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PropertyShorthand.
    def exitPropertyShorthand(self, ctx:js_grammarParser.PropertyShorthandContext):
        pass


    # Enter a parse tree produced by js_grammarParser#propertyName.
    def enterPropertyName(self, ctx:js_grammarParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by js_grammarParser#propertyName.
    def exitPropertyName(self, ctx:js_grammarParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by js_grammarParser#arguments.
    def enterArguments(self, ctx:js_grammarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by js_grammarParser#arguments.
    def exitArguments(self, ctx:js_grammarParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by js_grammarParser#argument.
    def enterArgument(self, ctx:js_grammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by js_grammarParser#argument.
    def exitArgument(self, ctx:js_grammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by js_grammarParser#expressionSequence.
    def enterExpressionSequence(self, ctx:js_grammarParser.ExpressionSequenceContext):
        pass

    # Exit a parse tree produced by js_grammarParser#expressionSequence.
    def exitExpressionSequence(self, ctx:js_grammarParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by js_grammarParser#TemplateStringExpression.
    def enterTemplateStringExpression(self, ctx:js_grammarParser.TemplateStringExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#TemplateStringExpression.
    def exitTemplateStringExpression(self, ctx:js_grammarParser.TemplateStringExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:js_grammarParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:js_grammarParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:js_grammarParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:js_grammarParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PowerExpression.
    def enterPowerExpression(self, ctx:js_grammarParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PowerExpression.
    def exitPowerExpression(self, ctx:js_grammarParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:js_grammarParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:js_grammarParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:js_grammarParser.ObjectLiteralExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:js_grammarParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#MetaExpression.
    def enterMetaExpression(self, ctx:js_grammarParser.MetaExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#MetaExpression.
    def exitMetaExpression(self, ctx:js_grammarParser.MetaExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#InExpression.
    def enterInExpression(self, ctx:js_grammarParser.InExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#InExpression.
    def exitInExpression(self, ctx:js_grammarParser.InExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:js_grammarParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:js_grammarParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#NotExpression.
    def enterNotExpression(self, ctx:js_grammarParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#NotExpression.
    def exitNotExpression(self, ctx:js_grammarParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:js_grammarParser.PreDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:js_grammarParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:js_grammarParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:js_grammarParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#AwaitExpression.
    def enterAwaitExpression(self, ctx:js_grammarParser.AwaitExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#AwaitExpression.
    def exitAwaitExpression(self, ctx:js_grammarParser.AwaitExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ThisExpression.
    def enterThisExpression(self, ctx:js_grammarParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ThisExpression.
    def exitThisExpression(self, ctx:js_grammarParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#FunctionExpression.
    def enterFunctionExpression(self, ctx:js_grammarParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#FunctionExpression.
    def exitFunctionExpression(self, ctx:js_grammarParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:js_grammarParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:js_grammarParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:js_grammarParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:js_grammarParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:js_grammarParser.PostDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:js_grammarParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#TypeofExpression.
    def enterTypeofExpression(self, ctx:js_grammarParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#TypeofExpression.
    def exitTypeofExpression(self, ctx:js_grammarParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx:js_grammarParser.InstanceofExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx:js_grammarParser.InstanceofExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:js_grammarParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:js_grammarParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#DeleteExpression.
    def enterDeleteExpression(self, ctx:js_grammarParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#DeleteExpression.
    def exitDeleteExpression(self, ctx:js_grammarParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ImportExpression.
    def enterImportExpression(self, ctx:js_grammarParser.ImportExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ImportExpression.
    def exitImportExpression(self, ctx:js_grammarParser.ImportExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:js_grammarParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:js_grammarParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:js_grammarParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:js_grammarParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#SuperExpression.
    def enterSuperExpression(self, ctx:js_grammarParser.SuperExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#SuperExpression.
    def exitSuperExpression(self, ctx:js_grammarParser.SuperExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:js_grammarParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:js_grammarParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:js_grammarParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:js_grammarParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:js_grammarParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:js_grammarParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:js_grammarParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:js_grammarParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:js_grammarParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:js_grammarParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:js_grammarParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:js_grammarParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#YieldExpression.
    def enterYieldExpression(self, ctx:js_grammarParser.YieldExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#YieldExpression.
    def exitYieldExpression(self, ctx:js_grammarParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:js_grammarParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:js_grammarParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#NewExpression.
    def enterNewExpression(self, ctx:js_grammarParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#NewExpression.
    def exitNewExpression(self, ctx:js_grammarParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:js_grammarParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:js_grammarParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:js_grammarParser.ArrayLiteralExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:js_grammarParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:js_grammarParser.MemberDotExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:js_grammarParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ClassExpression.
    def enterClassExpression(self, ctx:js_grammarParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ClassExpression.
    def exitClassExpression(self, ctx:js_grammarParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:js_grammarParser.MemberIndexExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:js_grammarParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:js_grammarParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:js_grammarParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:js_grammarParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:js_grammarParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:js_grammarParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:js_grammarParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:js_grammarParser.AssignmentOperatorExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:js_grammarParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#VoidExpression.
    def enterVoidExpression(self, ctx:js_grammarParser.VoidExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#VoidExpression.
    def exitVoidExpression(self, ctx:js_grammarParser.VoidExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#CoalesceExpression.
    def enterCoalesceExpression(self, ctx:js_grammarParser.CoalesceExpressionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#CoalesceExpression.
    def exitCoalesceExpression(self, ctx:js_grammarParser.CoalesceExpressionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#assignable.
    def enterAssignable(self, ctx:js_grammarParser.AssignableContext):
        pass

    # Exit a parse tree produced by js_grammarParser#assignable.
    def exitAssignable(self, ctx:js_grammarParser.AssignableContext):
        pass


    # Enter a parse tree produced by js_grammarParser#FunctionDecl.
    def enterFunctionDecl(self, ctx:js_grammarParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by js_grammarParser#FunctionDecl.
    def exitFunctionDecl(self, ctx:js_grammarParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by js_grammarParser#AnoymousFunctionDecl.
    def enterAnoymousFunctionDecl(self, ctx:js_grammarParser.AnoymousFunctionDeclContext):
        pass

    # Exit a parse tree produced by js_grammarParser#AnoymousFunctionDecl.
    def exitAnoymousFunctionDecl(self, ctx:js_grammarParser.AnoymousFunctionDeclContext):
        pass


    # Enter a parse tree produced by js_grammarParser#ArrowFunction.
    def enterArrowFunction(self, ctx:js_grammarParser.ArrowFunctionContext):
        pass

    # Exit a parse tree produced by js_grammarParser#ArrowFunction.
    def exitArrowFunction(self, ctx:js_grammarParser.ArrowFunctionContext):
        pass


    # Enter a parse tree produced by js_grammarParser#arrowFunctionParameters.
    def enterArrowFunctionParameters(self, ctx:js_grammarParser.ArrowFunctionParametersContext):
        pass

    # Exit a parse tree produced by js_grammarParser#arrowFunctionParameters.
    def exitArrowFunctionParameters(self, ctx:js_grammarParser.ArrowFunctionParametersContext):
        pass


    # Enter a parse tree produced by js_grammarParser#arrowFunctionBody.
    def enterArrowFunctionBody(self, ctx:js_grammarParser.ArrowFunctionBodyContext):
        pass

    # Exit a parse tree produced by js_grammarParser#arrowFunctionBody.
    def exitArrowFunctionBody(self, ctx:js_grammarParser.ArrowFunctionBodyContext):
        pass


    # Enter a parse tree produced by js_grammarParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:js_grammarParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by js_grammarParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:js_grammarParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by js_grammarParser#literal.
    def enterLiteral(self, ctx:js_grammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by js_grammarParser#literal.
    def exitLiteral(self, ctx:js_grammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by js_grammarParser#numericLiteral.
    def enterNumericLiteral(self, ctx:js_grammarParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by js_grammarParser#numericLiteral.
    def exitNumericLiteral(self, ctx:js_grammarParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by js_grammarParser#bigintLiteral.
    def enterBigintLiteral(self, ctx:js_grammarParser.BigintLiteralContext):
        pass

    # Exit a parse tree produced by js_grammarParser#bigintLiteral.
    def exitBigintLiteral(self, ctx:js_grammarParser.BigintLiteralContext):
        pass


    # Enter a parse tree produced by js_grammarParser#identifierName.
    def enterIdentifierName(self, ctx:js_grammarParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by js_grammarParser#identifierName.
    def exitIdentifierName(self, ctx:js_grammarParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by js_grammarParser#reservedWord.
    def enterReservedWord(self, ctx:js_grammarParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by js_grammarParser#reservedWord.
    def exitReservedWord(self, ctx:js_grammarParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by js_grammarParser#keyword.
    def enterKeyword(self, ctx:js_grammarParser.KeywordContext):
        pass

    # Exit a parse tree produced by js_grammarParser#keyword.
    def exitKeyword(self, ctx:js_grammarParser.KeywordContext):
        pass


    # Enter a parse tree produced by js_grammarParser#eos.
    def enterEos(self, ctx:js_grammarParser.EosContext):
        pass

    # Exit a parse tree produced by js_grammarParser#eos.
    def exitEos(self, ctx:js_grammarParser.EosContext):
        pass



del js_grammarParser