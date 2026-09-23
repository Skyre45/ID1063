#include<stdio.h>

int main(){

int n;
scanf("%d",&n);

float max = 0;

for(int i = 1;i<=n;i++){
	float a;
	scanf("%f",&a);
	if(max<a){
		max = a;
	}
}
printf("max number is %f",max);








return 0;
}
