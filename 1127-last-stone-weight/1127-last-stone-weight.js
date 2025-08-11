/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {

    stones.sort((a, b) => b - a)
    let left = 0
    let right = 1
    while (stones.length > 1) {
        if (stones[left] === stones[right]) {
            stones.shift()
            stones.shift()

        } else if (stones[left] !== stones[right]) {
            stones.push(stones[left] - stones[right])
            stones.splice(right, 1)
            stones.splice(left, 1)
            stones.sort((a,b)=>b-a)
        }
    }
    return stones.length === 0 ? 0 : stones[0]
};