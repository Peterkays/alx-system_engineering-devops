#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Inifinite loop.
 * Return: Always 0.
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
 * main - Build zombie process.
 * Return: Always 0.
 */
int main(void)
{
	pid_t child;
	int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", child);
	}
	infinite_while();
	return (0);
}
