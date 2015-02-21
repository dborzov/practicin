var b = require('../traverseBinaryTree.js');
var test = require("tap").test


var root = {
	value: "root node yo",
	left: null,
	right: null
};

b.inOrder(root, function(node) {
	return node.value; 
})

test("make sure test thingy works", function(t) {
	t.equal("thing", "not a thing", "thingie should be thing");
	t.end();
});