#include <stdio.h>

#define MAX 20

int productEntry(int A[][MAX], int B[][MAX],
                 int row, int col, int common);

int main(void)
{
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];
    int r1, c1, r2, c2;
    int i, j;

    scanf("%d %d", &r1, &c1);

    for (i = 0; i < r1; i++) {
        for (j = 0; j < c1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &r2, &c2);

    for (i = 0; i < r2; i++) {
        for (j = 0; j < c2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    /* Compute the product matrix by calling productEntry
       once for each entry of C. */
    for(int i=0;i<r1;i++){
        for(int j=0;j<c2;j++){
            C[i][j] = productEntry(A, B, i, j, c1);
        }
    }

    /* Print the product matrix. */
    for(int i=0;i<r1;i++){
        for(int j=0;j<c2;j++){
            printf("%d",C[i][j]);
        
        if(j<c2-1){
            printf(" ");
        }}
        printf("\n");
        
    }

    return 0;
}

int productEntry(int A[][MAX], int B[][MAX],
                 int row, int col, int common)
{
    /* Write your code here. */
    int pE = 0;
    for(int i=0;i<common;i++){
                    pE += A[row][i]*B[i][col];
        
    }
    return pE;
}

