
def GetToken(Lexim):
    case=0
    i=0
    while True:
        match case:
            case 0:
                if((Lexim[i]>='0' and Lexim[i]<='9') and i<len(Lexim)):
                    i+=1
                    case="intnumber"
                elif(Lexim[i]=="_" and i<len(Lexim)):
                    i+=1
                    case="var1"
                elif(Lexim[i]=="p" and i<len(Lexim)):
                    i+=1
                    case="if1"
                elif(Lexim[i]=="b" and i<len(Lexim)):
                    i+=1
                    case="else_if1"
                elif(Lexim[i]=="j" and i<len(Lexim)):
                    i+=1
                    case="else1"
                elif(Lexim[i]=="n" and i<len(Lexim)):
                    i+=1
                    case="for1"
                elif(Lexim[i]=="d" and i<len(Lexim)):
                    i+=1
                    case="d_checker"
                elif(Lexim[i]=="e" and i<len(Lexim)):
                    i+=1
                    case="output1"
                elif(Lexim[i]=='"' and i<len(Lexim)):
                    i+=1
                    case="string1"
                elif(Lexim[i]=="$" and i<len(Lexim)):
                    i+=1
                    case="def_name1"    
                else:
                    case="operations"
                    
            # ----------------------------
            
            case "d_checker":
                if (Lexim[i]=="a" and i<len(Lexim)):
                    i=i+1
                    case="def1"
                elif (Lexim[i]=="o" and i<len(Lexim)):
                    i=i+1
                    case="input1"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "var1":
                if(Lexim[i]=="1" and i<len(Lexim)):
                    i+=1
                    case="var2"
                else:
                    return "EROR"
            case "var2":
                if(Lexim[i]=="5" and i<len(Lexim)):
                    i+=1
                    case="var3"
                else:
                    return "EROR"
            case "var3":
                if(Lexim[i]=="_" and i<len(Lexim)):
                    i+=1
                    case="var4"
                else:
                    return "EROR"
            
            case "var4":
                if (i==len(Lexim))and (i>4):
                    return "<Var> "
                elif (Lexim[i]>='0' and Lexim[i]<='9') or (Lexim[i]>="A" and Lexim[i]<="Z") or (Lexim[i]>="a" and Lexim[i]<="z") or (Lexim[i]=="_"):
                    i+=1
                    case="var4"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "if1":
                if(Lexim[i]=="o" and i<len(Lexim)):
                    i+=1
                    case="if2"
                else:
                    return "EROR"
            case "if2":
                if(Lexim[i]=="l" and i<len(Lexim)):
                    i+=1
                    case="if3"
                else:
                    return "EROR"
            case "if3":
                if(Lexim[i]=="_" and i<len(Lexim)):
                    i+=1
                    case="if4"
                else:
                    return "EROR"
            case "if4":
                if(Lexim[i]=="s" and i<len(Lexim)):
                    i+=1
                    case="if5"
                else:
                    return "EROR"
            case "if5":
                if(Lexim[i]=="e" and i<len(Lexim)):
                    i+=1
                    case="if6"
                else:
                    return "EROR"
            case "if6":
                if(Lexim[i]=="r" and i<len(Lexim)):
                    i+=1
                    case="if7"
                else:
                    return "EROR"
            case "if7":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="if8"
                else:
                    return "EROR"
            case "if8":
                if(Lexim[i]=="t" and i<len(Lexim)):
                    i+=1
                    case="if9"
                else:
                    return "EROR"
            case "if9":
                if(i==len(Lexim)):
                    return "<If> "
                else:
                    return "EROR"
            
            # ----------------------------
                
            case "else_if1":
                if(Lexim[i]=="e" and i<len(Lexim)):
                    i+=1
                    case="else_if2"
                else:
                    return "EROR"
            case "else_if2":
                if(Lexim[i]=="h" and i<len(Lexim)):
                    i+=1
                    case="else_if3"
                else:
                    return "EROR"
            case "else_if3":
                if(Lexim[i]=="e" and i<len(Lexim)):
                    i+=1
                    case="else_if4"
                else:
                    return "EROR"
            case "else_if4":
                if(Lexim[i]=="s" and i<len(Lexim)):
                    i+=1
                    case="else_if5"
                else:
                    return "EROR"
            case "else_if5":
                if(Lexim[i]=="h" and i<len(Lexim)):
                    i+=1
                    case="else_if6"
                else:
                    return "EROR"
            case "else_if6":
                if(Lexim[i]=="t" and i<len(Lexim)):
                    i+=1
                    case="else_if7"
                else:
                    return "EROR"
            case "else_if7":
                if(i==len(Lexim)):
                    return "<Elseif> "
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "else1":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="else2"
                else:
                    return "EROR"
            case "else2":
                if(Lexim[i]=="h" and i<len(Lexim)):
                    i+=1
                    case="else3"
                else:
                    return "EROR"
            case "else3":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="else4"
                else:
                    return "EROR"
            case "else4":
                if(Lexim[i]=="n" and i<len(Lexim)):
                    i+=1
                    case="else5"
                else:
                    return "EROR"
            case "else5":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="else6"
                else:
                    return "EROR"
            case "else6":
                if(Lexim[i]=="m" and i<len(Lexim)):
                    i+=1
                    case="else7"
                else:
                    return "EROR"
            case "else7":
                if(i==len(Lexim)):
                    return "<Else> "
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "for1":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="for2"
                else:
                    return "EROR"
            case "for2":
                if(Lexim[i]=="m" and i<len(Lexim)):
                    i+=1
                    case="for3"
                else:
                    return "EROR"
            case "for3":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="for4"
                else:
                    return "EROR"
            case "for4":
                if(Lexim[i]=="z" and i<len(Lexim)):
                    i+=1
                    case="for5"
                else:
                    return "EROR"
            case "for5":
                if(i==len(Lexim)):
                    return "<For> "
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "def1":
                if(Lexim[i]=="s" and i<len(Lexim)):
                    i+=1
                    case="def2"
                else:
                    return "EROR"
            case "def2":
                if(Lexim[i]=="t" and i<len(Lexim)):
                    i+=1
                    case="def3"
                else:
                    return "EROR"
            case "def3":
                if(Lexim[i]=="o" and i<len(Lexim)):
                    i+=1
                    case="def4"
                else:
                    return "EROR"
            case "def4":
                if(Lexim[i]=="o" and i<len(Lexim)):
                    i+=1
                    case="def5"
                else:
                    return "EROR"
            case "def5":
                if(Lexim[i]=="r" and i<len(Lexim)):
                    i+=1
                    case="def6"
                else:
                    return "EROR"
            case "def6":
                if (i==len(Lexim)):
                    return "<Call> " 
                elif(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="def7"
                else:
                    return "EROR"
            case "def7":
                if(Lexim[i]=="t" and i<len(Lexim)):
                    i+=1
                    case="def8"
                else:
                    return "EROR"
            case "def8":
                if(Lexim[i]=="_" and i<len(Lexim)):
                    i+=1
                    case="def9"
                else:
                    return "EROR"
            case "def9":
                if(Lexim[i]=="e" and i<len(Lexim)):
                    i+=1
                    case="def10"
                else:
                    return "EROR"
            case "def10":
                if(Lexim[i]=="l" and i<len(Lexim)):
                    i+=1
                    case="def11"
                else:
                    return "EROR"
            case "def11":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="def12"
                else:
                    return "EROR"
            case "def12":
                if(Lexim[i]=="h" and i<len(Lexim)):
                    i+=1
                    case="def13"
                else:
                    return "EROR"
            case "def13":
                if(Lexim[i]=="i" and i<len(Lexim)):
                    i+=1
                    case="def14"
                else:
                    return "EROR"
            case "def14":
                if(i==len(Lexim)):
                    return"<Def> "
                else:
                    return "EROR"
                
            # ----------------------------
            
            case "def_name1":
                if i<len(Lexim):
                    if (Lexim[i]>='0' and Lexim[i]<='9') or (Lexim[i]>="A" and Lexim[i]<="Z") or (Lexim[i]>="a" and Lexim[i]<="z") or (Lexim[i]=="_"):
                        i+=1
                        case="def_name2"
                else:
                    return "EROR"
                
            case "def_name2":
                if i==len(Lexim):
                    return "<DefName> "
                elif (Lexim[i]>='0' and Lexim[i]<='9') or (Lexim[i]>="A" and Lexim[i]<="Z") or (Lexim[i]>="a" and Lexim[i]<="z") or (Lexim[i]=="_"):
                    i+=1
                    case="def_name2"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "input1":
                if (Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="input2"
                else:
                    return "EROR"
            case "input2":
                if (i==len(Lexim)):
                    return("<Input> ")
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "output1":
                if(Lexim[i]=="j" and i<len(Lexim)):
                    i+=1
                    case="output2"
                else:
                    return "EROR"
            case "output2":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="output3"
                else:
                    return "EROR"
            case "output3":
                if(Lexim[i]=="b" and i<len(Lexim)):
                    i+=1
                    case="output4"
                else:
                    return "EROR"
            case "output4":
                if(Lexim[i]=="a" and i<len(Lexim)):
                    i+=1
                    case="output5"
                else:
                    return "EROR"
            case "output5":
                if(Lexim[i]=="t" and i<len(Lexim)):
                    i+=1
                    case="output6"
                else:
                    return "EROR"
            case "output6":
                if(i==len(Lexim)):
                    return "<Output> "
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "string1" :
                if ((Lexim[i] =='"') and (i==len(Lexim)-1)):
                    return "<String> "
                elif i<len(Lexim):
                    i+=1
                    case="string1"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "intnumber" :
                if i<len(Lexim):
                    if (Lexim[i]>='0' and Lexim[i]<='9'):
                        i+=1 
                        case="intnumber"
                    elif Lexim[i]=='.':
                        i+=1
                        case="floatnumber1"
                elif i==len(Lexim):
                    return "<Int> "
                else:
                    return "EROR"
                
            case "floatnumber1" :
                if i<len(Lexim):
                    if (Lexim[i]>='0' and Lexim[i]<='9'):
                        i+=1 
                        case="floatnumber2"
                else:
                    return "EROR"
                    
            case "floatnumber2" :
                if i==len(Lexim):
                    return "<Float> "
                elif (Lexim[i]>='0' and Lexim[i]<='9') and i<len(Lexim):
                    i+=1 
                    case="floatnumber2"
                else:
                    return "EROR"
            # ---------------------------- 
            
            case "operations":
                if Lexim[i]=="," and len(Lexim)==1:
                    return "<,> "
                elif Lexim[i]=="+" and len(Lexim)==1:
                    return "<+> "
                elif Lexim[i]=="-" and len(Lexim)==1:
                    return "<-> "
                elif Lexim[i]=="*" and len(Lexim)==1:
                    return "<*> "
                elif Lexim[i]=="/" and len(Lexim)==1:
                    return "</> "
                elif Lexim[i]=="^" and len(Lexim)==1:
                    return "<^> "
                elif Lexim[i]=="+" and len(Lexim)==2:
                    if Lexim[i+1]=="+":
                        return "<++> "
                elif Lexim[i]=="-" and len(Lexim)==2:
                    if Lexim[i+1]=="-" :
                        return "<--> "
                elif Lexim[i]=="=" and len(Lexim)==1:
                    return "<=> " 
                elif Lexim[i]=="=" and len(Lexim)==2:
                    if Lexim[i+1]=="=":
                        return "<Equal> " 
                elif Lexim[i]=="<" and len(Lexim)==2:
                    if Lexim[i+1]=="=":
                        return "<SmallerEqual> " 
                elif Lexim[i]==">" and len(Lexim)==2:
                    if  Lexim[i+1]=="=":
                        return "<BiggerEqual> " 
                elif Lexim[i]==">" and len(Lexim)==1:
                    return "<Bigger> " 
                elif Lexim[i]=="<" and len(Lexim)==1:
                    return "<Smaller> "
                elif Lexim[i]=="(" and len(Lexim)==1:
                    return "<(> "
                elif Lexim[i]==")" and len(Lexim)==1:
                    return "<)> "
                elif Lexim[i]==";" and len(Lexim)==1:
                    return "<;> "
                elif Lexim[i]=="{" and len(Lexim)==1:
                    return "<{> "
                elif Lexim[i]=="}" and len(Lexim)==1:
                    return "<}> "
                else:
                    return "EROR"
                

        
        
        
        
# ===============================================
# ==================== main: ====================


def Run():
    var_index=0
    varubales=[] # for repeatedly var's
    with open("input.txt",'r') as r_input: 
        line_len=len(r_input.readlines())
        
    open('Token.txt', 'w').close() # clear Token.txt file
    w_output=open("Token.txt","w")
    with open("input.txt",'r') as r_input:
        for i in range(line_len):
            input_line=r_input.readline()
            input_line=input_line.split()
            for j in range(len(input_line)):
                Token=GetToken(input_line[j])
                #GetToken returns : 
                #<Var>
                #<If>
                #<Elseif>
                #<Else>
                #<For>
                #<Call>
                #<Def>
                #<Input>
                #<Output>
                #operation tokens:  #<+> <-> <*> </> <^> <++> <--> <=>
                                    #<Equal> <SmallerEqual> <BiggerEqual> <Smaller> <Bigger>
                # EROR
                if Token=="EROR":
                    print("Lexim EROR in line ",i)
                    # exit()
                elif Token=="<Var> ":
                    Is=False
                    for i in range (len(varubales)):
                        if input_line[j]==varubales[i]:
                            Is=True
                            Token="<Var"+str(i)+"> "
                            break
                    if Is==False:
                        Token="<Var"+str(var_index)+"> "
                        varubales.append(input_line[j])
                        var_index+=1
                        
                w_output.write(Token)
            w_output.write("\n")
            
    return  
        
        
