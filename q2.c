#include<stdio.h>

int main(){

int n;
scanf("%d",&n);

printf("ENTER VALUES OF 1ST VECTOR: ");
float vec1[n],vec2[n];

for (int i=0;i<n;i++){
	scanf("%f",&vec1[i]);}

 printf("ENTER VALUES OF 2ND VECTOR: ");
for (int i=0;i<n;i++){
        scanf("%f",&vec2[i]);}

float dp = 0;

for (int i=0;i<n;i++){
	dp += (vec1[i])*(vec2[i]);}
printf("%f is the dot product of the two vectors.",dp);

return 0;
}
