getHeight = require('../13 BinarySearchTree (js)/binarySearchTree.js').getHeight;


var array2tree = function(array) {
	traverseSlice = function(low, high) {
		if (low >= high) {
			return null;
		}
		height = Math.ceil(Math.log2((high - low) + 1));
		mid = low + Math.pow(2,height-1) - 1;
		// console.log("low ", low, " mid ", mid, " high ",high);
		return {
			val: array[mid],
			left: traverseSlice(low, mid),
			right: traverseSlice(mid + 2, high)
		};
	} 

	var low = 0,
	    high = array.length;
	return traverseSlice(low, high);
}




module.exports = {
	array2tree: array2tree
};