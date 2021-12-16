#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <time.h>

/*
type of values : int64_t
max value : 2^63 - 1
*/

// Bézout coefficients
int64_t findInvREAL(int64_t e, int64_t phiN) {
    int64_t a = phiN;
    int64_t b = e;
    int64_t q, r;
    int64_t prev[2] = {1,0};
    int64_t curr[2] = {0,1};
    int64_t x, y;
    while (b != 0) {
        q = a/b;
        r = a%b;
        x = prev[0] - curr[0] * q;
        y = prev[1] - curr[1] * q;
        a = b;
        b = r;
        prev[0] = curr[0]; prev[1] = curr[1];
        curr[0] = x; curr[1] = y;
    }
    return prev[1];
}

int64_t pgcdEuclide(int64_t a, int64_t b) {
    int64_t first = a, second = b, tmp;
    while (b != 0) {
        tmp = a;
        a = b;
        b = tmp%b;
    }
    return a;
}

// Chose e
int64_t choseEps(int64_t phiN) {
    if (phiN > 257 && pgcdEuclide(phiN, 257))
        return 257;
    if (phiN > 65537 && pgcdEuclide(phiN, 65537))
        return 65537;
    for(int64_t i = 3; i < phiN; ++i) {
        if (pgcdEuclide(phiN, i))
            return i;
    }
    return 0;
}

// Return square root
int64_t sqroot(int64_t val) {
    int64_t counter = 1;
    int64_t sqr = 1;
    while (sqr <= val) {
        ++ counter;
        sqr = counter*counter;
    }
    return counter-1;
}


// Check if number is prime
int isPrime(int64_t numb) {
    int64_t root = sqroot(numb);
    for (int64_t i = 2; i <= root; ++i) {
        if (numb % i == 0) {
            return 0;
        }
    }
    return 1;

}

// Generate a number
int64_t genRandom() {
    int64_t randval;
    FILE *f;
    f = fopen("/dev/random", "r");
    fread(&randval, sizeof(int32_t), 1, f);
    fclose(f);
    return  randval>>5;     // phi and phiN are sometimes too big without the shift
}

// Return a generated prime number
int64_t genNum() {
    int prime = 0;
    int64_t generatedNum = 0;

    while (!prime) {
        generatedNum = genRandom();
        prime = isPrime(generatedNum);        
    }
    
    return generatedNum;
}


int main() {
    

    // Generating prime numbers
    int64_t p = genNum();
    int64_t q = genNum();
    while (p == q) {
        q = genNum();
    }
    
    // N and phiN
    int64_t N = p*q;
    int64_t phiN = (p-1)*(q-1);

    // e prime with phiN
    int64_t e = choseEps(phiN);

    // d = inv e % phiN
    int64_t d = findInvREAL(e, phiN) % phiN;
    while (d < 0) {
        d += phiN;
    }

    // TO DELETE
    int64_t res = (e*d) % phiN;
    printf("%lu\n", res);
    

    // print keys
    printf("phiN = %lu\n", phiN);   // TO DELETE
    printf("Public key :\nN : %lu\ne : %li\n", N, e);
    printf("Secret key :\nN : %lu\nd : %li\n", N, d);
}