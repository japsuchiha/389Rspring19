# Writeup 7 - Binaries I

Name: *Japneet Singh Arora*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *Japneet Singh Arora*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
#include <stdio.h>

int main () {
    int x = 0x1ceb00da;
    int y = 0xfeedface;

    printf("x = %d\n", y);

    printf("y = %d\n", x);

    y = x^y;
    x = x^y;
    y = x^y;

    printf("x = %d\n", y);

    printf("y = %d\n", x);

    return(0);
}
```

### Part 2 (10 Pts)

The program above swaps the value contained in the two variables and prints the ans before and after the swap.
