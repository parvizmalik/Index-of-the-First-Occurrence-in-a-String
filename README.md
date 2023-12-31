﻿# Index-of-the-First-Occurrence-in-a-String

Of course! Let's walk through the `strStr` function visually using the sample inputs: `haystack = 'abcxxy'` and `needle = 'xxy'`.

1. **Initialization**:
   - `haystack`: `'abcxxy'`
   - `needle`: `'xxy'`
   - Check if `needle` is empty; if it's empty, return 0 immediately. In our case, it's not.

2. **Outer Loop**:
   - We loop over `i` from `0` to `haystack.length - needle.length` (i.e., `3` in this case). This is because we're checking every possible starting position of `needle` in `haystack`.
   - Let's illustrate this with our example:

     ```
     Iteration 1: i = 0
     haystack: [a]bcxxy
     needle:   [x]xy

     Iteration 2: i = 1
     haystack: a[b]cxxy
     needle:   [x]xy

     Iteration 3: i = 2
     haystack: ab[c]xxy
     needle:   [x]xy

     Iteration 4: i = 3
     haystack: abc[x]xy
     needle:   [x]xy
     ```

3. **Inner Loop**:
   - For each iteration of the outer loop, there's an inner loop that checks if the segment of `haystack` starting from `i` matches `needle`.
   - We initialize a flag `matched` to `true` and assume there's a match unless proven otherwise.

4. **Checking for Matches**:
   - Let's consider the fourth iteration where `i = 3`:

     ```
     j = 0:
     haystack[i + j]: abc[x]xy -> 'x'
     needle[j]:       [x]xy    -> 'x'
     ```

     The characters match. So, we move to the next character.

     ```
     j = 1:
     haystack[i + j]: abc[x]xy -> 'x'
     needle[j]:       x[x]y    -> 'x'
     ```

     They match again. Move to the next character.

     ```
     j = 2:
     haystack[i + j]: abcx[x]y -> 'y'
     needle[j]:       xx[y]    -> 'y'
     ```

     They match for the last character of `needle` too.

5. **Returning the Result**:
   - Since all characters matched in the fourth iteration, the `matched` flag remains `true`. We exit the inner loop and check the `matched` flag. Since it's `true`, we return the value of `i`, which is `3`.
   - If no matches were found after all iterations, we'd return `-1`.

Running the `console.log(strStr('abcxxy','xxy'))` will indeed print `3`, indicating that the substring `'xxy'` starts at index `3` in the string `'abcxxy'`.
