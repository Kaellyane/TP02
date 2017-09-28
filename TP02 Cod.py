def integer_to_digit(x):
    if x in range(0,10):
        return chr(ord('0') + x)
    if x in range(10,16):
        return chr(ord('7') + x)

def integer_to_string(n, b):
    x=0
    i=0
    a=0
    liste_lettre=["A","B","C","D","E","F"]
    liste_expo=[]
    liste_base_b=[]
    print(a, "*")
    while a < n:
        liste_expo.append(a)
        a=b**i
        i=i+1
        print(a)
    del liste_expo[0]
    print(liste_expo)
    h=len(liste_expo) - 1
    print(h)
    while h >= 0:
        if n//liste_expo[h] < 10:
            liste_base_b.append(str(n//liste_expo[h])) 
        else :
            liste_base_b.append(str(liste_lettre[(n//liste_expo[h]) % 10]))
        n=n%liste_expo[h]
        h=h-1
    return "".join(liste_base_b)

def deux_puissance(n):
    if n == 0 :
        return 2 >> 1
    else :
        return 2 << n-1

def most_least_significant_bits_str(integer):
    
