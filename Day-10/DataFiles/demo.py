def reversenumber(d):
    r = 0
    while d!=0:
        r = r*10+d%10
        d//=10
    return r

def printeven(ty):
    while ty!=0:
        if (ty%10)%2==0:
            print(ty%10,end=" ")
        ty//=10
    return
