'''
70. Climbing Stairs
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

def stair(remaining:int) -> int: return 1 if remaining <= 1 else stair(remaining-1) + stair(remaining-2)


print(stair(20))


# final solution, must be optimized with a dict of already find solutions, depending on the size

class Solution(object):
    def climbStairs(self, remaining): 
        return 1 if remaining <= 1 else self.climbStairs(remaining-1) + self.climbStairs(remaining-2)