#include <stdio.h>

int main(){
	float a,b,c;
	printf("Enter your three numbers: a b c\n");
	scanf("%f %f %f",&a,&b,&c);
	if ((a<=b) && (a<=c))
	{printf("%f is the smallest number", a);}
	else if ((b<=a) && (b<=c)){
		printf("%f is the smallest number.",b);}
	else{
		printf("%f is the smallest number.",c);}
	return 0;
}
