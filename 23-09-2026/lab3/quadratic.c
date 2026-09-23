#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main(){
	float a,b,c;
	printf("Input values for quadratic ax^2 + bx + c: a b c\n");
	scanf("%f %f %f",&a,&b,&c);
	int deti = 0;
	float detsq = pow(b,2)-4*a*c;
	float root1,root2;

	if (detsq > 0){
		root1 = ((-b)+sqrt(detsq))/(2*a);
		root2 = ((-b)-sqrt(detsq))/(2*a);
		printf("%f,%f are your roots",root1,root2);}
	else if (detsq == 0){
		root1 = (-b)/(2*a);
		printf("You have repeated roots and it is: %f",root1);}
	else {
	printf("your 1st complex root is %f + i%f \n",(-b/2*a),(sqrt(abs(detsq))));
	printf("your 2nd complex root is %f - i%f",(-b/2*a),(sqrt(abs(detsq))));}

	return 0;
	}


		
