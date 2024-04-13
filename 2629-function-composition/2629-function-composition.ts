type F = (x: number) => number;

function compose(functions: F[]): F {
    
    return function(x) {
        var f1 = x;
        for (var i = functions.length - 1 ; i > -1; i--){
            f1 = functions[i](f1);
        }
        return f1;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */