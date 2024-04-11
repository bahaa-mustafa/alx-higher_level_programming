#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: a head of list
*
* Return: 1 if cycle found and 0 in other
*/
int check_cycle(listint_t *list)
{
    listint_t *current = list, *checker = list;

    if (list == NULL)
        return (0);
    while (current && checker && current->next)
    {
        checker = checker->next->next;
        current = current->next;
        if (current == checker)
            return (1);
    }
    return (0);
}