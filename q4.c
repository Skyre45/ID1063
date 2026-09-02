#include<stdio.h>

int main(){

int m,n;
printf("Enter value of m: ");
scanf("%d",&m);
printf("\n");
printf("Enter value of n: ");
scanf("%d",&n);
printf("\n");

for (int i=0;i<n;i++){
	printf(" * ");}
printf("\n");

for(int i=0;i<m-2;i++){
	printf(" * ");
	for(int j=0;j<n-2;j++){
		printf("   ");
	}
	printf(" * \n");}

for (int i=0;i<n;i++){
       printf(" * ");}










return 0;
}
