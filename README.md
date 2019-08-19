# Optimisation_Levenshtein
Python script improvments to reduce time and computations when distance is bounded.

## the Levenshtein Distance

the Levenshtein Distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

## Basic principle


## Improved Principle

### Words Length
If the length difference between words is bigger than the threshold defined, the process is stopped before computations.
Since the difference is bigger than the treshold the Levenshtein distance will be at least the value of the difference and then over the treshold.

### Current maximum value
Using previous explanations like the distance can not decrease and cell computation is based on [i, j-1], [i-1, j-1] and [i-1, j] it's possible to cut the process before the end.
At the end of each row, if the maximum value of the latter is above the treshold then the process can be stopped since it cannot decrease.

### Matrix axis
Based on the algorithm mechanism (i.e. filling row by row) the shorter word have to be placed on the j's axis and the longer on on the i's axis. 
It allow to check more often the maximum value of rows and reduce possible unnecessary computations.

### 
'levenshtein' VS 'distance'
2 (pre-check) steps
96 steps
97% faster

'levenshtein' VS 'distances'
2 (pre-check) + 40 (cells) + 4 (row check) = 42 steps
120 steps
65% faster

'levenstein', 'levenshtein'
2 (pre-check) + 132 (cell) + 11 (row check) = 145 steps
132 steps
10% slower

## Results
Time needed to compute two differences is divided by 2 or 3! 

```python
start = time.time()
levenshtein('levenshtein', 'distance')
levenshtein('levenshtein', 'distances')
levenshtein('levenstein', 'levenshtein')
print('Standart Levenshtein (no "max_value" in it): ' + str(time.time() - start))

start = time.time()
levenshtein_upg('levenshtein', 'distance')
levenshtein_upg('levenshtein', 'distances')
levenshtein_upg('levenstein', 'levenshtein')
print('Upgraded Levenshtein (with "max_value = 2"): ' + str(time.time() - start))
```

```
Standart Levenshtein (no "max_value" in it): 0.0007631778717041016
Upgraded Levenshtein (with "max_value = 2"): 0.00024628639221191406
```


