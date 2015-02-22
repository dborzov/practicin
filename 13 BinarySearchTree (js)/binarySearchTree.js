

// visualize binary search tree in a terminal

getHeight = function(node) {
	if (!node) {
		return 0;
	}

	return Math.max(
		getHeight(node.left), 
		getHeight(node.right)) + 1;
}



draw = function(tree) {
	h = getHeight(tree);
	Width = 2**h - 1;
	for (d:=0;d < h; d++) {
		console.log();
	}

}


module.exports = {
	getHeight: getHeight,
	draw: draw
};
