#include <stdio.h>
#include <string.h>

void vulnerable_function() {
    char buffer[10]; // Small buffer

    printf("Enter input: ");
    gets(buffer); // Unsafe function (no boundary check)

    printf("You entered: %s\n", buffer);
}

int main() {
    vulnerable_function();
    return 0;
}
