/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let temp = x.toString();
    
    let reverse_string = temp.split("").reverse().join("");
    
    return temp === reverse_string;
        
};