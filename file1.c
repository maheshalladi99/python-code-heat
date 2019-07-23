#include<stdio>
#include<conio.h>
int main (void)
{
  FILE * fileName;
  char ch;
  fileName = fopen("anything.txt","wt");
  for (ch = 'D' ; ch <= 'S' ; ch++) {
    putc (ch , fileName);
    }
  fclose (fileName);
  return 0;
}
