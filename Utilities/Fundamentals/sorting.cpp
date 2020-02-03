#include <iostream>
#include <vector>

std::vector<int> insertion_sort(std::vector<int> &array)
{
    if (array.size() < 2)
        return array;
    
    for (int i {1}; i <  array.size(); i++)
    {
        int key = array[i];
        int j = i-1;

        while (j >= 0 && array[j] > key)
        {
            array[j+1] = array[j];
            j--;
        }

        array[j+1] = key;
    }

    return array;
}

int main()
{
    return 0;
}