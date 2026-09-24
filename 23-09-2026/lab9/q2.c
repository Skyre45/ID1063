#include<stdio.h>

int daysElapsed(int day,int month){
	int months[12]={31,28,31,30,31,30,31,31,30,31,30,31};
	int dE = 0;
	if(day<=months[month-1]){if(month>1){
	for(int i=0;i<month-1;i++){
		dE += months[i];
	}}
	
	dE += day;}
	return dE;
}

int main(){
	int day, month;
	scanf("%d %d", &day,&month);
	printf("%d",daysElapsed(day, month));
	return 0;
}

