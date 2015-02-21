
var bfs = require('./bfs.js').bfs;

var graph = [
	[1,0,1,0],
	[0,1,1,1],
	[1,1,1,0],
	[0,1,0,1]
];

console.log("Distances to things: ", bfs(graph,0,3));