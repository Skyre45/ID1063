#include<stdio.h>

int main(){

/*Write a program that accepts a positive integer n, followed by n
floating-point values, and stores the values in an array.
Compute the average of the values and then print the number of values
that are strictly greater than the average.
For example:
Enter the value of n: 6
Enter the values: 4.5 2.0 7.5 5.0 3.0 8.0
Average: 5.0
Number of values above the average: 2*/

int n;
scanf("%d",&n);

float arr[n];

for(int i=0;i<n;i++){
	scanf("%f",&arr[i]);}

float avg=0.0;

for(int i=0;i<n;i++){
	avg += arr[i];}

avg = (avg/n);

int count=0;

for(int i=0;i<n;i++){
	if(arr[i]>avg){
		count++;
	}}
printf("The count is %d,and the average is %f.",count,avg);













return 0;
}
