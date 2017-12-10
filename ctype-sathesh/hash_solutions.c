
#include "../include/hash.h"
#include <stdint.h>


bucket_t hash_fn(voidp key, bucket_t max_bkt)
{
    return (long*) key / max_bkt;
}
int compare_fn(voidp key, voidp comparewith)
{
    long *p1 = key, *p2 = comparewith;

    if (*p1 == *p2)
        return 0;
    else
        return 1;

}
void dump_fn(voidp key, voidp data)
{
}

/*
 * Verify that there are no duplicate numbers in an array
 * num [input] is array of integers
 * len [input] length of the array
 * Return value
 *    true: duplicate present
 *    false: no duplicates
 */

int
check_duplicate_numbers(int *num, int len)
{
      int i;
      hashCookie cookie = hash_init(10, hash_fn. cmp_fn, NULL);

      for (i=0; i < len; i++) {
         if(hash_lookup(cookie, (voidp) (intptr_t) num[i])) {
            // duplicate
            return 1;
         }
         hash_insert(cookie, (voidp) (intptr_t) num[i], 0);
      }
      return 0;
}
