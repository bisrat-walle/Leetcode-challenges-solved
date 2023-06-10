# Generate binary string
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a string containing of <strong>0</strong>, <strong>1</strong> and <strong>?</strong> - a wildcard character, generate all distinct&nbsp;<strong>binary strings</strong> that can be formed by replacing each wildcard character by either <strong>0</strong> or <strong>1</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>1??0?101
<strong>Output: </strong>10000101 10001101 10100101 10101101 
11000101 11001101 11100101 11101101
<strong>Explanation:
</strong>There will be 8 such possible strings that 
can be formed, they are 10000101, 10001101, 
10100101, 10101101, 11000101, 11001101, 
11100101 and 11101101.
</span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input: </strong>10?</span>
<strong><span style="font-size:18px">Output: </span></strong><span style="font-size:18px">100 101</span>
<span style="font-size:18px"><strong>Explanation: </strong>There are 2 such possible strings
and they are 100 and 101.</span>
</pre>

<p><strong><span style="font-size:18px">Your Task:</span></strong><br>
<span style="font-size:18px">You don't need to read or print anything. Your task is to complete the function&nbsp;<strong>generate_binary_string()&nbsp;</strong>which takes the given string as input parameter and returns a vector of strings containing all the possible strings that can be formed.</span></p>

<p><span style="font-size:18px"><strong>Note :&nbsp;</strong>Strings should be printed in lexicographically&nbsp;increasing order.</span></p>

<p><span style="font-size:18px"><strong>Expected Time complexity: </strong>O(2<sup>n</sup>)</span><br>
<span style="font-size:18px"><strong>Expected Space complexity:&nbsp;</strong>O(n*2<sup>n</sup>)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤&nbsp;length of string ≤ 30</span><br>
<span style="font-size:18px"><strong>Note:</strong>&nbsp;Number of '<strong>?</strong>' in&nbsp;any&nbsp;string does not exceed 15.</span></p>
</div>