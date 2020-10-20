n = str(input())
def oddbefeven(x) :
    if x[0].isdigit() :
        if int(x)%2 == 0 :
            return True
        else :
            return False
    else :
        return True

arrange = ''.join(sorted(n, key = lambda x: (x[0].isdigit(), oddbefeven(x), x.swapcase())))
print(str(arrange))
