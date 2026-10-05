#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generateVector(int v[], int n, int m) {
    for (int i = 0; i < n; i++)
        v[i] = rand() % (m + 1);   // integers 0..m inclusive
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);

    int v[n];
    srand(time(NULL));             // once, in main, not inside the function
    generateVector(v, n, m);

    for (int i = 0; i < n; i++)
        printf("%d ", v[i]);
    printf("\n");
    return 0;
}
