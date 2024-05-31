// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 52;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int x = toupper(word[0]) - 'A';
    int y = toupper(word[1]) - 'A';
    int z = x + y % 52;
    return z;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    char word[LENGTH + 1];
    FILE *file = fopen(dictionary,"r");
    node *n = malloc(sizeof(node));

    if (file == NULL || n == NULL)
    {
        return false;
    }
    while (fscanf(file, "%s", word) != EOF)
    {
        n->next = NULL;
        strcpy(n->word, word);
        n->next = table[hash(word)];
        table[hash(word)] = n;
    }

    free(n);
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    FILE * file = fopen("dictionaries/large","r");
    char word[LENGTH + 1];
    int n = 0;

    if (file == NULL)
    {
        return 0;
    }

    while (fread(word, sizeof(char *), 1, file))
    {
        n++;
    }

    fclose(file);
    return n;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
