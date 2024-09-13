def main():

    #double n;
    #double r;
    #double x;
    #double y;
    #double z;
    #string s1;
    #string s2;
    #boolean b1;
    #boolean b2;
    b1 = True
    s1 = "\nx maior ou igual que y"
    s2 = "\nx menor que y"
    print("\nInsira um numero X (diferente de zero):")
    x = float(input())
    while(x==0):
       print("\nNumero invalido!!!\n")
       print("\nInsira um numero X (diferente de zero):")
       x = float(input())
    print("\nInsira um numero Y")
    y = float(input())
    print("\nInsira um numero Z")
    z = float(input())
    z = z/11
    print("\nZ dividido por 11:")
    print(z)
    if(x>=y):
        print(s1)
        b1 = True
    else:
        print(s2)
        b1 = False
    if(b1==True):
        r = x%y
        print("\nResto da divisao de x por y:")
        print(r)
        print("\n\nEzComp v0.2.7 2024")
    else:
        print("\nInsira um numero N, que sera expoente de X:")
        n = float(input())
        x = x**n
        print("\nX elevado a N:")
        print(x)
        print("\n\nEzComp v0.2.7 2024")

if __name__ == "__main__":
    main()

