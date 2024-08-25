st= input("Enter Your Message :- ")
chars=st.split(" ")
code=input("Type 'E' for encrypting and 'D' for decoding")
code=True if (code=="E") else False

if(code):
    r1=input("Enter any 4 random character to encrypt your msg.:- ") 
    r2=input("Enter any secondary 4 random character to encrypt your msg.:- ")
    newchar=[]
    for char in chars:
        # newchar=[]
        if len(st)>=3:
            # r1="nsbb"
            # r2="kjhb"
            stnew= r1+char[1:]+char[0]+r2
            newchar.append(stnew)
            # print(" ".join(newchar))
        else:
            newchar.append(char[::-1])
    print(" ".join(newchar))

else:
    newchar=[]
    for char in chars:
        if len(st)>=3:
            stnew=char[4:-4]
            stnew=stnew[-1]+stnew[:-1]
            newchar.append(stnew)
        else:
            newchar.append(char[::-1])
    print(" ".join(newchar))

