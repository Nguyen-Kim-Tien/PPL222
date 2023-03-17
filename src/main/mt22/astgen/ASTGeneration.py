from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

def flatten(lst):
    return [elem for sublist in lst for elem in (flatten(sublist) if isinstance(sublist, list) else [sublist])]

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decl_list = [self.visitDecl(x) for x in ctx.decl()]
        decl_list = [decl for sublist in decl_list for decl in (sublist if isinstance(sublist, list) else [sublist])]
        return Program(decl_list)

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visitChildren(ctx)

    def visitArraytype(self, ctx: MT22Parser.ArraytypeContext):
        lst_dms = self.visit(ctx.dimension())
        typ = self.visit(ctx.eletype())
        return ArrayType(lst_dms, typ)

    def visitNumber(self, ctx: MT22Parser.NumberContext):
        return self.visitChildren(ctx)
    
    def visitEletype(self, ctx: MT22Parser.EletypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        return BooleanType()

    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        return [str(ctx.INTLIT().getText())] + (self.visit(ctx.dimension()) if ctx.getChildCount() > 1 else [])

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visitChildren(ctx)

    def visitVardeclNoEq(self, ctx: MT22Parser.VardeclNoEqContext):
        idlist = self.visit(ctx.idlist())
        typ = self.visit(ctx.eletype()) if ctx.eletype() else self.visit(ctx.arraytype())
        return [VarDecl(x, typ) for x in idlist]

    def visitVardeclEq(self, ctx: MT22Parser.VardeclEqContext):
        if ctx.assignment():
            ident = ctx.IDENTIFIER().getText()
            assign = self.visit(ctx.assignment())
            expr = self.visit(ctx.expr())
            lst = [ident, assign, expr]
            lst_flatten = flatten(lst)
            idxType = int(len(lst_flatten)/2)
            eletype = lst_flatten[idxType]
            identlist = lst_flatten[0:idxType]
            val = lst_flatten[idxType + 1:]

            return list(map(lambda x, y: VarDecl(x, eletype, y), identlist, val))
        else:
            ident = ctx.IDENTIFIER().getText()
            expr = self.visit(ctx.expr())
            typ = self.visit(ctx.getChild(2))
            return VarDecl(ident, typ, expr)

    def visitAssignment(self, ctx: MT22Parser.AssignmentContext):
        if ctx.assignment():
            return [ctx.IDENTIFIER().getText(), self.visit(ctx.assignment()), self.visit(ctx.expr())]
        return [ctx.IDENTIFIER().getText(), self.visit(ctx.getChild(2)), self.visit(ctx.expr())]

    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idlist()) if ctx.getChildCount() != 1 else [ctx.IDENTIFIER().getText()]

    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist()) if ctx.getChildCount() != 1 else [self.visit(ctx.expr())]

    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        inherited = True if ctx.INHERIT() else False
        out = True if ctx.OUT() else False
        ident = ctx.IDENTIFIER().getText()
        eletype = self.visit(ctx.eletype()) if ctx.eletype() else self.visit(ctx.arraytype())
        return ParamDecl(ident, eletype, out, inherited)

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr1(0))
        left = self.visit(ctx.expr1(0))
        right = self.visit(ctx.expr1(1))
        op = ctx.CONCAT().getText()
        return BinExpr(op, left, right)

    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr2(0))
        return BinExpr(self.visit(ctx.compare()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))

    def visitCompare(self, ctx: MT22Parser.CompareContext):
        if ctx.EQUAL_TO():
            return ctx.EQUAL_TO().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        elif ctx.GTE():
            return ctx.GTE().getText()

    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())
        if ctx.AND():
            return BinExpr(ctx.AND().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        elif ctx.OR():
            return BinExpr(ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr4())
        if ctx.PLUS():
            return BinExpr(ctx.PLUS().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        elif ctx.MINUS():
            return BinExpr(ctx.MINUS().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr5())
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))

    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        # expr5: NOT expr5 | expr6;
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr6())
        return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))

    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr7())
        return UnExpr(ctx.MINUS().getText(), self.visit(ctx.expr6()))

    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        ident = ctx.IDENTIFIER().getText()
        exp = self.visit(ctx.exprlist())
        return ArrayCell(ident, exp) 

    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        else:
            return self.visit(ctx.expr())

    def visitFactor(self, ctx: MT22Parser.FactorContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.IDENTIFIER():
            return Id(str(ctx.IDENTIFIER().getText()))
        elif ctx.funccall():
            return self.visit(ctx.funccall())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.BOOLEANLIT():
            return BooleanLit(True if ctx.BOOLEANLIT().getText() == "true" else False)

    def visitArrayCell(self, ctx: MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)

    def visitFunccall(self, ctx: MT22Parser.FunccallContext):
        if ctx.specialFunction():
            ident, expr = self.visit(ctx.specialFunction())
            if expr is not None:
                expr = expr if isinstance(expr, list) else [expr]
            return FuncCall(ident, expr if expr is not None else [])
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.doWhileStmt():
            return self.visit(ctx.doWhileStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        lst = self.visit(ctx.vardecl())
        return lst

    def visitAssignStmt(self, ctx: MT22Parser.AssignStmtContext):
        lhs = self.visit(ctx.lhs())
        expr = self.visit(ctx.expr())
        return AssignStmt(lhs, expr)

    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        ident = ctx.IDENTIFIER().getText()
        expr = self.visit(ctx.exprlist())
        return ArrayCell(ident, expr)

    def visitStmtlocal(self, ctx: MT22Parser.StmtlocalContext):
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx: MT22Parser.IfStmtContext):
        expr = self.visit(ctx.expr())

        if ctx.getChildCount() == 3:
            stmt = self.visit(ctx.stmtlocal(0))
            return IfStmt(expr, stmt)

        left = self.visit(ctx.stmtlocal(0))
        right = self.visit(ctx.stmtlocal(1))
        return IfStmt(expr, left, right)

    def visitForStmt(self, ctx: MT22Parser.ForStmtContext):
        initexp = self.visit(ctx.initExpr())
        conditionExpr = self.visit(ctx.conditionExpr())
        updateExpr = self.visit(ctx.updateExpr())
        stmt = self.visit(ctx.stmtlocal())
        return ForStmt(initexp, conditionExpr, updateExpr, stmt)

    def visitInitExpr(self, ctx: MT22Parser.InitExprContext):
        return AssignStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr()))

    def visitConditionExpr(self, ctx: MT22Parser.ConditionExprContext):
        return BinExpr(self.visit(ctx.operator()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))

    def visitOperator(self, ctx: MT22Parser.OperatorContext):
        if ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.EQUAL_TO():
            return ctx.EQUAL_TO().getText()
        elif ctx.GTE():
            return ctx.GTE().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        return ctx.NOT_EQUAL().getText()

    def visitUpdateExpr(self, ctx: MT22Parser.UpdateExprContext):
        return self.visit(ctx.expr())

    def visitWhileStmt(self, ctx: MT22Parser.WhileStmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmtlocal())
        return WhileStmt(expr, stmt)

    def visitDoWhileStmt(self, ctx: MT22Parser.DoWhileStmtContext):
        # doWhileStmt: DO blockStmt WHILE expr SEMI;
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockStmt()))

    def visitCallStmt(self, ctx: MT22Parser.CallStmtContext):
        if ctx.specialFunction():
            ident, expr = self.visit(ctx.specialFunction())
            if expr is not None:
                expr = expr if isinstance(expr, list) else [expr]
            return CallStmt(ident, expr if expr is not None else [])
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.exprlist()) if ctx.exprlist() else [])

    def visitBlockStmt(self, ctx: MT22Parser.BlockStmtContext):
        return BlockStmt(self.visit(ctx.stmtTerm()))

    def visitStmtTerm(self, ctx: MT22Parser.StmtTermContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtList())

    def visitStmtList(self, ctx: MT22Parser.StmtListContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt()) if isinstance(self.visit(ctx.stmt()), list) else [self.visit(ctx.stmt())]
        local = self.visit(ctx.stmt()) if isinstance(
            self.visit(ctx.stmt()), list) else [self.visit(ctx.stmt())]
        return local + self.visit(ctx.stmtList())

    def visitBreakStmt(self, ctx: MT22Parser.BreakStmtContext):
        return BreakStmt()

    def visitContinueStmt(self, ctx: MT22Parser.ContinueStmtContext):
        return ContinueStmt()

    def visitReturnStmt(self, ctx: MT22Parser.ReturnStmtContext):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)
    
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        ident = ctx.IDENTIFIER().getText()
        rettype = self.visit(ctx.returnType())
        param_list = self.visit(ctx.paramterList())
        inherits = self.visit(ctx.inheritance()) if ctx.inheritance() else None
        blockStmt = self.visit(ctx.blockStmt())
        return FuncDecl(ident, rettype, param_list, inherits, blockStmt)

    def visitInheritance(self, ctx: MT22Parser.InheritanceContext):
        if ctx.getChildCount() == 0:
            return None
        return ctx.IDENTIFIER().getText()

    def visitParamterList(self, ctx: MT22Parser.ParamterListContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramterListTerm())

    def visitParamterListTerm(self, ctx: MT22Parser.ParamterListTermContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.paramterListTerm())

    def visitReturnType(self, ctx: MT22Parser.ReturnTypeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.arraytype():
            return self.visit(ctx.arraytype())
        return BooleanType()

    def visitSpecialFunction(self, ctx: MT22Parser.SpecialFunctionContext):
        return self.visitChildren(ctx)

    def visitReadInteger(self, ctx: MT22Parser.ReadIntegerContext):
        return ctx.READINTEGER().getText(), None

    def visitPrintInteger(self, ctx: MT22Parser.PrintIntegerContext):
        return ctx.PRINTINTEGER().getText(), self.visit(ctx.expr())

    def visitReadFloat(self, ctx: MT22Parser.ReadFloatContext):
        return ctx.READFLOAT().getText(), None

    def visitWriteFloat(self, ctx: MT22Parser.WriteFloatContext):
        return ctx.WRITEFLOAT().getText(), self.visit(ctx.expr())

    def visitPrintBoolean(self, ctx: MT22Parser.PrintBooleanContext):
        return ctx.PRINTBOOLEAN().getText(), None

    def visitReadString(self, ctx: MT22Parser.ReadStringContext):
        return ctx.READSTRING().getText(), None

    def visitPrintString(self, ctx: MT22Parser.PrintStringContext):
        return ctx.PRINTSTRING().getText(), self.visit(ctx.expr())

    def visitSuperCall(self, ctx: MT22Parser.SuperCallContext):
        return ctx.SUPER().getText(), self.visit(ctx.exprlist())

    def visitPreDefault(self, ctx: MT22Parser.PreDefaultContext):
        return ctx.PREVENTDEFAULT().getText(), None