type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    var val: number = init;
    if (nums.length > 0){
        for (var i = 0; i < nums.length; i++){
            val = fn(val, nums[i]);
        }
        return val;
    } else {
      return init;  
    }
};