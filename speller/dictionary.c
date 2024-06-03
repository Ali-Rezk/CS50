// Implements a dictionary's functionality
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
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
node *n;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int x = hash(word);
    node *p = malloc(sizeof(node));

    if (p == NULL)
    {
        return false;
    }

    p->next = NULL;
    p = table[x];

    while (strcasecmp(p->word,word) != 0 && p != NULL)
    {
        p = p->next;
    }

    if(p == NULL)
    {
        free(p);
        return false;
    }
    else
    {
        free(p);
        return true;
    }


}


// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    int x = toupper(word[0]) - 'A';

    return x;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO create hash table
    char word[LENGTH + 1];
    FILE *file = fopen(dictionary,"r");

    int z = 0;

    if (file == NULL)
    {
        return false;
    }
    while (fscanf(file, "%s", word) != EOF)
    {
        n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        z = hash(word);
        strcpy(n->word, word);
        n->next = NULL;
        n->next = table[z];
        table[z] = n;
        if (n != NULL)
        {
            free(n);
        }

    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    FILE * file = fopen("dictionaries/large","r");
    char word[LENGTH + 1];
    int x = 0;

    if (file == NULL)
    {
        return 0;
    }

    while (fread(word, sizeof(char *), 1, file))
    {
        x++;
    }

    fclose(file);
    return x;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return true;

    if (n == NULL)
    {
        return false;
    }

    n->next = NULL;

    for (int i = 0; i < N; i++)
    {
        n = table[i];

        while (n != NULL)
        {
            table[i] = n->next;
            free(n);
            n = table[i];
        }
    }
    return true;
}
