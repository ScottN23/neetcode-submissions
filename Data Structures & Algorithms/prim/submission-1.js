/**
 * const PriorityQueue = require('priority-queue-js');
 */

class Solution {
    /**
     * @param {number} n
     * @param {Array<Array<number>>} edges
     * @returns {number}
     */
    minimumSpanningTree(n, edges) {
        const adj = {};
        for (let i = 0; i < n; i++) {
            adj[i] = [];
        }

        for (let [n1, n2, w1] of edges) {
            adj[n1].push([n2, w1]);
            adj[n2].push([n1, w1]);
        }

        const minHeap = new PriorityQueue((a, b) => a[0] - b[0]);
        minHeap.enqueue([0, 0]);

        let res = 0;
        const visited = new Set();
        
        while (!minHeap.isEmpty() && visited.size < n) {
            const [weight, v] = minHeap.dequeue();
            if (visited.has(v)) {
                continue;
            }

            res += weight;
            visited.add(v);

            for (const [neighbor, weight] of adj[v]) {
                if (!visited.has(neighbor)) {
                    minHeap.enqueue([weight, neighbor]);
                }
            }
        }
        
        return visited.size === n ? res : -1;
    }
}
