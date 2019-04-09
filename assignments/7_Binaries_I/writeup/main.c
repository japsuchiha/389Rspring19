/*
 * Name: *Japneet Singh Arora*
 * Section: *0101*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Japneet Singh Arora*
 */

/* your code goes here */

#include <stdio.h>

int main () {
    int x = 0x1ceb00da;
    int y = 0xfeedface;

    y = x^y;
    x = x^y;
    y = x^y;

    printf("x = %d\n", y);

    printf("y = %d\n", x);

    return(0);
}