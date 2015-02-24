var array1 = [52, 57, 78 ,79,80,81,82,84];
var array2 = [0,20,21,54,55,56,57,78];

var merger = require('./index.js').merger;

merged = merger(array1,array2);
console.log(new Array(20).join("="));
console.log("array1: ", array1);
console.log("array1: ", array2);
console.log(new Array(20).join("~"));
console.log("Merged : ", merged);
console.log(new Array(20).join("+"));

