function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const returned_array = [];
    
    
    for (var i = 0; i < arr.length; i++){
        returned_array.push(fn(arr[i], i ));
    }
    
    return returned_array;
};
