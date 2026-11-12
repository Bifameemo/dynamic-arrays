#ifndef DYNAMIC_ARRAYS_H
#define DYNAMIC_ARRAYS_H

typedef struct
{
    int *items;
    int count;
    int capacity;
} DynamicArray;

DynamicArray da_create(int *items, int count);
void da_append(DynamicArray *xs, int x);
void da_extend(DynamicArray *xs, DynamicArray ys);

#endif // DYNAMIC_ARRAYS_H