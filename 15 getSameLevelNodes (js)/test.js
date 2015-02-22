var getSameLevelNodes = require('./index.js').getSameLevelNodes;
var array2tree = require('./index.js').array2tree;
var draw = require('../13 BinarySearchTree (js)/binarySearchTree.js').draw;

 var traverseLinkedList = function(el) {
 	console.log(new Array(20).join("-"));
 	console.log("Traversin\' linked list: ", el);
 	while (el.next) {
 		el = el.next;
 		console.log(" ..to ", el.val);
 	}
 }


var sortedArray1 = [0,1,2,3,4];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

 var lls = getSameLevelNodes(tree);
lls.forEach(function(el) {
	traverseLinkedList(el);
});