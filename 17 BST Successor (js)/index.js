var array2BST = require('../14 sortedArray2searchTree (js)/index.js').array2tree;
var draw = require('../13 BinarySearchTree (js)/binarySearchTree.js').draw;

var sortedArray1 = [0,1,2,3,4,5,6,7,8,9];
tree = array2BST(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

// reformulate in-order traversal with explicit stack
continueTraversing = function(stack) {
	while(stack.length >0) {
		var el = stack[stack.length -1];

		// left node was not checked out yet
		if (!el.left) {
			el.left = true;
			if (el.p.left) {
				el.p.left.parentLeft = el.p;
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
				el.p.right.parentRight = el.p;
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
};

continueTraversing([{
	left: false,
	right: false,
	p: tree
}]);

sel = tree.left.right.right;
console.log("Selected node is: ", sel.val);

stack = [{
	left:true,
	right: false,
	p: sel
}];

while(sel.parentLeft || sel.parentRight) {
	if (sel.parentLeft) {
		stack.unshift({
			left:true,
			right:false,
			p:sel.parentLeft
		});
		sel = sel.parentLeft;
	} else {
		stack.unshift({
			left:true,
			right:true,
			p:sel.parentRight
		});
		sel = sel.parentRight;
	}
}

console.log("~~~~~~~~~~~~~~~~~~~~")
continueTraversing(stack);
