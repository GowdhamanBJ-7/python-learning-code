def add(a,b):
    return a+b

def division(a, b):
    if b ==0 :
        raise ValueError('Zero is not acceptable')
    if type(a) != int or type(b) != int:
        raise TypeError("Input must be an integer")
    return a/b

string = "abracadabra"
l = list(string)
print(l)
l[0] ='y'
string = ''.join(l)
print(string)

