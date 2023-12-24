class SyntaxAnalyzer():
    def __init__(self,File):
        self.File=File
        self.Head=0
        self.Lookahead=self.File[self.Head]  
    
    
    
    def Match(self,Var):
        if Var == "<Var":
            if self.Lookahead[:4]==Var:
                self.Head+=1
                if self.Head == len(self.File):
                    self.Lookahead="$"
                else:
                    self.Lookahead=self.File[self.Head]
            return True
        else: 
            if self.Lookahead==Var:
                self.Head+=1
                if self.Head == len(self.File):
                    self.Lookahead="$"
                else:
                    self.Lookahead=self.File[self.Head]
                return True
            else:
                print("SyntaxError")
                exit()



    def S(self):
        if (self.Lookahead=="<If>" or self.Lookahead=="<For>" or self.Lookahead=="<Call>" or self.Lookahead=="<Def>" or self.Lookahead=="<Output>"):
            self.Syntax()      
        elif (len(self.Lookahead)>=6 and self.Lookahead[:4]=="<Var"):
            self.Assignment()
        else:
            print("SyntaxError")
            exit()


    
    def Syntax(self):
        if (self.Lookahead=="<If>"):
            self.Match("<If>")
            self.Match("<(>")
            self.Compare()
            self.Match("<)>")
            self.Match("<{>")
            self.S()
            self.Match("<}>")
            self.IfCondition()
            
        elif (self.Lookahead=="<For>"):
            self.Match("<For>")
            self.Match("<(>")
            self.Assignment()
            self.Match("<;>")
            self.Action()
            self.Match("<;>")
            self.Compare()
            self.Match("<)>")
            self.Match("<{>")
            self.S()
            self.Match("<}>")
            
        elif (self.Lookahead=="<Call>"):
            self.Match("<Call>")
            self.Match("<DefName>")
            self.Match("<(>")
            self.Caller()
            self.Match("<)>")
            
        elif (self.Lookahead=="<Def>"):
            self.Match("<Def>")
            self.Match("<DefName>")
            self.Match("<(>")
            self.Caller()
            self.Match("<)>")
            self.Match("<{>")
            while self.Lookahead!="<}>":
                self.S()
            self.Match("<}>")
            
        elif (self.Lookahead=="<Output>"):
            self.Match("<Output>")
            self.Match("<(>")
            self.Match("<Var")
            self.Match("<)>")
            
        else:
            print("SyntaxError")
            exit()



    def IfCondition(self):
        if (self.Lookahead=="<Elseif>"):
            self.Match("<Elseif>")
            self.Match("<(>")
            self.Compare()
            self.Match("<)>")
            self.Match("<{>")
            self.S()
            self.Match("<}>")
            self.ElseifCondition()

        elif (self.Lookahead=="<Else>"):
            self.Match("<Else>")
            self.Match("<(>")
            self.Compare()
            self.Match("<)>")
            self.Match("<{>")
            self.S()
            self.Match("<}>")
        
        else:
            return

            
            
    def ElseifCondition(self):
        if (self.Lookahead=="<Else>"):
            self.Match("<Else>")
            self.Match("<{>")
            self.S()
            self.Match("<}>")
        
        else:
            return



    def Caller(self):
        self.Variable()
        self.MultiCaller()
        
        

    def MultiCaller(self):
        if self.Lookahead=="<,>":
            self.Match("<,>")
            self.Caller()
            
        else:
            return



    def Assignment(self):
        self.Match("<Var")
        self.Match("<=>")
        self.VarAssignment()



    def VarAssignment(self):
        if ((len(self.Lookahead)>=6 and self.Lookahead[:4]=="<Var") or self.Lookahead=="<Int>" or self.Lookahead=="<Float>" or self.Lookahead=="<String>"):
            self.Variable()
            self.X()
            
        elif (self.Lookahead=="<Input>"):
            self.Match("<Input>")
            self.Match("<(>")
            self.Match("<)>")
        
        else:
            print("SyntaxError")
            exit()



    def X(self):
        if (self.Lookahead=="<+>" or self.Lookahead=="<->" or self.Lookahead=="<*>" or self.Lookahead=="</>" or self.Lookahead=="<^>" or self.Lookahead=="<++>" or self.Lookahead=="<-->"):
            self.Op()
        else:
            return

    def Action(self):
        self.Variable()
        self.Op()

    def Op(self):
        if (self.Lookahead=="<+>"):
            self.Match("<+>")
            self.Variable()
            
        elif (self.Lookahead=="<->"):
            self.Match("<->")
            self.Variable()
            
        elif (self.Lookahead=="<*>"):
            self.Match("<*>")
            self.Variable()
            
        elif (self.Lookahead=="</>"):
            self.Match("</>")
            self.Variable()
            
        elif (self.Lookahead=="<^>"):
            self.Match("<^>")
            self.Variable()
            
        elif (self.Lookahead=="<++>"):
            self.Match("<++>")
            
        elif (self.Lookahead=="<-->"):
            self.Match("<-->")
        
        else:
            print("SyntaxError")
            exit()
    


    def Compare(self):
        self.Variable()
        self.Comparator()
        self.Variable()
        
        

    def Comparator(self):
        if (self.Lookahead=="<Equal>"):
            self.Match("<Equal>")
            
        elif (self.Lookahead=="<SmallerEqual>"):
            self.Match("<SmallerEqual>")
            
        elif (self.Lookahead=="<BiggerEqual>"):
            self.Match("<BiggerEqual>")
            
        elif (self.Lookahead=="<Smaller>"):
            self.Match("<Smaller>")
            
        elif (self.Lookahead=="<Bigger>"):
            self.Match("<Bigger>")
        
        else:
            print("SyntaxError")
            exit()



    def Variable(self):
        if ((len(self.Lookahead)>=6 and self.Lookahead[:4]=="<Var")):
            self.Match("<Var")
            
        elif (self.Lookahead=="<Int>"):
            self.Match("<Int>")
            
        elif (self.Lookahead=="<Float>"):
            self.Match("<Float>")
            
        elif (self.Lookahead=="<String>"):
            self.Match("<String>")
            
        else:
            print("SyntaxError")
            exit()
            
            
            
def Run():
    with open("Token.txt",'r') as r_input:
        File=r_input.read()
    File=File.split()
    Analyzed_file=SyntaxAnalyzer(File)
    while Analyzed_file.Lookahead!="$":
        Analyzed_file.S() 
    print("SYntax is OK")       