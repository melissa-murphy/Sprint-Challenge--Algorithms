#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because it must touch everything 


b) O(nlog(n)) 
Because it has both a for loop: O(n)
and a while loop: O(log(n))


c) O(n) -- more bunnies == more to touch.

## Exercise II

The last time I worked on this question, I didn't think about the "broken eggs is minimized" aspect. So instead of a for loop that starts at the bottom and moves up 1 until an egg breaks is not the most efficient. For this we would want to implement a binary search.
Find the upper/lower limits, divide in half, then while found floor is false, run through an if/elif loop
