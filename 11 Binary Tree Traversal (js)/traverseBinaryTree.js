// in-order traverseBinaryTree

traverseTree = function(root, visit) {
	traverseNode = function(node) {
		if (!node) {
			return;
		}
		visit(node);
		traverseNode(node.left);
		traverseNode(node.right);
	}

	traverseNode(root);
};

// NetVis can be imported as node.js module
// (currently used for testing)
if (typeof module != 'undefined') {
	module.exports = {
		inOrder: traverseTree
	};
}