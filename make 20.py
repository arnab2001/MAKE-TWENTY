def makes_twenty (n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20
n1, n2 = map(int,input("Enter two values:").split())
print (makes_twenty(n1, n2))
