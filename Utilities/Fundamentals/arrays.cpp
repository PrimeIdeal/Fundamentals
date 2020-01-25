#include <iostream>

void remove_val(int *array, int array_size, int val)
{
    int *i {array};
    int *k {array};
    while (i < array + array_size)
    {
        if (*i != val)
        {    
            *k = *i;
            ++k;
        }
        ++i;
    }
}

void reverse_pointers(int *array, int array_size)
{
    int *i {array};
    int *k {array + array_size - 1};
    int swap;
    while (i < k)
    {
        swap = *i;
        *i = *k;
        *k = swap;
        ++i;
        --k;
    }
}

void reverse_indices(int *array, int array_size)
{
    int swap;
    for (int i {0}; i < array_size/2; ++i)
    {
        swap = array[i];
        array[i] = array[array_size-i-1];
        array[array_size-i-1] = swap;
    }
}