#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main() {
    int n;
    long l;
    char c;
    float f;
    double d;

    scanf("%d %ld %c %f %lf", &n, &l, &c, &f, &d);

    printf("%d\n", n);
    printf("%ld\n", l);
    printf("%c\n", c);
    printf("%.3f\n", f);
    printf("%.9f", d);
    
    return 0;
}
