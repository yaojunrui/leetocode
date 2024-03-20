/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let word = ""; //store the prefix
    let words = ""; //store the previous prefix
    let count = 0; // count which char

    while (count != strs[0].length){
        words = word;
        word += strs[0][count];

        for (let i = 1; i < strs.length; i++){
            if (word[count] !== strs[i][count]){
                word = words;
                break;
            }
        }

        if (word === words){
            break;
        }

        count++;
    }

    return word;
};