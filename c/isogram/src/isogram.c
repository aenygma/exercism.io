#include <stdio.h>
#include "isogram.h"

bool is_isogram(const char phrase[]){

    int c;
    int i=0;
    int histsize=26;
    bool hist[histsize];

    // validate input
    if (phrase == NULL)
        return false;

    // init histogram
    for(int j=0; j<histsize; ++j)
        hist[j] = 0;

    while ((c=phrase[i]) != '\0'){
        ++i;

        // force everything to lowercase
        if ((c >= 'A') && (c <= 'Z'))
            hist[c-'A'] = true;

        // only account for alphabets
        if ((c >= 'a') && (c <= 'z'))
            hist[c-'a'] = true;
    }

    // validate if any > 0
    for(int j=0; j<histsize; ++j){
        if (hist[j] )
            return false;
    }

    return true;
}
