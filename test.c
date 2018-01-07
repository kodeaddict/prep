#include <stdio.h>
int check_duplicate_numbers(int *num, int len);
void main()
{
    int arr[] = { 1,3,4,5,6,6,7};
    int ret;
    ret = check_duplicate_numbers(arr, sizeof(arr)/ sizeof(arr[0]));

    printf("ret = %d\n", ret);
}

