#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - zombie process
 * Return: 0 in some cases jajaja
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create zombie
 * Return: 0 in some cases jaja
 */
int main(void)
{
	int i = 0;
	pid_t zombie;

	while (i < 5)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %i\n", zombie);
		} else
			exit(0);
		i++;
	}
	infinite_while();
	return (0);
}
