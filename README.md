## Question:
Given a list of chords in a circle, count the number of intersections, if any. For smiplicity's sake, assume all starting and ending points are unique.

### Solution:

## Time complexity:

`The problem can be solved in O(nlogn) time complexity in Python and O(n) time complexity in Java, C++. The space complexity is O(n).`

## Algorithm:

`The idea behind algorithm is any chord 'x' will intersect other chord 'y' if its start 's_x' or end 'e_x' (not both) is in between the start 's_y' and end 'e_y' of the chord y.` 

## Assumptions:

1) Radian Measure list is sorted
2) Identifier are denoted as `sx` and `ex`
3) `sx <= ex`

## How to run:

Step 1:
Set the input test cases in the `main` function using list `input_radians_identifiers`.

Step 2:
run `python solution.py`

Output:
The `solution.py` prints `intersection` values for all test cases.

## Variables:

`chord_ranks`   - An hashmap to maintain the order of chords (helps in optimizing search for start point of a chord).
`active_chords_bv` - An integer to track all active chords (bitwise operations).
`total_chords`  - total number of chords parsed.
`intersection`  - output variable.

## Functions:
`find_intersections` - Finds number of intersections give correct input [(radian measures), (identifiers)]
`count_bits_to_right` - Finds number of set bits to the right of the rank bit. 

## Code Explanation:

Firstly we create a 'chord_ranks' hashmap by iterating the radian identifiers in reverse orders. At every time encountering a new start point 'sx' we add it to the hashmap with key 'sx' and value 'total_chords'. The 'total_chords' variable maintains number of chords encountered until current iteration.

After creating a hashmap we start iterating through the radian identifiers in the given order. At every time we encounter a 'sx' we create a bit vector and set the bit at ('rank'==chord_ranks['sx']) to 1.

Upon encountering an end point 'ex' we find the 'rank' of corresponding 'sx' from the hashmap 'chord_ranks' and increment the 'intersections' by the total number set bits positioned at the right of the 'rank' bit.

After completing the loop we return the 'intersections' output.

## Note !
`The bitcount operation in Java, C++ languages has O(1) time complexity, due to limit on integer size. Therefore the current solution in C++ or Java would be O(n) complexity.
Where as in Python-3 the bitcount is O(logn) due to uncapped integer size. Hence the final complexity of current solution is O(nlogn).`
