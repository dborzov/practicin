var array2BST = require('../14 sortedArray2searchTree (js)/index.js').array2tree;
var draw = require('../13 BinarySearchTree (js)/binarySearchTree.js').draw;

var sortedArray1 = [0,1,2,3,4,5,6,7,8,9];
tree = array2BST(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

// reformulate in-order traversal with explicit stack
stack = [{
	left: false,
	right: false,
	p: tree
}];


while(stack.length >0) {
	var el = stack[stack.length -1];

	// left node was not checked out yet
	if (!el.left) {
		el.left = true;
		if (el.p.left) {
			stack.push({
				left: false,
				right: false,
			p: el.p.left}
			);
		}
 		continue;
	}

	if (!el.right) {
		console.log("print value: ", el.p.val);
		el.right = true;
		if (el.p.right) {
			stack.push({
				left: false,
				right: false,
				p: el.p.right
			});
		}
		continue
	}

	// if (el.right && el.left)
	stack.pop();
}