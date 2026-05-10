run=True
def Auto () :
    infomation=input("Please detail infomation,when you see a [X.txt],and you can  detail [QUIT] to quit")
    
    if not infomation == "QUIT" :
           fp=open("File.txt","w")
           print(infomation,file=fp)
           fp.close()
    else :
           quit

while run == True :
      Auto()
