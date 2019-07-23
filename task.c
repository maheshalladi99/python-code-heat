#include <stdio.h>
#include <string.h>
 
int main()
{
   char string[100];
   int c = 0, count[100] = {0}, x,d=0,co=0,counter=0,j,i,b=0,count1[100],a,f=0;
 
   printf("Enter a string\n");
  
   scanf("%s",string);
   while (string[c] != '\0') 
   {
         if (string[c] >= 'a' && string[c] <= 'z')
        {
         x = string[c] - 'a';
         
         count[x]++;
        }
 
      c++;
   }
 
   for (c = 0; count[c]!='\0'; c++)
   {
       printf("%d ",count[c]);
      d++;
    
   }
   printf("\n");
   
 printf("%d \n",d);
 {
     for(i=1;i<=d;i++)
     {
         if(d%i == 0)
         {
             counter++;
         }
     }
     if(counter == 2)
     {
         printf("%d is a prime \n",d);
         for(j=1;count[i]!= '\0';j++)
         {
             for(i=1;i<=count[i];i++)
             {      f++;
                 if(count[i]%j==0)
                 a=b++;
                 count1[f]=a;
                 //f++;
             }
         }
     }
     
 } for (c = 0; count1[c]!='\0'; c++)
   {
       printf("%d ",count1[c]);
   }
 
   return 0;
}




























