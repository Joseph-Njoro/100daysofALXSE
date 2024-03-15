// C program to demonstrate the error occured
// when function prototype is not specified

// Prototype of foo() function is not specified

int main()
{
	// foo() function called
	foo();
	getchar();
	return 0;
}

// definition of foo() function
void foo() {
printf("foo called");
}