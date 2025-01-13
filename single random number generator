#include <stdio.h>
static unsigned long x0 = 1;  // Initial seed

unsigned long my_random() {
    // Constants for the Linear Congruential Generator
    const unsigned long a = 1664;   // Multiplier 
    const unsigned long c = 13904;  // Increment 
    const unsigned long m = 4276;  // Modulus 
    x0 = (a * x0 + c) % m;  // LCG formula: (a * seed + c) % m
    return x0; }

int main() {
    printf("Random number: %lu\n", my_random());
    return 0;
}
