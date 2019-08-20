def main():
    f = open("test.txt","r") 
    outfile = open("out.txt","w")
    i = 0
    while 1:
        c = f.read(1)
        i = i + 1
        if not c:
            break

        if i%32 == 0:
            outfile.write("\n")
        else:
                c = '7'
                outfile.write(hex(ord(c)) + " ")

    outfile.close()
    f.close()
         
if __name__=="__main__":
    main()
