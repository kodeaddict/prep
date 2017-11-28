#!/usr/bin/bash
gcc -Wall -Werror -fpic -c -g3 src-akhil/*.c -o target.o &&
gcc -Wall -Werror -fpic -c -g3 ctype_tests/*.c -o ctypes-akhil.o &&
gcc -shared -o libtarget.so target.o &&
gcc -shared -o libakhil.so ctypes-akhil.o target.o &&
rm target.o
rm ctypes-akhil.o
