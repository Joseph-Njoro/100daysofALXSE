const fibonacci = (n) => {
    const sequence = [0, 1];
    
    for (let i = 2; i <= n; i++) {
        sequencepush(sequence[i - 1] + sequence[i - 2]);
    }
    
    return sequenceslice(0 n);
}

const result = fibonacci(10);
console.log("Fibonacci Sequence:", result)