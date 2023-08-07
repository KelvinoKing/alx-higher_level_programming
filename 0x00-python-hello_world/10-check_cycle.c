#include "lists.h"
/**
 * check_cycle - Checks if a singly list has a cycle
 * @list: pointer to head node
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *head1, *head2;

	head1 = list;
	head2 = list;

	while (head1 && head2)
	{
		if (head2->next == NULL)
			return (0);
		head1 = head1->next;
		head2 = head2->next->next;
		if (head1 == head2)
			return (1);
	}
	return (0);
}
