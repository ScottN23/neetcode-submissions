class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const numMap = new Map();
        for (let i = 0; i < nums.length; i++) {
            const num = nums[i];
            const difference = target - num;
            const sumIndex = numMap.get(difference);

            if (numMap.has(difference)) {
                return [i, sumIndex];
            }
            numMap.set(nums[i], i);
        }
        return [-1, -1]
    }
}
