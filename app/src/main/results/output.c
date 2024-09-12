#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){

    int True = 1;
    int False = 1;

    float n;
    float r;
    float x;
    float y;
    float z;
    char s1[1000];
    char s2[1000];
    int b1;
    int b2;
    b1 = True;
    strcpy(s1, "\nx maior ou igual que y");
    strcpy(s2, "\nx menor que y");
    printf("\nInsira um numero X (diferente de zero):");
    scanf("%f", &x);
    while(x==0){
       printf("\nNumero invalido!!!\n");
       printf("\nInsira um numero X (diferente de zero):");
       scanf("%f", &x);
    }
    printf("\nInsira um numero Y");
    scanf("%f", &y);
    printf("\nInsira um numero Z");
    scanf("%f", &z);
    z = z/11;
    printf("\nZ dividido por 11:");
    printf("%f", z);
    if(x>=y){
        printf(s1);
        b1 = True;
    }else{
        printf(s2);
        b1 = False;
    }
    if(b1==True){
        r = (int)x%(int)y;
        printf("\nResto da divisao de x por y:");
        printf("%f", r);
        printf("\n\nEzComp v0.2.7 2024");
    }else{
        printf("\nInsira um numero N, que sera expoente de X");
        scanf("%f", &n);
        x = pow(x, n);
        printf("\nX elevado a N:");
        printf("%f", x);
        printf("\n\nEzComp v0.2.7 2024");
    }


    return 0;

}
