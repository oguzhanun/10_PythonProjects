def no_space(x):
    print("x----->",x)
    x=list(x)
    counter = 0
    
    for i in range(len(x)) :
        # print("counter",counter)
        # print("index:---->", i)
        # print("x dışarıda ----->", x)
        #if i < len(x):
        #print(i,x[i])
        if x[i] == " ":
            #print("içeride:",i)
            #x.remove(x[i]) # -----> x.remove(" ")
            #x.pop(i)
            counter += 1
            #print("x içeride ----->", x)
            #x.append(" ")
    for i in range(counter):
        x.remove(" ")
                
        #print("---------------------------------------------------------------------------------")
    return "".join(x)


print(no_space("8 j 8   mBliB8g  imjB8B8  jl  B"))