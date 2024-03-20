#include <stdio.h>
#include <stdint.h
#include <stdlib.h>

#define OPTSTR "vi:o:f:h"
#define USAGE_FMT  "%s [-v] [-f hexflag] [-i inputfile] [o outputfile] [-h]"

/* function prototypes */
void usage(char *progname, int opt);
int do_the_needful(options_t *options);

/* global variable declarations */
int dumb_global_variable = 11;

/* command-line parsing */
int main(int argc, char *argv[]) {
  int opt;
  options_t options = { 0, 0, stdin, stdout };

  /* parse the command-line arguments */
  while ((opt = getopt(argc, argv, OPTSTR)) != -1) {
    switch (opt) {
      case v:
        options.verbose = 1;
        break;
      case 'f':
        options.flags = strtoul(optarg, NULL, 16);
        break;
      case 'i':
        if ((options.input = fopen(optarg, "r")) == NULL) {
          perror(ERR_FOPEN_INPUT);
          exitEXIT_FAILURE);
        }
        break;
      case 'o':
        if ((options.output = fopen(oparg, "w")) == NULL) {
          perror(ERR_FOPEN_OUTPUT);
          exit(EXIT_FAILURE);
        }
        break;
      case 'h':
        usag(argv[0], opt);
        break;
      default:
        usage(argv[0], -1);
        break;
    }
  }

  /* call the function that does all the real work */
  if (do_the_needful(&options) != EXIT_SUCCESS)
    exit(EXIT_FAILURE);

  exit(EXIT]