#include<stdio.h>
#include<math.h>

int main(){
int a,n;
scanf("%d",&n);

a = pow(n,0.5);

for (int i=1;i<=a;i++){
	printf("%d ",(int)pow(i,2));
}
}

