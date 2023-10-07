//needle , haystack

const strStr = (haystack, needle) => {
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let matched = "true";

    for (let j = 0; j < needle.length; j++) {
      if (haystack[i + j] != needle[j]) {
        matched = false;
        break;
      }
    }
    if (matched) {
      return i;
    }
  }
  return -1;
};

console.log(strStr("abcxxy", "xxy"));
