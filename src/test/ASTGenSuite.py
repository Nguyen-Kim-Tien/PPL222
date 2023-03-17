import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test1(self):
        input = """x,y: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))


    def test2(self):
        input = """x,y,z: integer = 1,2,3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))


    def test3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))


    def test4(self):
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))


    def test5(self):
        input = """
                foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
                main: function void () {
                    printInteger(4);
}"""
        expect = """Program([
\tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
\tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))


    def test6(self):
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))


    def test7(self):
        input = """ func: function integer(){
            a=b+1;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))


    def test8(self):
        input = """ func: function integer(){
            a[1,2,3]=4.5;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), FloatLit(4.5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))


    def test9(self):
        input = """func: function integer(){
            a[1,2,3]=4.5+b[1,2];
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, FloatLit(4.5), ArrayCell(b, [IntegerLit(1), IntegerLit(2)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))


    def test10(self):
        input = """ a : integer = {1,2,3}; """
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))


    def test11(self):
        input = """func: function integer(){
            a[1,2,3]=(4.5+8*9)+10;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, BinExpr(+, FloatLit(4.5), BinExpr(*, IntegerLit(8), IntegerLit(9))), IntegerLit(10)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))


    def test12(self):
        input = """func: function integer(){
            a=a::b;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))


    def test13(self):
        input = """func: function integer(){
            a=(true && false) || true;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, BooleanLit(True), BooleanLit(False)), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))


    def test14(self):
        input = """func: function integer(){
            a=a%3;
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(%, Id(a), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))


    def test15(self):
        input = """func: function integer(){
            a=print(4);
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), FuncCall(print, [IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))


    def test16(self):
        input = """ func: function integer(){
            a={1,2,3}/4;
            } """
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))


    def test17(self):
        input = """func: function integer(){
            a={1,2,3}/4;
            print(5);
            } """
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(4))), CallStmt(print, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))


    def test18(self):
        input = """func: function void(a:integer){
                  a=-3;
            } """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))


    def test19(self):
        input = """func: function void(a:integer){
                  a=-3+{1,2,3};
            }  """
        expect = """Program([
	FuncDecl(func, VoidType, [Param(a, IntegerType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, UnExpr(-, IntegerLit(3)), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))


    def test20(self):
        input = """ main:function void(){
            a=!true &&false;
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, UnExpr(!, BooleanLit(True)), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))


    def test21(self):
        input = """ main:function void(){if(a == 1){}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))


    def test22(self):
        input = """main:function void(){a="abc"::3.3E-4;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, StringLit(abc), FloatLit(0.00033)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))
    
    
    def test23(self):
        input = """ main:function void(){
                        if(a == 1) 
                            a=3;
                        else
                            a=4;   
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(3)), AssignStmt(Id(a), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    
    
    def test24(self):
        input = """  main:function void(){
                        if((a == 1)  && true) 
                           {
                               a=2;
                           }
                        else
                            {a=4;} }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(&&, BinExpr(==, Id(a), IntegerLit(1)), BooleanLit(True)), BlockStmt([AssignStmt(Id(a), IntegerLit(2))]), BlockStmt([AssignStmt(Id(a), IntegerLit(4))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))
    
    
    def test25(self):
        input = """main:function void(){
                        if(a == 1) 
                            a=3;
                        if(true && false)
                            x=y-4;
                        else
                            a=4;   
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), AssignStmt(Id(a), IntegerLit(3))), IfStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), AssignStmt(Id(x), BinExpr(-, Id(y), IntegerLit(4))), AssignStmt(Id(a), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))
    
    
    def test26(self):
        input = """ main:function void(){
                    for(i = 1, i < 4, i + 1) break;
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))
    
    
    def test27(self):
        input = """ main:function void(){\nfor(i = 1, i < 4, i + 1){}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))
    
    
    def test28(self):
        input = """ main:function void(){\n
                     while(true){
                         x[1,2]=3;
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    
    def test29(self):
        input = """ main:function void(){\n
                     while(true)
                        a=a+1;
                    }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    

    def test30(self):
        input = """ main:function void(){\n
                     while(true){
                         x[1,2]=3;
                         a="abc"::"cfe";
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([AssignStmt(ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), IntegerLit(3)), AssignStmt(Id(a), BinExpr(::, StringLit(abc), StringLit(cfe)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    
    
    def test31(self):
        input = """ main:function void(){\n
                     while(x<6){
                        {{}}
                     }
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(6)), BlockStmt([BlockStmt([BlockStmt([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))
    
    
    def test32(self):
        input = """ main:function void(){\n
                        x:integer;
                        x=x+1;
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    
    
    def test33(self):
        input = """ main:function void(){\n
                    do{
                        x:integer;
                        x=x+1;
                    }while(x==1);
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([VarDecl(x, IntegerType), AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    
    
    def test34(self):
        input = """ main:function void(){
                    while(a == 2){}
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    
    
    def test35(self):
        input = """main:function void(){\n
                    do{
                        x:integer=1;
                    }while((x==1) && (y<2));
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(1)), BinExpr(<, Id(y), IntegerLit(2))), BlockStmt([VarDecl(x, IntegerType, IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    
    
    def test36(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            break;
                        }
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    
    
    def test37(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            continue;
                        }
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    
    
    def test38(self):
        input = """  main:function void(){
                    do {{}}
                    while(a == 2);
                    }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([BlockStmt([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))
    
    
    def test39(self):
        input = """ main:function void(){
                    do {{i = 1; \n i = 2;}}
                    while(a == 2);} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([BlockStmt([AssignStmt(Id(i), IntegerLit(1)), AssignStmt(Id(i), IntegerLit(2))])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    
    
    def test40(self):
        input = """ main:function void(){
        do {{i = 1; \n {i = 2;}}}
        while(a == 2);} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(a), IntegerLit(2)), BlockStmt([BlockStmt([AssignStmt(Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), IntegerLit(2))])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))
    
    
    def test41(self):
        input = """ main:function void(){
                for(i = 1, i < 4, i + 1){
                    if (i == 1) {{\n}}}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([BlockStmt([])]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))
    
    
    def test42(self):
        input = """main:function void(){\n
                    while(a==3){
                        if(x==1){
                            return 0;
                        }
                    }
                        
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(==, Id(a), IntegerLit(3)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))
    
    
    def test43(self):
        input = """ main:function void(){
                    for(i = 1, i < 4, i + 1) 
                        for(j = 1, j < 5, j+1){}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    
    
    def test44(self):
        input = """ main:function void(){
            for(i = 1, i < 4, i + 1)
            {\n a= a + 1; \n a = 1;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    
    
    def test45(self):
        input = """ main:function void(){
                    for(i = 1, i < 4, i + 1) 
                        while(true){\n
                            if(true) break;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BooleanLit(True), BreakStmt())])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))
    
    
    def test46(self):
        input = """ main:function void(){\n
                    for(i = 1, i < 4, i + 1) 
                        while(true){\n 
                            a:integer = 1; \n 
                                if(true) 
                                    break; 
                    a = a + 1;}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), WhileStmt(BooleanLit(True), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), IfStmt(BooleanLit(True), BreakStmt()), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))
    
    
    def test47(self):
        input = """main:function void(){\n
                    x:float;
                    if(x<2) return 3;
                    return 0;                       
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType), IfStmt(BinExpr(<, Id(x), IntegerLit(2)), ReturnStmt(IntegerLit(3))), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))
    
    
    def test48(self):
        input = """main:function void(){\n
                    x:float=1.3;
                    print(x);
                    return 0;                       
                    }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), CallStmt(print, Id(x)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))
    
    
    def test49(self):
        input = """ main:function void(){\n
                    x:float=1.3;
                    print(x,"abv");
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), CallStmt(print, Id(x), StringLit(abv)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    
    
    def test50(self):
        input =  """ main:function void(){\n
                    x:float=1.3;
                    print(x,"abv",5,true,a[1,2]);
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), CallStmt(print, Id(x), StringLit(abv), IntegerLit(5), BooleanLit(True), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))
    
    
    def test51(self):
        input = """ a,b :integer = 3,2;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    
    def test52(self):
        input = """ a,b :auto; """
        expect = """Program([
	VarDecl(a, AutoType)
	VarDecl(b, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    
    
    def test53(self):
        input = """ a,b : auto = 1,3; """
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    
    
    def test54(self):
        input = """ a,b : integer = 1 + 2, 3+4; """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
	VarDecl(b, IntegerType, BinExpr(+, IntegerLit(3), IntegerLit(4)))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    
    
    def test55(self):
        input = """x,y:string;
                    a,b,c:float=1,2,4.e5;
                    d: array[1,2] of integer;"""
        expect = """Program([
	VarDecl(x, StringType)
	VarDecl(y, StringType)
	VarDecl(a, FloatType, IntegerLit(1))
	VarDecl(b, FloatType, IntegerLit(2))
	VarDecl(c, FloatType, FloatLit(400000.0))
	VarDecl(d, ArrayType([1, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    
    
    def test56(self):
        input = """ main:function void(inherit out x:float){\n
                    x:float=1.3;
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(x, FloatType)], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))
    
    
    def test57(self):
        input = """ main:function void( out x:float,y:integer){\n
                    x:float=1.3;
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [OutParam(x, FloatType), Param(y, IntegerType)], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    
    
    def test58(self):
        input = """ main:function void(inherit x:float,y:integer){\n
                    x:float=1.3;
                    return 0;                       
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [InheritParam(x, FloatType), Param(y, IntegerType)], None, BlockStmt([VarDecl(x, FloatType, FloatLit(1.3)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    
    
    def test59(self):
        input = """ a : auto = {1,2,3}; """
        expect = """Program([
	VarDecl(a, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    
    def test60(self):
        input = """ a, b : auto= {1,2,3},4; """
        expect = """Program([
	VarDecl(a, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(b, AutoType, IntegerLit(4))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
    
    def test61(self):
        input = """main:function void(){\nfor(i = 1, i < 4, i + 1) break;}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    
    
    def test62(self):
        input = """ main : function void(){\n
                    print(1);} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    
    def test63(self):
        input = """  inc : function void (out n : integer , delta : integer){\n} """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    
    
    def test64(self):
        input = """x: integer = 65;
                fact: function integer (n: integer) {
                    if (n == 0) return 1;
                        else return n * fact(n - 1);\n}
                inc: function void(out n: array [5] of integer, delta: integer) {
                    n = n + delta;\n}
                main: function void() {
                        delta: integer = fact(3);\
                        inc(x, delta);
                        printInteger(x);\n}"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, ArrayType([5], IntegerType)), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    
    
    def test65(self):
        input = """ main : function void(){
            \n \nreturn 0;\n } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    
    def test66(self):
        input = """ func: function integer(){\nbreak;\n}"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))
    
    
    def test67(self):
        input = """ a: float;"""
        expect = """Program([
	VarDecl(a, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    
    def test68(self):
        input = """ main : function void(){
                    foo(2 + x, 4.0 / y);
                    } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    
    def test69(self):
        input = """a,b,c,d,e,f,e,g,e,d : integer = 1,2,3,4,5,6,7,8,9,10;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(d, IntegerType, IntegerLit(4))
	VarDecl(e, IntegerType, IntegerLit(5))
	VarDecl(f, IntegerType, IntegerLit(6))
	VarDecl(e, IntegerType, IntegerLit(7))
	VarDecl(g, IntegerType, IntegerLit(8))
	VarDecl(e, IntegerType, IntegerLit(9))
	VarDecl(d, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
    
    def test70(self):
        input = """ gram : function integer(out a : integer) inherit func{} """
        expect = """Program([
	FuncDecl(gram, IntegerType, [OutParam(a, IntegerType)], func, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    
    
    def test71(self):
        input = """ main : function void(){
                \nfunc(func());} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(func, FuncCall(func, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    
    def test72(self):
        input = """ main : function void(){
                if(a == 1){
                    foo(x);}} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([CallStmt(foo, Id(x))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    
    def test73(self):
        input = """ main:function void(){
            for(i = 1, i < 4, i + 1) 
                if(i==4) 
                    while(true){}
        } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(4)), WhileStmt(BooleanLit(True), BlockStmt([]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    
    
    def test74(self):
        input = """ main : function void(){ 
                        a = 5 *6 /4;} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, BinExpr(*, IntegerLit(5), IntegerLit(6)), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    
    
    def test75(self):
        input = """ main : function void(){ 
                        return foo(1, a, b) + 1;} """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(+, FuncCall(foo, [IntegerLit(1), Id(a), Id(b)]), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    
    
    def test76(self):
        input = """ main : function void(){
            a = a :: b;
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    
    def test77(self):
        input = """a: string = "234"; """
        expect = """Program([
	VarDecl(a, StringType, StringLit(234))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    
    
    def test78(self):
        input = """main:function void(){if(a == 1){}}  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    
    def test79(self):
        input = """ a :float= {}; """
        expect = """Program([
	VarDecl(a, FloatType, ArrayLit([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))
    
    
    def test80(self):
        input = """ main : function void () {
                arr = {};
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    
    
    def test81(self):
        input = """ main : function void () {
                a : array [5] of integer;
            }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    
    
    def test82(self):
        input = """ main : function void () {
                        if(false){
                            print(6);
                        }
                }   """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(False), BlockStmt([CallStmt(print, IntegerLit(6))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    
    
    def test83(self):
        input = """  main : function void () {
                    a : array[5] of integer;
                }    """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))
    
    
    def test84(self):
        input = """ main : function void () {
                    a : auto = {5,1,2};
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, ArrayLit([IntegerLit(5), IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    
    
    def test85(self):
        input = """ main : function void () {
                    a ={{1,2,3}};
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    
    
    def test86(self):
        input = """ main : function void () {
                    a = {{1,2,3}};
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))
    
    
    def test87(self):
        input = """  main : function void () {
                    a = {{1,2,3}, {}};
                }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    
    
    def test88(self):
        input = """ x:boolean=true; """
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))
    
    
    def test89(self):
        input = """ main : function void () {
                    a = {{1,2,3}, {{}}};
                } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([ArrayLit([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))
    
    
    def test90(self):
        input = """ main : function void () {
                    a = {{{}}, {{}}, {{},{}}};
                }  """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([ArrayLit([ArrayLit([])]), ArrayLit([ArrayLit([])]), ArrayLit([ArrayLit([]), ArrayLit([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    
    def test91(self):
        input = """ 
                func1 : function array [5] of integer(){
                }
                """
        expect = """Program([
	FuncDecl(func1, ArrayType([5], IntegerType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    
    
    def test92(self):
        input = """
                func1 : function array [5] of integer(a : integer ){
                    return 1;
                }
                """
        expect = """Program([
	FuncDecl(func1, ArrayType([5], IntegerType), [Param(a, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    
    def test93(self):
        input = """
                func1 : function integer(a : array [5] of integer){
                    return 1;
                }
                """
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    
    
    def test94(self):
        input = """
                func1 : function integer(a : array [5] of integer){
                    return 1;
                }
                """
        expect = """Program([
	FuncDecl(func1, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    
    
    def test95(self):
        input = """a : integer = {1,2,3};"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    
    
    def test96(self):
        input = """a12 : array [1] of integer = {1,2};"""
        expect = """Program([
	VarDecl(a12, ArrayType([1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    
    def test97(self):
        input = """
        x : integer = 1;
        x ,z:float =1.e-5,4.9;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(x, FloatType, FloatLit(1e-05))
	VarDecl(z, FloatType, FloatLit(4.9))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))



    def test98(self):
        input = """
            x : integer;
            main : function void () {
                count(1+1,1*2);} 
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(count, BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(*, IntegerLit(1), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))



    def test99(self):
        input = """
            main : function void (x: string) {}
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(x, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))



    def test100(self):
        input = """
            arr : array [5] of integer = {---5, foo(), a && b};
        """
        expect = """Program([
	VarDecl(arr, ArrayType([5], IntegerType), ArrayLit([UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(5)))), FuncCall(foo, []), BinExpr(&&, Id(a), Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 400))


