def GetToken(Lexim):
    case=0
    i=0
    while True:
        match case:
            case 0:
                if(Lexim[i]=="1"):
                    i+=1
                    case="var1"
                elif(Lexim[i]=="p"):
                    i+=1
                    case="if1"
                elif(Lexim[i]=="b"):
                    i+=1
                    case="else_if1"
                elif(Lexim[i]=="j"):
                    i+=1
                    case="else1"
                elif(Lexim[i]=="n"):
                    i+=1
                    case="for1"
                elif(Lexim[i]=="d"):
                    i+=1
                    case="d_checker"
                elif(Lexim[i]=="e"):
                    i+=1
                    case="output1"
                else:
                    # case="operations"
                    return "EROR"
            # ----------------------------
            
            case "d_checker":
                if (Lexim[i]=="a"):
                    i=i+1
                    case="def1"
                elif (Lexim[i]=="o"):
                    i=i+1
                    case="input1"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "var1":
                if(Lexim[i]=="5"):
                    i+=1
                    case="var2"
                else:
                    return "EROR"
            case "var2":
                if(Lexim[i]=="_"):
                    i+=1
                    case="var3"
                else:
                    return "EROR"
            
            case "var3":
                if (Lexim[i]>='0' and Lexim[i]<='9') or (Lexim[i]>="A" and Lexim[i]<="Z") or (Lexim[i]>="a" and Lexim[i]<="z") or (Lexim[i]=="_"):
                    i+=1
                    case="var4"
                else:
                    return "EROR"
            case "var4":
                if (i==len(Lexim)):
                    return "<VarToken>"
                elif (Lexim[i]>='0' and Lexim[i]<='9') or (Lexim[i]>="A" and Lexim[i]<="Z") or (Lexim[i]>="a" and Lexim[i]<="z") or (Lexim[i]=="_"):
                    i+=1
                    case="var4"
                else:
                    return "EROR"
            # ----------------------------
            
            case "if1":
                if(Lexim[i]=="o"):
                    i+=1
                    case="if2"
                else:
                    return "EROR"
            case "if2":
                if(Lexim[i]=="l"):
                    i+=1
                    case="if3"
                else:
                    return "EROR"
            case "if3":
                if(Lexim[i]=="_"):
                    i+=1
                    case="if4"
                else:
                    return "EROR"
            case "if4":
                if(Lexim[i]=="s"):
                    i+=1
                    case="if5"
                else:
                    return "EROR"
            case "if5":
                if(Lexim[i]=="e"):
                    i+=1
                    case="if6"
                else:
                    return "EROR"
            case "if6":
                if(Lexim[i]=="r"):
                    i+=1
                    case="if7"
                else:
                    return "EROR"
            case "if7":
                if(Lexim[i]=="a"):
                    i+=1
                    case="if8"
                else:
                    return "EROR"
            case "if8":
                if(Lexim[i]=="t"):
                    i+=1
                    case="if9"
                else:
                    return "EROR"
            case "if9":
                if(i==len(Lexim)):
                    return "<IfToken>"
                else:
                    return "EROR"
            
            # ----------------------------
                
            case "else_if1":
                if(Lexim[i]=="e"):
                    i+=1
                    case="else_if2"
                else:
                    return "EROR"
            case "else_if2":
                if(Lexim[i]=="h"):
                    i+=1
                    case="else_if3"
                else:
                    return "EROR"
            case "else_if3":
                if(Lexim[i]=="e"):
                    i+=1
                    case="else_if4"
                else:
                    return "EROR"
            case "else_if4":
                if(Lexim[i]=="s"):
                    i+=1
                    case="else_if5"
                else:
                    return "EROR"
            case "else_if5":
                if(Lexim[i]=="h"):
                    i+=1
                    case="else_if6"
                else:
                    return "EROR"
            case "else_if6":
                if(Lexim[i]=="t"):
                    i+=1
                    case="else_if7"
                else:
                    return "EROR"
            case "else_if7":
                if(i==len(Lexim)):
                    return "<ElseifToken>"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "else1":
                if(Lexim[i]=="a"):
                    i+=1
                    case="else2"
                else:
                    return "EROR"
            case "else2":
                if(Lexim[i]=="h"):
                    i+=1
                    case="else3"
                else:
                    return "EROR"
            case "else3":
                if(Lexim[i]=="a"):
                    i+=1
                    case="else4"
                else:
                    return "EROR"
            case "else4":
                if(Lexim[i]=="n"):
                    i+=1
                    case="else5"
                else:
                    return "EROR"
            case "else5":
                if(Lexim[i]=="a"):
                    i+=1
                    case="else6"
                else:
                    return "EROR"
            case "else6":
                if(Lexim[i]=="m"):
                    i+=1
                    case="else7"
                else:
                    return "EROR"
            case "else7":
                if(i==len(Lexim)):
                    return "<ElseToken>"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "for1":
                if(Lexim[i]=="a"):
                    i+=1
                    case="for2"
                else:
                    return "EROR"
            case "for2":
                if(Lexim[i]=="m"):
                    i+=1
                    case="for3"
                else:
                    return "EROR"
            case "for3":
                if(Lexim[i]=="a"):
                    i+=1
                    case="for4"
                else:
                    return "EROR"
            case "for4":
                if(Lexim[i]=="z"):
                    i+=1
                    case="for5"
                else:
                    return "EROR"
            case "for5":
                if(i==len(Lexim)):
                    return "<ForToken>"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "def1":
                if(Lexim[i]=="s"):
                    i+=1
                    case="def2"
                else:
                    return "EROR"
            case "def2":
                if(Lexim[i]=="t"):
                    i+=1
                    case="def3"
                else:
                    return "EROR"
            case "def3":
                if(Lexim[i]=="o"):
                    i+=1
                    case="def4"
                else:
                    return "EROR"
            case "def4":
                if(Lexim[i]=="o"):
                    i+=1
                    case="def5"
                else:
                    return "EROR"
            case "def5":
                if(Lexim[i]=="r"):
                    i+=1
                    case="def6"
                else:
                    return "EROR"
            case "def6":
                if (i==len(Lexim)):
                    return "<CallToken>" 
                elif(Lexim[i]=="a"):
                    i+=1
                    case="def7"
                else:
                    return "EROR"
            case "def7":
                if(Lexim[i]=="t"):
                    i+=1
                    case="def8"
                else:
                    return "EROR"
            case "def8":
                if(Lexim[i]=="_"):
                    i+=1
                    case="def9"
                else:
                    return "EROR"
            case "def9":
                if(Lexim[i]=="e"):
                    i+=1
                    case="def10"
                else:
                    return "EROR"
            case "def10":
                if(Lexim[i]=="l"):
                    i+=1
                    case="def11"
                else:
                    return "EROR"
            case "def11":
                if(Lexim[i]=="a"):
                    i+=1
                    case="def12"
                else:
                    return "EROR"
            case "def12":
                if(Lexim[i]=="h"):
                    i+=1
                    case="def13"
                else:
                    return "EROR"
            case "def13":
                if(Lexim[i]=="i"):
                    i+=1
                    case="def14"
                else:
                    return "EROR"
            case "def14":
                if(i==len(Lexim)):
                    return"<DefToken>"
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "input1":
                if (Lexim[i]=="a"):
                    i+=1
                    case="input2"
                else:
                    return "EROR"
            case "input2":
                if (i==len(Lexim)):
                    return("<InputToken>")
                else:
                    return "EROR"
            
            # ----------------------------
            
            case "output1":
                if(Lexim[i]=="j"):
                    i+=1
                    case="output2"
                else:
                    return "EROR"
            case "output2":
                if(Lexim[i]=="a"):
                    i+=1
                    case="output3"
                else:
                    return "EROR"
            case "output3":
                if(Lexim[i]=="b"):
                    i+=1
                    case="output4"
                else:
                    return "EROR"
            case "output4":
                if(Lexim[i]=="a"):
                    i+=1
                    case="output5"
                else:
                    return "EROR"
            case "output5":
                if(Lexim[i]=="t"):
                    i+=1
                    case="output6"
                else:
                    return "EROR"
            case "output6":
                if(i==len(Lexim)):
                    return "<OutputToken>"
                else:
                    return "EROR"
            
            # ----------------------------
            
        
        
        
        
        
# ===============================================
# ==================== main: ====================


# -------- read file --------
r_input=open("input.txt","r")
List=r_input.read()
r_input.close()
List=List.split()

open('Token.txt', 'w').close() # clear Token.txt file

for i in range (len(List)):
    Token=GetToken(List[i])
    if Token=="EROR":
        print("Syntax Eror!")
        break
    w_output=open("Token.txt","a")
    w_output.write(Token)
    w_output.write("\n")
    w_output.close()
    
    
r_Token=open("Token.txt","r")
List1=r_Token.read()
List1=List1.split('\n')
for x in List1:
    print(x)
r_Token.close()
    