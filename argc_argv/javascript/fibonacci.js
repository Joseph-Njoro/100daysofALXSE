const fibonacci = (n) => {
    const sequence = [0, 1];
    
    for (let i = 2; i <= n; i++) {
        sequence.push(sequence[i - 1] + sequence[i - 2]);
    }
    
    return sequence.slice(0 n);
}

const result = fibonacci(10);
console.log("Fibonacci Sequence:", result)