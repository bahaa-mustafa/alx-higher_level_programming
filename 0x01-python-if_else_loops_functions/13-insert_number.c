#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current;

    if (!new_node)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;
    current = *head;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }
    while (current->next)
    {
        if (current->next->n > new_node->n)
        {
            new_node->next = current->next;
            current->next = new_node;
            return (new_node);
        }
        current = current->next;
    }
    current->next = new_node;
    return (new_node);    
}