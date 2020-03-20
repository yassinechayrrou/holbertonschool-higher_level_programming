#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
  *insert_node - inserts new node into sorted LL at proper order
  *@head: pointer to head node of linked list
  *@number: data to insert
  *Return: NULL or pointer to inserted node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *temp;

	if (*head == NULL)
		return (NULL);
	temp = *head;
	newNode = malloc(sizeof(listint_t));
	newNode->n = number;
	while (temp)
	{
		if (temp->next == NULL)
		{
			if (temp->n >= number)
			{
				newNode->next = temp;
				return (newNode);
			}
			if (temp->n < number)
			{
				temp->next = newNode;
				newNode->next = NULL;
				return (newNode);
			}
		}
		if (temp->next)
		{
			if (temp->n <= number && temp->next->n >= number)
			{
				newNode->next = temp->next;
				temp->next = newNode;
				return (newNode);
			}
		}
		temp = temp->next;
	}
	return (NULL);
}
