#include <stdio.h>

int main() {
    int i, j, v, N;
    int array[100];
    int cnt = 0;
    
    scanf("%d", &N);
    for (i = 0; i < N; i++) {
        scanf("%d",&array[i]);
    }
	
    scanf("%d", &v);
    for (j = 0; j < N; j++) {
        if(array[j] == v)
            cnt++;
    }
    
    printf("%d", cnt);
    return 0;
}