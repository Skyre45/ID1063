#include<stdio.h>
#include<math.h>

float f(float x){
	float y = exp(x)-2;
	return y;
}

float g(float x){
	float z = x - f(x)/(f(x)+2);
	return z;
}

int main(){
	float x0=1;
	float x = g(x0);

	while(x0-x>0.001){
		x0 = x;
		x = g(x);
	}
	
	printf("%f %f",x,f(x));

	return 0;
}

