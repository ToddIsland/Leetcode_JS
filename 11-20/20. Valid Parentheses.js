/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = new Array();
    for(let i =0;i<s.length;i++){
        let char = s[i];
        if(char == '('){
            stack.push(')');
        }
        else if(char == '['){
            stack.push(']');
        }
        else if(char == '{'){
            stack.push('}');
        }
        else if(stack.length == 0 || stack.pop() != char){
            return false;
        }
    }
    return stack.length == 0;
};