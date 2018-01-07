#include <stdio.h>
#include <string.h>

int urlify(char *url, int len)
{
    int newlen, i, idx, bcount = 0;

    for (i = 0; i < len; i++) {
        if (url[i] == ' ')
            bcount++;
    }

    /* no blank in given url, return success */
    if (bcount == 0)
        return 0;

    newlen = len + (2 * bcount);
    url[newlen] = '\0';
    idx = newlen - 1;
    for (i = len - 1;  i >= 0; i--) {
        if (url[i] == ' ') {
            url[idx] = '0';
            url[idx - 1] = '2';
            url[idx - 2] = '%';
            idx -= 3;
        } else {
            url[idx--] = url[i];
        }
    }
    return 0;
}

#if 0
int main()
{
    char url[200] = "hello world sathesh";
    printf ("ip = %s\n", url);
    urlify (url, strlen(url));
    printf ("op = %s\n", url);

}
#endif
