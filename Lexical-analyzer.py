def GetToken(Lexim):
    c=0
    i=0
    match c:
        case 0:
            if(Lexim[i]=="1"):
                i+=1
                case="var1"
            elif(Lexim[i]=="p"):
                pass
            elif(Lexim[i]=="b"):
                pass
            elif(Lexim[i]=="j"):
                pass
            elif(Lexim[i]=="n"):
                pass
            elif(Lexim[i]=="d"):
                pass
            elif(Lexim[i]=="e"):
                pass
            else:
                pass
            
        case "var1":
            pass
        case "var2":
            pass
        case "var3":
            pass
        
        # ----------------------------
        
        case "if1":
            pass
        case "if2":
            pass
        case "if3":
            pass
        case "if4":
            pass
        case "if5":
            pass
        case "if6":
            pass
        case "if7":
            pass
        case "if8":
            pass
        case "if9":
            pass
        
        # ----------------------------
            
        case "else_if1":
            pass
        case "else_if2":
            pass
        case "else_if3":
            pass
        case "else_if4":
            pass
        case "else_if5":
            pass
        case "else_if6":
            pass
        case "else_if7":
            pass
        
        # ----------------------------
        
        case "else1":
            pass
        case "else2":
            pass
        case "else3":
            pass
        case "else4":
            pass
        case "else5":
            pass
        case "else6":
            pass
        case "else7":
            pass
        
        # ----------------------------
        
        case "for1":
            pass
        case "for2":
            pass
        case "for3":
            pass
        case "for4":
            pass
        case "for5":
            pass
        
        # ----------------------------
        
        case "def1":
            pass
        case "def2":
            pass
        case "def3":
            pass
        case "def4":
            pass
        case "def5":
            pass
        case "def6":
            pass
        case "def7":
            pass
        case "def8":
            pass
        case "def9":
            pass
        case "def10":
            pass
        case "def11":
            pass
        case "def12":
            pass
        case "def13":
            pass
        case "def14":
            pass
        case "def15":
            pass
            
        # ----------------------------
        
        case "call1":
            pass
        case "call2":
            pass
        case "call3":
            pass
        case "call4":
            pass
        case "call5":
            pass
        case "call6":
            pass
        case "call7":
            pass
        
        # ----------------------------
        
        case "input1":
            pass
        case "input2":
            pass
        case "input3":
            pass
        
        # ----------------------------
        
        case "output1":
            pass
        case "output2":
            pass
        case "output3":
            pass
        case "output4":
            pass
        case "output5":
            pass
        case "output6":
            pass
        
        # ----------------------------
        
        
        
        
        
        
# ===============================================
# ==================== main: ====================


# -------- read file --------
r_input=open("input.txt","r")
List=r_input.read()
r_input.close()
List=List.split()

for i in range (len(List)):
    GetToken(List[i])
    
    