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
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if ((*head)->n > number || *head == NULL || head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
