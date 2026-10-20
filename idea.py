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
 



 