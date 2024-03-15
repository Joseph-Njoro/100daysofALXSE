#include <stdio.h>
void foo();
int main()
{
	// foo() function called
	foo();
	getchar();
	return 0;
}

// definition of foo() function
void foo() {
printf("foo called\n");
}