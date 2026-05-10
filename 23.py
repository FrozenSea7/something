Quit=False
Project=str(23)
print(Project ,"R\n", "Python File")
print(Project ,"\n", "Python File")
import math
def Version() :
    V=str(input("Version \t Please"))
    print("Now Version \t",V)
    if V == "V10" :
        print('It.s your turn,but you have lost')
        pass
    else :
        fp=open("File.txt","w")
        print('Version is ',V,file=fp)
        fp.close#close
        fp=open("1 to 200","w")
        for num in range (1,201):
            print(num,file=fp)
        fp.close()
        print("READY")
        

Version()
Quit=True
    
