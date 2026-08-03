class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const anagramMap = {};
        for (let str of strs) {
            const sortedStr = str.split("").sort().join("");
            if (!anagramMap[sortedStr]) {
                anagramMap[sortedStr] = []
            }
            anagramMap[sortedStr].push(str)
        }
        return Object.values(anagramMap)
    }
}
