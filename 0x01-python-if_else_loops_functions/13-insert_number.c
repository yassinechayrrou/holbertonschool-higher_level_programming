#include "lists.h"
/**
  *insert_node - inserts new node into sorted LL at proper order
  *@head: pointer to head node of linked list
  *@number: data to insert
  *Return: NULL or pointer to inserted node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *temp;

	temp = *head;
	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	if (*head == NULL)
	{
		newNode->next = NULL;
		*head = newNode;
		return (*head);
	}
	while (temp = temp->next)
	{
		if (temp->next == NULL && temp->n >= number)
		{
			newNode->next = *head;
			*head = newNode;
			return (*head);
		}
		if (temp->next == NULL && temp->n < number)
		{
			temp->next = newNode;
			newNode->next = NULL;
			return (newNode);
		}
		if (temp->next && temp->n >= number)
		{
			newNode->next = *head;
			*head = newNode;
			return (*head);
		}
		if (temp->next && temp->n < number && temp->next->n >= number)
		{
			newNode->next = temp->next;
			temp->next = newNode;
			return (newNode);
		}
	}
	return (NULL);
}
