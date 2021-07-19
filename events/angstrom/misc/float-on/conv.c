#include <stdio.h>
#include <stdint.h>

union cast {
	uint64_t a;
	double b;
};

int main() {
	union cast converter;
	double x;
	
	scanf("%lu", &converter.a);
	printf("%lu %0.18lf\n", converter.a, converter.b);
	scanf("%lf", &converter.b);
	printf("%lu %lf\n", converter.a, converter.b);
	return 0;
}
