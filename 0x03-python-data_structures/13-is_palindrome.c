#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to list
 *
 * Return: 1 if it was palindrome and 0 if not
*/
int is_palindrome(listint_t **head)
{
    listint_t *current;
    int arr[2000] = {0};
    int flag = 0, i, j;


    if (!*head)
        return (1);

    current = *head;
    while (current)
    {
        arr[flag] = current->n;
        flag++;
        current = current->next;
    }
    
    for (i = 0, j = flag - 1; i < flag && j > i; i++)
    {
        if (arr[i] != arr[j--])
        {
            return (0);
        }
    }
    return (1);
}
