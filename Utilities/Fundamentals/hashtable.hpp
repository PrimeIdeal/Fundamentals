#ifndef HASHTABLE_H
#define HASHTABLE_H

#include <cstring>

class HashSet
{
    private:
        int storage[100][100];

    public:
        HashSet()
        {
            std::memset(storage, -1, sizeof(storage[0][0])*100*100);
        }
        void add(int key)
        {
            int ident {key%100};
            for (int *i {storage[ident]}; i < storage[ident] + 100; ++i)
            {
                if (*i == -1)
                {
                    *i = key;
                    return;
                }
                if (*i == key)
                    return;
            }
        }
        void remove(int key)
        {
            int ident {key%100};
            int *k {storage[ident]};
            while (k < storage[ident] + 100)
            {
                for (int *i {storage[ident]}; i < storage[ident] + 100; ++i)
                {
                    if (*i != key)
                        *k++ = *i;
                }
                if (k < storage[ident] + 100)
                    *k++ = -1;
            }
        }
        bool contains(int key)
        {
            int ident {key%100};
            for (int *i {storage[ident]}; i < storage[ident] + 100; ++i)
            {
                if (*i == -1)
                    break;
                if (*i == key)
                    return true;
            }
            return false;
        }
};

class HashMap_Basic
{
    private:
        int storage[1000001];

    public:
        HashMap_Basic()
        {
            std::memset(storage, -1, sizeof(storage[0])*1000001);
        }
        void put(int key, int value)
        {
            storage[key] = value;
        }
        int get(int key)
        {
            return storage[key];
        }
        void remove(int key)
        {
            storage[key] = -1;
        }
};

#endif