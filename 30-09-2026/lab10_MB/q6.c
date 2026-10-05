#include <stdio.h>

int main() {
    int a, b;
    int *p;

    scanf("%d %d", &a, &b);

    /* Make p point to the smaller variable.
       If a and b are equal, make p point to b. */
    if(a>b || a == b){
        p = &b;
    }
    else{
        p = &a;
    }

    /* Add 10 to the variable pointed to by p. */
    *p += 10;


    printf("%d %d\n", a, b);

    return 0;
}

