for i in range(2,10):
    print("#    %d단    # "%i,end="")
print("")

for i in range(1,10):
    for r in range(2,10):
        print("%2d X %2d = %2d  " %(r,i,r*i),end="") 
        
    print("")
