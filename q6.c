#include<stdio.h>

int main(){

int n;
scanf("%d",&n);

int a;
int found=0;
int arr[n],arr2[n];


for (int i=0;i<n;i++){
	scanf("%d",&arr[i]);
	}

for (int i = 0; i < n; i++) {
    arr2[i] = arr[i];
}

for (int i =0;i<n;i++){
 for(int j = i+1;j<n;j++){
	 if (arr[i]>arr[j]){
		 a = arr[i];
		 arr[i]=arr[j];
		 arr[j] = a;}}}

for (int i = 0;i<n-1;i++){
	int b;
	if (arr[i]==arr[i+1]){
		found = 1;
		printf("This number is repeating: %d. Repeated at position: " ,arr[i]);
			for (int j=0;j<n;j++){
				if (arr[i]==arr2[j]){
					printf("%d ",j);}}
		while(i<n-2 && arr[i+1]==arr[i+2]){
			i++;}}}
		printf("\n");
if (found==0){
	printf("No repeating numbers");}
return 0;
}
							
