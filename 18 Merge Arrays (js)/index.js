module.exports.merger = function(a1, a2) {
    var p1 = 0,
        p2 = 0;
    var merger = [];

    while(p1 < a1.length && p2 < a2.length) {
 		if (a1[p1] > a2[p2]) {
 			merger.push(a2[p2]);
 			p2++;
 		} else {
 			merger.push(a1[p1]);
 			p1++;
 		}
    }

    if (p1 === a1.length) {
    	leftovers = a2.slice(p2);
    } else {
    	leftovers = a1.slice(p1);
    }
    merger = merger.concat(leftovers);
    return merger;
};