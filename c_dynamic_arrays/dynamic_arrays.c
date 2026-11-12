#include <stdlib.h>
#include "dynamic_arrays.h"

DynamicArray da_create(int *items, int count)
{
    DynamicArray da;
    // assume malloc never fails
    da.items = malloc(sizeof(int));
    da.count = 0;
    da.capacity = 1;
    for (int i = 0; i < count; ++i)
    {
        da_append(&da, items[i]);
    }
    return da;
}

void da_append(DynamicArray *xs, int x)
{
    if (xs->count == xs->capacity)
    {
        // reallocate 2 times the memory
        xs->capacity *= 2;
        // assume realloc never fails
        xs->items = realloc(xs->items, sizeof(int) * xs->capacity);
    }
    xs->items[xs->count++] = x;
    return;
}

void da_extend(DynamicArray *xs, DynamicArray ys)
{
    // loops infinitely if xs and ys point to the same items array
    for (int i = 0; i < ys.count; ++i)
    {
        da_append(xs, ys.items[i]);
    }
}
