#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int coins[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &coins[i]);
    }

    int *pmin = &coins[0];

    /* Scan the array.
       Make pmin point to the chest with the fewest coins. */
    for(int i=0; i<n; i++){
        if(*pmin > coins[i]){
            pmin = &coins[i];
        }
    }

    /* Remove all coins from the cursed chest. */
    *pmin = 0;

    for (int i = 0; i < n; i++) {
        printf("%d", coins[i]);
        if (i < n - 1) {
            printf(" ");
        }
    }
    printf("\n");

    return 0;
}

