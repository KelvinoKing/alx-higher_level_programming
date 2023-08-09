#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to pointer of head node
 * @number: integer to be inserted
 *
 * Return: pointer to new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	current = *head;

	while (current != NULL)
	{
		if (current->next->n > number)
		{
			temp = current->next;
			new->next = temp;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	if (current == NULL)
	{
		add_nodeint_end(head, number);
	}
	free(new);
	return (NULL);
}
