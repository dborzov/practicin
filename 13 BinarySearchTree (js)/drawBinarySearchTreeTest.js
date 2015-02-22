var draw = require('./binarySearchTree.js').draw;

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
 };

 draw(depth4);
