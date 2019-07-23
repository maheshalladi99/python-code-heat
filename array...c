
#include <stdio.h>
 
int main()
{
 
        int arr[50], size, i, largest;
 
        printf("\n Enter the size of the array: ");
	scanf("%d", &size);
 
        printf("\n Enter %d elements of  the array: ", size);
 
        for (i = 0; i < size; i++)
		scanf("%d", &arr[i]);
 
        largest = arr[0];
 
        for (i = 1; i < size; i++) 
        {
		if (largest < arr[i])
			largest = arr[i];
	}
 
        printf("\n largest element present in the given array is : %d", largest);
 
        return 0;
 
}
