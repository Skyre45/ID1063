#include<stdio.h>

int main(){
int i = 8;
int yeah = 0;
while (yeah==0){
	int z;
	scanf("%d",&z);
	if (z!=8){
		printf("try again");
	}
	else{
		printf("correct");
		yeah = 1;
	}
}
return 0;
}
