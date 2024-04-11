type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const filteredArr = [];
    
    for (var i = 0; i < arr.length; i++){
        if (fn(arr[i], i)){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
};
