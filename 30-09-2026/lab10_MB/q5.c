#include <stdio.h>
#include <stdbool.h>

int main() {
    int n;
    int a[100];
    int i;
    bool safe = true;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    /* Check whether all readings are safe.
       Use the Boolean variable safe. */
    for (int i=0;i<n;i++){
        if (a[i]<20 || a[i]>80){
            safe = false;
        }
    }

    if (safe) {
        printf("Safe\n");
    }
    else {
        printf("Unsafe\n");
    }

    return 0;
}

