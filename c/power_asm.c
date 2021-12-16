// Ben et Romain

// Tout ca pour utiliser l'instruction bsf.....

// base<2^32, expo<2^64, modula<2^32

// bien mais pas ouf, bcp de calcule redondant (parcourir exp de gauche a droite)

#include <stdlib.h>
#include <stdio.h>


extern u_int64_t powo(u_int64_t, u_int64_t, u_int64_t);
__asm__(".globl powo\n\t"
        ".type func, @function\n\t"
	"powo:\n\t"
		"mov rax, 1;\n\t" // init
		"mov r8, rdx;\n\t"

	"encore:\n\t"
		"bsf rcx, rsi;\n\t" // recup index premier 1

		"mov r9, 1;\n\t"  // retire le 1 trouve
		"shl r9, cl;\n\t" // (shl ne fonctionne qu'avec cl comme 2eme ope)
		"xor rsi, r9;\n\t"

		"xchg rax, r9;\n\t" // sauvegarde resultat temporaire
		"mov rax, rdi;\n\t"

	"partiel:"
		"cmp rcx, 0;\n\t"
		"jz next;\n\t"

		"imul rax;\n\t" // evite que ca deborde
		"idiv r8;\n\t" // recupere le modulo
		"mov rax, rdx;\n\t"

		"loop partiel;\n\t"

	"next:"
		"imul r9;\n\t" // assemble resultat partiel et le precedent
		"idiv r8;\n\t" // recupere le modulo
		"mov rax, rdx;\n\t"

		"cmp rsi, 0;\n\t" // c'est fini
		"jnz encore;\n\t"

		"ret;\n\t");

int main(){
	u_int64_t res = powo(4294967295,18446744073709551615, 4294967293);
/* 	printf("%lu\n", res); */
}

