#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
Every time a passes through the loop, it's value is added by `n^2`. Therefore the time it will take to reach `n^3` is `n^3 / n^2` which is just `n`. Therefore, `a` passes through the loop a total of `n` times.


b) O(n log n)
Each time `j` is going through the while loop it's value is multiplied by `2`, so it will have gone `log n` times through the while loop before reaching the end. And that is repeating itself `n` times through the for loop, so that's why its `n` multiplied by `log n`.


c) O(n)
The value if n is decremented by one each time it passes through the method

## Exercise II
Start a for loop with variable `i` between `1` and `n + 1`, . Drop an egg each time to see if it breaks or not. If the egg breaks, set the value of `f` to `i` and then break out of the loop. If the egg doesn't break, continue through the loop.
```
for i in range(1, n + 1):
    if egg breaks:
        break
```
This means that the code won't reach the end of the loop and will stop midway. Therefore, the runtime complexity should be `O(f)`

