#include<stdio.h>
int main()
{
	int a[5][5],i=0,j=0,m,n,c1=0,c2=0;
	printf("enter m,n values");
	scanf("%d %d",&m,&n);
	printf("enter matrix elements");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if((i==j)&&(a[i][j]!=0)){
			c1++;}
			else if((i!=j)&&(a[i][j]==0))
			c2++;
		}
	}
	if((c1==m)&&(c2==(n*(n-1))))
	printf("\nit is a diagonal matrix");
	else
		printf("\nit is not a daigonal matrix");
	}
