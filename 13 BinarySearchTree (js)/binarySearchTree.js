

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
	Width = Math.pow(2,h) - 1;
	nodes = [{
		n: tree,
		pos: Math.pow(2,(h-1)) -1
	}];
	console.log(new Array(Width + 3).join("="));
	for (var d=h; d > 0; d--) {
		var line = new Array(Width + 1).join(" ");
		if (d>1) {
			span = Math.pow(2,(d-2));
		} else {
			span = 0;
		}
		spanLine = new Array(span + 1).join("-");
		nodes.forEach(function(el){
			line = line.substr(0, el.pos - span) + spanLine + el.n.val + spanLine + line.substr(el.pos + span + 1);
		});
		console.log("|" + line + "|");
		
		var nNodes = [];
		nodes.forEach(function(el) {
             if (el.n.right) {
             	nNodes.push({
             		n: el.n.right,
             		pos: el.pos + (Math.pow(2,(d-2)))
             	});
             }

              if (el.n.left) {
             	nNodes.push({
             		n: el.n.left,
             		pos:el.pos - (Math.pow(2,(d-2)))
             	});
             }
		});
		nodes = nNodes;
	}
	console.log(new Array(Width + 3).join("="));

}


module.exports = {
	getHeight: getHeight,
	draw: draw
};
