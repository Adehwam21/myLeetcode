/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    var content = JSON.stringify(obj)
    return content.length <= 2 ? true : false
};