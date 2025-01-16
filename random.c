//Prints 10 random numbers
#include <stdio.h>
static unsigned long x0 = 1;  // Initial seed

unsigned long my_random() {
  // Constants for the Linear Congruential Generator
  const unsigned long a = 16094;   // Multiplier 
  const unsigned long c = 13048;  // Increment 
  const unsigned long m = 427689;  // Modulus 
  x0 = (a * x0 + c) % m;  // LCG formula: (a * seed + c) % m
  return x0; }

unsigned long my_random_range(unsigned long min, unsigned long max) {
  return min + (my_random() % (max - min + 1)); }

int main() {
  // Testing the custom random number generator
  for (int i = 0; i < 10; i++) {
    unsigned long random_number = my_random_range(0, 100);
    // Random number between 0 and 100
    printf("Random number: %lu\n", random_number); }
  return 0; }
