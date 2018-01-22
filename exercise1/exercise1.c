#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int x = 42;
char y[15] = "James Bond";
char a[6];
_Bool z = 1;



int main(void)
{

    if ( z == 1 )
{
    (strcpy(a, "True"));
}

    printf("%i, %s, %s\n", x, y, a);
    printf("%i\n", x);
    printf("%s\n", y);
    printf("%s\n", a);
}
