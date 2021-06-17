fd=open("file.txt","r")
new_fd=open("NewFile.txt","w")

fd1=fd.readlines();
#print (fd1)

for i in fd1:
    if "Sitaram" not in i:
        new_fd.write(i)
print(new_fd)

