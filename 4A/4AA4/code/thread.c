#include <stdio.h>
#include <pthread.h>

int g = 0;

void *aThread() {
    g++;
    printf("%d\n", g);
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    int i;
    pthread_t thread[3];
    for (i=0; i<3; i++) {
        if ( pthread_create( thread+i, NULL,aThread, NULL) ) {
            printf("ERROR; return code from pthread_create()\n");
            return -1;
        }
    }
    printf("the value of g is %d\n", g);
    return 0;
}