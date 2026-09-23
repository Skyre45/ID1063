#include<stdio.h>
#include<math.h>

int main(){
float f;
int n;

scanf("%f",&f);
scanf("%d",&n);

for (int i =1;i <= n;i++){
	printf("%f ",pow(f,i));
}

return 0;
}
