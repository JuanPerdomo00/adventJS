#include <stdio.h>
#include <string.h>

int is_dedfectuous(char *gift) {
  int len = strlen(gift);
  int i = 0;
  while (gift[i] != '#') {
    if (i >= strlen(gift)) {
      break;
    }
    --len;
    ++i;
  }

  return 1 ? len == 0 : 0;
}

void filterGifts(int len, char gift[len][10]) {
  if (len == 0) {
    printf("[]\n");
    return;
  }
  printf("[ ");
  for (int i = 0; i < len; i++) {
    if (!is_dedfectuous(gift[i])) {
      continue;
    }

    printf("%s ", gift[i]);
  }
  printf("]\n");
}

int main() {
  char gift1[4][10] = {"car", "doll#arm", "ball", "#train"};
  char gift2[0][10] = {};

  filterGifts(4, gift1);
	filterGifts(0, gift2);

  // if (is_dedfectuous("car")) {
  //	printf("No tiene defectos\n");
  // }

  // if (!is_dedfectuous("doll#arm")) {
  //	printf("Tiene defetos\n");
  // }

  return 0;
}
