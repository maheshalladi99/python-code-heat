
#include<stdio.h>
int main()
{
	int a[5][5],i=0,j=0,m,n;
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
		if(i%2==0)
	for(j=0;j<n;j++)
	{
	printf("%d ",a[i][j]);
}
else 
		for(j=n-1;j>=0;j--)
{
	printf("%d ",a[i][j]);
}
}
}

