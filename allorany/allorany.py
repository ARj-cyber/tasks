lst = []
lst = [int(x) for x in input().split()]

# Function
def CheckPositive(list) :
    return(all(x > 0 for x in list))

def CheckPalindrome(list) :
    return(any(str(x) == str(x)[::-1] for x in list))

# Drive code
if(CheckPositive(lst) and CheckPalindrome(lst)) :
    print("True")
else :
    print("False")
