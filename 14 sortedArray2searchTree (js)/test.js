//  test.js

var array2tree = require('./index.js').array2tree;
var draw = require('../13 BinarySearchTree (js)/binarySearchTree.js').draw;

var sortedArray1 = [0,1,2,3,4];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

var sortedArray1 = [0,1,2,3];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

var sortedArray1 = [0,1,2];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

var sortedArray1 = [0,1];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);

var sortedArray1 = [0,1,2,3,4,5,6,7,8,9];
tree = array2tree(sortedArray1);
console.log("Array:", sortedArray1);
draw(tree);