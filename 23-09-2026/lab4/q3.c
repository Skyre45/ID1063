#include<stdio.h>

int main(){
float r,v;
scanf("%f",&r);
int n = 0;
v = 1.0;
while(v<=2.0){
	v = v*((100+r)/100);
	n++;
}
printf("years = %d",n);

return 0;
}
