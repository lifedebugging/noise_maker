"""
i want to try writing a function and then maybe i can use that code to put in my github that i wrote my own noise maker i can name it noise maker function that takes any query and add noises on fly so to add noises on fly i need a lazy generator 
that would be good quick exercise for me to write something fun
i should structure it first
to add a noise i need a function
- that takes a input as in *args **kwargs and number of test case they need if empty it will random.rand to generate anywhere between 50-100 test case
- then the query can be check for numbers and special letter
- and using type or instance convert all to string 
- that will give us alphanumeric string
- and use .re we strip all the special letter because in reality not every special letter count to intent but we are not checking intent its a function to create set of test case with human like error and multi similar test case
- if user provide special letter preserve it if it does not we use our own re to put special letter like ! or ?? double question mark, test case we can add capital letters, swap the word from first to second or add one word typo, and we could makethetest with no space
- this could check variety of edge cases such as variables and human errors
- to achieve that we need something that we can loop over each word and if needed each letter in word in query
- we can either string method to convert the string to [] list with space as delimeter 
- or since we thinking of using generator we can convert it to tuple 
- and with some logic in between it add all the error and does swapping etc etc..
- and it provide a clean list of set test case upto given number of test case since we will append in a list and we will generator it won't stress the memory  

"""

"""
A Few Architectural Tips to Keep in Mind Before You Code

    Input Signature: Since your function needs a base query to mutate, think about how it will accept that source string. Will it take a base query as the primary argument, followed by your *args / **kwargs for configuration?

    Independent vs. Cascading Mutations: Decide whether each yielded item should apply one random mutation to the base query (e.g., just a typo or just a swap), or if you want some iterations to stack multiple errors together (e.g., a typo plus a case shift plus missing spaces). Keeping them mostly independent at first makes it easier to trace why a test case failed.

    Generator vs. List Accumulation: You mentioned appending to a list and using a generator. Remember: a pure generator yields items on the fly one by one, so you don't actually need an internal results = [] list unless you want to shuffle or deduplicate the final batch before returning it.
    
    """

"""
yes i think args kwargs not needed it should take a single base primary input in a variable input and convert it to string right there
yes you're right on second we need multiple similar like typo error say
thisismistake - this one route to gibbirish 
and the next is just normal query then we won't have any data to determine whether the all will router to gibbirish
so we need like 10 at least of with no space thisismistake so we know it all routes there if someone is writing an accuracy test i wonder if it will make it easier to test
and then followed by 10-20 of single typo mistakes like that 
so we don't need list accumulation then what we need there so it just yeild to result? diectly
"""

"""
so wait uh i was thinking that in the end it will give the user using my function a list or something that they can directly loop over in their custom function 
or do i stick to yield such that a person writing test case can integrate my noise maker in thier function or maybe i write a class so you can inherit and call without adding complexity

"""

"""
Here is the secret weapon in Python: You don't actually have to choose between a generator and a list.

If you write your function using yield (making it a generator), the caller has total flexibility:

    If they want to loop over it lazily: They can just write for noisy in noise_maker("query"): and it streams items one by one.

    If they want a plain list: They can wrap it instantly in a list constructor: test_batch = list(noise_maker("query")).

By returning a generator, you give them the memory-efficient streaming option and the list option all in one.

As for using a class versus a function:

    A standalone function is usually best if it's just a utility that transforms input to output without needing to remember state.

    A class is only really worth it if you want to store configuration state—like setting a global random seed, configuring a default noise intensity, or keeping track of how many mutations have been generated across sessions.
    
"""
### pseudo code

"""
def function (takes input, and kwargs/ number_of_case = pos int/none)
input - convert to str(input)
if number_of_case none use random.rand or numpy random to generate number between 50-100
OR - use the tuplie (50,100).[random.randint(0,1)]

input string will be converted to a list [] using .stip(" ")
because with list we can run nested loop to a letter in word if needed

using the number_of_case we range, however idk if range is memory efficient or there are something else i can use here
then the logic starts-

this is a tricky part because number_of_case can be n here

say 50 so we need say 25 normal test case == base input
the rest 25 say 5-10 ten contains typo
rest 10 contain swap case how are you doing to are how you doing, etc..
adn the 5 with no space

BUT if it is 100 then lets say we decide on half of case will always be normal case and rest will have some errors

the problem number 
1. how we deciding if 5 will have typo or 10 will have typo because input can be n number because i can use deterministic value here for example like is said 50 or 100 half case will be normal
2. i can decide that out of 50 left in 100 cases 10 will have typo 10 will have nospce 10 will have swap but as soon as number_of_case is odd or given some else number by user how am i gonna handle that  
2. do i have number_of_case capped by user? but when i think say someone using my function but they want 1000 cases if i cap my function is useless to them
"""
 
"""
To answer distribution dilemma there is a simple approach

weighted probabilistic distribution

Instead of saying "I need 10 of these," you can let each iteration roll a weighted dice. For every case you generate in your loop, decide its mutation type based on a percentage probability:

    40% chance: Return the normal/base query.

    20% chance: Apply a typo.

    20% chance: Remove spaces.

    20% chance: Swap words.

so i look for random.choices and weighted random selection
"""

"""
okay so I learned few things first there are two random.choices one is 
the standard library random.choices
it doest not has to add up to 100% 
and you can use cum_weights if the probability is pre computed it slightly boost the performance and to not use both weights and cum_weights together
and there is value of k that it apply how many random selection we want i think its like swapping the probability randomly
second is numpy.random.choices
the probability has to add up to 1.0
it is more optimized for large arrays and data science
and there is replace =false to get sample without replacement idk what that means
and then one more there is numpy.random.default_rng
again the probability has to add up to 1.0
and you provide the size=10 maybe its similar that it will generated 10 random choices swapping the p
and lastly there is scipy but i heard its kind of slow idk why its slow and but it is more recommended for satisticaly anyalsis
"""
"""
but here k don't swap probabilities, it simply tells the function how many items yu want to pull out in one go

for k = 50 it rolls the weighted dice 50 times and returns a list of 50 choices
"""

"""
random.choice is i think a better choice for this wher numpy.random.choices will be overkill

I can make random.choices fast with cum_weights and  passing num_cases directly into the k parameter before loop starts


If you pass k=50000, random.choices creates a list of 50,000 small text labels (like ["normal", "typo", "normal", ...]).

While 50,000 items sounds big, a list of strings like that takes up less than 2 megabytes of RAM. However, if you feel uncomfortable pre-allocating a list upfront, you don't actually have to do it that way.

so, by using num_cases you make the decision inside the generator loop on ever step using a function call

"""

"""this solve the variable n input problem"""

"""
next is how do you decide where will be typo

actually that is you can just shove in a random letter or close proximity according to keyboard layout QWERTY to the word for example 
"what" in physical keyboard 'q and e' are closes to it so it could be qhat or ehat 

what about swapping words 

we could that randomly as well swap one word and put it randomly between the elements

and no space?

for that we choose two element position and and just perform nospace() to them randomly choose the two pos

"""


##observation

"""
one thing i found out that when using random.choices

say

word = "what are you doing"
result = random.choices(word)

1. it output single character
2. if your input contain 'space' it sometimes choose the space as well
3. the outputs always be a unhashable list so you gotta  ''.join(result) to get something out

so for the space you can pass the stripped input that is stripped of space 
"""


# typo function

"""
for my typo mistake i went with a manual written layout with 2d grid
the reason is to mock the human like error in QWERTY layout proximity and is very scallable

the method is simple
check for the row and column to target char that it

• abs(r1 - r2) <= 1: This means the other key can only be in the same row (difference of 0), the row right above (difference of 1), or the row right below (difference of 1). It cannot be 2 or more rows away.
• abs(c1 - c2) <= 1: This means the other key can only be in the same column (difference of 0), the column to the left (difference of 1), or the column to the right (difference of 1). It cannot be 2 or more columns away.

here char in normal can be chose random letter in word  in test case
and then simply replaced by its nearest neighbor

we can implement distance wieghting such as higher probability to horizontal neighbor since
finger slips sideways more often

and the other errors like "hitting both keys together sometimes 'wehat' or 'whaat' when typing fast

"""
"""
made some changes to typo 

to solve the weight problem we added weights.append(3)
the one that are in similar row will have more weights and rest will have 1

then later we can directly pass this to random.choices 

which is obv choose one from the horizontal key with more weights 

say 
y 
[t,u,h,g,j] weights = [3,3,1,1,1]

so the probability of getting t and u being chosen is higher

"""

 
## word_swap

"""
_wordswap(text)

.split the word using (" ")

then we loop over with enumerate

take the index with random.choices

since the index contains whole word swap to right or left if index to left is 0 always setup to right if right is empty always swap to left word

we can use maketrans here 

return " ".join(words)
"""

## nospace

"""
the idea of nospace is sometimes we forget to press space when speed typing
this module will mimic such edge case where input has nospace at some points

to achieve that we simply split the text to where space is now we have a list=
and then choosing the index random again we can either follow the step of word swap

where if index is 0 it perform strip with right side of index vice versa to the index [-1] and if the index is not at the edge it can  randomly choose left or right

here i thought that somehow we can get away without performing split but we don't do that the len becomes each char instead of each word

we have swap words

"""

