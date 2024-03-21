#include <stdio.h>
#include <stdlib.h>

int main() {
  int m, n, i, j, sum = 0;

  printf("Enter rows and columns: ");
  scanf("%d%d", &m, &n);

  int (*matrix)[n];
  matrix = (int (*)[n]) malloc(m * n * sizeof(int));
  if (matrix == NULL) {
    printf("Memory not allocated");
    exit(0);
  }

  printf("Enter elements: ");
  for (i = 0; i < m; i++)
    for (j = 0; j < n; j++)
      scanf("%d", *(matrix + i) + j);

  printf("The matrix is: ");
  for (i = 0; i < m; i++) {
    for (j = 0; j < n; j++)
      printf("%d ", *(*(matrix + i) + j));
    printf("\n");
  }

  printf("The sum of elements is: %d", sum);

  free(matrix);
  return 0;
}