# Optimisation_Levenshtein
Python script improvments to reduce time and computations when distance is bounded.

## the Levenshtein Distance

the Levenshtein Distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.

## Basic principle
The Levenshtein algorithms is treated as a matrix where each character of the first word is a column (plus a blank) and each character of the second word is a row (plus a blank) as folow: 

X|" "|i|n|s|e|r|t|i|o|n
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
" "||||||||||
d ||||||||||
e ||||||||||
l ||||||||||
e ||||||||||
t ||||||||||
i ||||||||||
o ||||||||||
n ||||||||||

Then it will be filled as folow: 
each cell will represent actions count needed to move from one word to the other adding characters one by one.

First comparison, " " vs " ", does not need any change then the value of the corresponding cell is 0.

Second comparison, " " vs " i", need one change (add 'i'), then the value of the corresponding cell is 1.

Third comparison, " " vs " in", need one change (add 'i' and 'n'), then the value of the corresponding cell is 2.

...

It leads to: 

X|" "|i|n|s|e|r|t|i|o|n
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
" "|0|1|2|3|4|5|6|7|8|9
d ||||||||||
e ||||||||||
l ||||||||||
e ||||||||||
t ||||||||||
i ||||||||||
o ||||||||||
n ||||||||||

For the following rows here is the method:

First column: same logic as in the previous step. Comparing " " to " " then " d" to " " and so on.

For the other columns there is two cases: 

..* letters for the row 'i' and the column 'j' are the same:
There is no change needed in that case, the distance between the current state [i,j]  (for example " insert" vs " delet") is the same as it was 1 letter before for both words ("inser" vs "dele"). Then it's the same distance as it was in [i-1, j-1].

..* letters for the row 'i' and the column 'j' are different:


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

### Algorithmics
Let's check the performance of these two algorithms in terms of steps (computations) needed: 


__Exemple 1: 'levenshtein' VS 'distance'__

standart levenshtein: 96 steps (1 blank + 11 letters) * (1 blank + 8 letters)

upgraded levenshtein: 2 steps (2 pre-check conditions)

result: 97% less steps for this case (reject at the second condition i.e. length difference above threshold).

__Exemple 2: 'levenshtein' VS 'distances'__

standart levenshtein: 120 steps

upgraded levenshtein: 46 steps (2 pre-check conditions + 40 letters comparisons + 4 row checks)

result: 65% less steps for this case (reject during letters comparisons when distance above threshold).

__Exemple 3: 'levenstein', 'levenshtein'__

standart levenshtein: 132 steps

upgraded levenshtein: 145 steps (2 pre-check conditions + 132 letters comparisons + 11 row checks)

result: 10% more steps for this case. Same steps as in the standart version plus checks, useless in this case.

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


