var getHeight = require('./binarySearchTree.js').getHeight;


depth1 = {
	right:null,
	left:null
}

depth2 = {
 	right: null,
 	left: {
 		left: null,
 		right:null
 	}
 }

 depth4 = {
 	val: "a",
 	left: {
 		val: "b",
 		left: {
 			val: "c",
 			right: {
 				val: "d"
 			}
 		}
 	},
 	right: {
 		val:"e"
 	}
 }


console.log("tree1 height is ", getHeight(depth1));
console.log("tree2 height is ", getHeight(depth2));
console.log("tree4 height is ", getHeight(depth4));

