#include "lists.h"
/**
 * check_cycle - Checks if the linked lists have loop
 * @list: linked list
 * Return: 0 if no cycle, 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slowp, *fastp;

	slowp = list;
	fastp = list;

	while (slowp && fastp && fastp->next)
	{
		slowp = slowp->next;
		fastp = fastp->next->next;
		if (slowp == fastp)
			return (1);
	}
return (0);
}
