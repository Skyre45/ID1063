#include <stdio.h>

int main(void) {
    printf("a b c | X\n");
    for (int i = 0; i < 8; i++) {
        int a = (i >> 2) & 1;
        int b = (i >> 1) & 1;
        int c = i & 1;
        int X = (a & b) | (b & c) | (c & a);
        printf("%d %d %d | %d\n", a, b, c, X);
    }
    return 0;
}
