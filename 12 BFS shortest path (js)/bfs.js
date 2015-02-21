module.exports.bfs = function(graph, start, finish) {
	var dist = {};
	dist[start] = [start];

	visitAdjNodes = function(i) {
		var adj = [];
		for (var j=0; j< graph[i].length; j++) {
			if (graph[i][j] === 1 && i !== j && !dist[j]) {
				adj.push(j);
				// if not visited, shortest distance
				dist[j] = dist[i].concat([j]);
			}
		}
		return adj;
	}

	var queue = visitAdjNodes(start);

	while (queue.length >0) {
		el = queue.pop();
		queue = visitAdjNodes(el).concat(queue);
	}

	return dist[finish];
}