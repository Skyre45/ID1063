#include <stdio.h>

int main() {
    unsigned int hours, minutes, seconds;
    unsigned int totalSeconds;

    /* Read input here. The format specifier is %u. */
    scanf("%u %u %u", &hours, &minutes, &seconds);
    /* Compute and print totalSeconds here */
    totalSeconds = hours*60*60 + minutes*60 + seconds;
    printf("%u", totalSeconds);
    return 0;
}
