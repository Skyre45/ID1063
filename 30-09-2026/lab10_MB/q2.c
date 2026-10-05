#include <stdio.h>

int main() {
    int n, m;
    int grid[100][100];
    int result[100][100];

    scanf("%d %d", &n, &m);

    /* Read the board */
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%d", &grid[i][j]);
        }
    }
    /* For every cell:
       - store -1 if it contains a mine
       - otherwise count mines in its neighboring cells
    */
    int count=0;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            /*-1 case*/
            if(grid[i][j]==1){
                 result[i][j]=-1;
                continue;
            }
            /*edge cases*/
            for(int x=-1;x<2;x++){
                for(int y=-1;y<2;y++){
                    if(x == 0 && y ==0) continue;
                    
                    int n1=i+x;
                    int n2=j+y;
                    
                    if(!(n1<0 || n2<0 || n1>=n || n2>=m)){
                        if (grid[n1][n2]==1) count++;
                    }
                }
            
            }
            result[i][j]=count;
            count = 0;
        }
    }
    /* Print the result matrix */
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            printf("%d", result[i][j]);
            if(!(j==m-1)){
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}

