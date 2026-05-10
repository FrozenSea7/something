run=True
fp=open("note.txt","w")#open the file,w=write
print("axxxxxxxxxxx00000weiusdisjsdanjx",file=fp)
fp.close()#close the file
fp=open("noge.txt","w")
for i in range(0,1600):
    print(i,file=fp)
fp.close()
