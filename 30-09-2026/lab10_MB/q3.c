#include <stdio.h>

int main() {
    long int a, b;
    long int product;

    /* Read the input here. The format specifier for long is %ld */
    scanf("%ld %ld", &a, &b);
    

    /* Compute product and print */
    product = a*b;
    printf("%ld", product);
    return 0;
}
