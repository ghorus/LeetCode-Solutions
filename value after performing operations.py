x=0
        for i in operations:
            if i[0:2]=="++" or i[1:]=="++":
                x+=1
            else:
                x-=1
            print(i[0:2])
        return x