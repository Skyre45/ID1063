#include<stdio.h>
#include<math.h>

/*
 A vibration sensor records the velocity of a machine component at regular intervals.
The readings may be positive or negative depending on the direction of motion.
Engineers use the root mean square (RMS) value to measure the overall strength of the vibration.

For n readings a[0], a[1], ..., a[n-1], the RMS value is

RMS = sqrt((a[0]^2 + a[1]^2 + ... + a[n-1]^2) / n)

Write a function

double rms(double a[], int n);

that accepts an array of vibration readings and its length and returns the RMS value.

The array is indexed starting from 0.

Input
The first line contains an integer n, the number of readings.
The second line contains n real numbers representing the vibration readings.

Output
Print the RMS value rounded to two decimal places.*/

double rms(double a[], int n){
	double result;
	for(int i =0;i<n;i++){
		result+=pow(a[i],2);
	}
	result = sqrt(result/n);
	return result;
}

int main(){
	int n;
	scanf("%d",&n);
	double a[n];
	for(int i=0;i<n;i++){
		scanf("%lf",&a[i]);
	}
	printf("%.2lf",rms(a, n));
	return 0;
	}


	

