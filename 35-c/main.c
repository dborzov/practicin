# include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  char *breaking_internets;
  breaking_internets = (char *) malloc(50);
  unsigned char cur = 0;
  while (breaking_internets[cur] != 'f') {
    cur++;
    breaking_internets[cur] = getchar();
    breaking_internets[cur+1] = '\0';
    printf("breaking_internets[%d]=%c \n",cur, *breaking_internets);
  }
  printf("here is the code: %c \n", *breaking_internets);
  return 0;
}
