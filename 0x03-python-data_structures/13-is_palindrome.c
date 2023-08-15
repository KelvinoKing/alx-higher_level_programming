#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - Checks a singly linked is a palindrome
 * @head: pointer to pointer of head node
 *
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *array, i;
	unsigned int num_nodes = 0;

	current = *head;
	while (current != NULL)
	{
		num_nodes++;
		current = current->next;
	}

	array = malloc(num_nodes * sizeof(int));
	if (array == NULL)
		return (0);

	current = *head;
	for (i = 0; current != NULL; i++)
	{
		array[i] = current->n;
		current = current->next;
	}
	current = *head;
	for (i = num_nodes - 1; current != NULL; i--)
	{
		if (current->n != array[i])
		{
			free(array);
			return (0);
		}
		current = current->next;
	}
	free(array);
	return (1);
}
