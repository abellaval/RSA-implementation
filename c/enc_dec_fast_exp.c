#include "python.c"

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


/* Optimisation commique pour clef pas trop grande, B_SIZEx plus rapide que lettre par lettre :o */

const unsigned B_SIZE = 3; // valeur max 4 si N est assez grand (si non deborde de u_int64_t en faisant (x^2)%n ((2^32)^2)%n OK ?)


u_int64_t* convToBigInt(char* m, const u_int64_t s){
	u_int64_t* res = (u_int64_t*) calloc(s, sizeof(u_int64_t));
	for(u_int64_t i=0; i<s; ++i) res[i] = *(m++);
	return res;
}

char* convToChar(u_int64_t* m, const u_int64_t s){
	char* res = (char*) calloc(s, sizeof(char));
	for(u_int64_t i=0; i<s; ++i) res[i] = *(m++);
	return res;
}

u_int64_t* encrypt(const char* const m, const u_int64_t s, const u_int64_t pw, const u_int64_t n){
	const unsigned B_MAX = (s/B_SIZE) + ((s%B_SIZE)!=0);

	u_int64_t* const res = (u_int64_t*) calloc(B_MAX, sizeof(u_int64_t));
	u_int64_t tmp, offset;
	char* const p = (char*)(&tmp);
	unsigned i, j;

	for(i=0; i<B_MAX; ++i){ // threading possible
		tmp = 0;
		for(j=0; j<B_SIZE; ++j){
			offset = i*B_SIZE+j;
		  if(offset==s) break;
			p[j] = m[offset]; // Such waow UwU
		}
		res[i] = powo(tmp, pw, n);
	}
	return res;
}

char* decrypt(const u_int64_t* const m, const u_int64_t s, const u_int64_t pw, const u_int64_t n){
	const unsigned B_MAX = (s/B_SIZE) + ((s%B_SIZE)!=0);

	char* res = (char*) calloc(s, sizeof(char));
	u_int64_t i, tmp, offset;
	char* const p = (char*)(&tmp);
	unsigned j;

	for(i=0; i<B_MAX; ++i){ // threading possible
		tmp = powo(m[i], pw, n);
		for(j=0; j<B_SIZE; ++j){
			offset = i*B_SIZE+j;
		  if(offset==s) break;
		   	res[offset] = p[j]; // Such waow UwU
		}
	}
	return res;
}


int main(){
	char m[] = "This a long string I want to try out !!";
	/* /1* char m[] = "aaaa"; *1/ */
	auto s = strlen(m);
	printf("Before encrypt: %s\n", m);
	u_int64_t* msgBig = encrypt(m, s, 18632293,  18641003);
	char* msgChar = decrypt(msgBig, s, 11711749, 18641003);
	printf("After decrypt: %s\n",msgChar);
}

