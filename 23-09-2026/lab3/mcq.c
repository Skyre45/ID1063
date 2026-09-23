#include<stdio.h>

 int main(){
	 int ans;
	 printf("The question is how many sides does square have:\n"
		"1.3 sides\n"
		"2.4sides \n"
		"3.5 sides\n"
		"4.6 sides\n");
	 scanf("%d",&ans);

	 if (ans == 2){
		 printf("You ARE correct.");}
	 else{
		 printf("You are wrong, answer is 4 sides");
	 }

	 return 0;
 }

