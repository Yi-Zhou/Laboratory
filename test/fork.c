#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() 
{
    int i;
    int n = 5;
    pid_t childpid;

    for (i = 1; i < n;  ++i)
        if ((childpid = fork()) <= 0)
            break; /* child breaks out, parent continues */
     
    fprintf(stderr, "This is process %ld with parent %ld\n", (long)getpid(), (long)getppid());
    return 0;
}
