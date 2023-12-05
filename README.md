# 👩🏾‍💻 Advent Of Code 2023

Main goals:
- To learn how to break down problems into it's moving parts
- To come up with algorithm approaches giving pros and cons of each one
- To identify clear edge cases and handle them before testing the code on the input data

I'm going to document my thought process here, considering different algorithmic approaches.

**Language**: Python.

## Use of AI
AI tools such as GPT are used strategically to help guide me on some parts of the AoC, more specifically parsing. Parsing inputs can be a pain, and they aren't directly relevant to building good problem solving skills. Of course, being good at parsing helps a lot, but I don't want to spend too much time on that for this year.

For each day I think of the algorithmic approaches without consulting any AI tools. I want to understand how the algorithm would work at a more abstract level as I believe this is more useful than the final code written. The ability to solve coding problems is two-fold: coming up with a useful algorithm, as well as writing code that implements that algorithm well. The former builds up the latter.

## Daily notes:

[Day 1: Trebuchet?! (String Manipulations)](#day-1) \
[Day 2: Cube Conundrum (String Manipulations + Parsing)](#day-2) \
[Day 3: Gear Ratios](#day-3) 
<!-- [Day 4: ...](#day-4)   -->

# Day 1
The goal is to find the specific calibration value for each line in the input. 

The calibration value can be calculated by pairing the *first* and *last* digit in a given line to form a 2-digit value. 

E.g.

```
1abc2 -> 1 and 2 -> 12
```

In this example, the digits are indeed the 1st and last elements in the line. But that assumption may not hold for every line.

E.g.

```
treb7uchet -> 7 and 7 -> 77
```
7 is the first AND last digit in the line, so therefore it is used for both digits in the 2-digit value. 

For each 2-digit value per line, we want to sum them up to get the final output.

Potential edge cases to consider:
- Does the line even have an integer? (it's not explicitly said that every line WILL have an integer)
- The line only has 1 digit (see above)
- The line has multiple digits (make sure that only the first and last integer are used)
- The order of the digits found matters (12 != 21)

## Algorithmic approach
As I look at the problem, this is the first approach that comes to mind.

1. Iterate through each line in the file
2. Convert each line into a list of chars
3. Remove all chars that are non-numeric
4. Return the first and last element of the list
5. Pair them together to form the 2-digit value
6. Add to a variable called total

#### Pros:
- It's fairly intuitive and easy to understand approach. 
- Due to that, it would be very easy to code in a short time frame.
- It can handle the edge cases too with simple error-checking

#### Cons:
- The time complexity is high: Iterating over the file per line makes it O(n), not even including the iteration needed per line and for the list conversion.
- High space complexity too: Creating a list for each line in the file would be a space complexity of O(n * m), where n is the number of lines and m is the length of the longest line.

Is there a way we can find a more optimal solution?

### Set theory

Suppose you define a set of all numeric values 0-9 (because sets must be of the same type, let's assume this numeric set is in chars). 

You could reduce the time complexity by converting each line in the file into a set, and performing intersection against the numeric set. 

E.g.

```
1abc2 -> ('1', 'a', 'b', 'c', '2')

print(('1', 'a', 'b', 'c', '2').intersection(numeric_set))

>>> ('1', '2') or ('2', '1')
```

Whilst this method does return the correct digits (for this specific example), we can't create the 2-digit value. 

Sets don't have order, so we can't determine which of these values is the first or last digit. Set theory wouldn't work to solve this problem at all.

### Pointers

Perhaps we don't need to even think about dropping all non-numeric values at all. Suppose we have each line in it's string format.

E.g.

```
mystr = "pqr3stu8vwx"
```

Let's assign a pointer (or rather, counter in the cases of python) to the top of the string, and the bottom of the string. Let's call these **head** and **tail**

```
head = 0
tail = len(mystr) - 1         # 10
```
We want to find the first and last digit in a string. So instead of iterating the whole list, we can iterate against head and tail, and adjust the pointers as needed.

```
if mystr[head].isdigit() and mystr[tail].isdigit():
    # both first and last digit have been found
    # combine them, and return the 2 digit value
    value = mystr[head] + mystr[tail]
    return value
else:
    if mystr[head].isdigit():
        # keep head pointer as it is
        # we have found the first digit
        # tail isn't a digit so we decrement that pointer by 1
        tail -= 1
    elif mystr[tail].isdigit():
        # keep tail pointer as it is
        # we have found the last digit
        # head isn't a digit, increment head by 1
        head += 1
```

With this, the program only has to move the pointer if it's not an int. Which means we don't waste time iterating through the whole list.

**Does this method handle all edge cases?**

Let's go back to the edge case of "there's only 1 digit in the line". With the pointer method, it's going to end up spending time changing the pointer of either head or tail to match. Whilst the method will still return the correct output, perhaps we can optimize that specific part.

We could create a list comprehension function to count how many digits there are in the string. This could help with those edge cases, by allowing the code to use an **or** gate instead of an **and**. 

Though it made add to the time complexity, the trade-off may be worth it in the end. 

<!-- I'll see if I can return the runtime of both approaches. -->

## Code - Part 1

The solution above looks like the following. Print debugging is present here.

```
def solve_day1_part1(input_data):
    lines = read_input_string(input_data)

    print(lines)
    
    result_part1 = 0

    for line in lines:
        head = 0
        tail = len(line) - 1

        while head < tail:
            print(line[head], line[tail])
            if line[head].isdigit() and line[tail].isdigit():
                break
            else:
                # print('something')
                if not line[head].isdigit():
                    print('head isnt a digit')
                    head += 1
                
                if not line[tail].isdigit():
                    print('tail isnt a digit')
                    tail -= 1

        value = line[head] + line[tail]
        print(value)
        result_part1 += int(value)

    return result_part1
```

Testing this on the sample input and output, gives the correct output. Though it's interesting to see that there was an additional loop on a lines where there's only 1 digit.

```
# treb7uchet

7 u
tail isnt a digit
77

```

Here, the digit has already been found, but because the code above doesn't have the edge case handling for 1 digit, it assumes that there must be a 2nd digit. Which gives us our correct output, but this may prove to increase runtime of the code.

In the end we are able to solve part 1 with this code. Though there's a high chance that this would need to change for part 2.

## Part 2 - What's changed?
Instead of dealing merely with integers, we now have to consider if the line in the input has the numbers in word format.

E.g.

```
two1nine -> two and nine -> 2 9 -> 29
```

Let's see how we can aproach this differently.

### Pattern recognition

Strings in python have a replace function, which is quite helpful. We could use this to replace all string formats of numbers into numerical, meaning that we don't have to change up our implementation too much.

With a dictionary like the following:

```
numsAsWords = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
```

We can replace occurences of those words in the string, with the following:

```
 for key, value in numsAsWords.items():
    line = line.replace(key, value)
```

### Problem

The example below shows that this conversion falls short:

```
eightwothree
eigh23     # this should be 8wo3!
23         
```

This is happening because the code is merely iterating against all keys, instead of iterating against the keys that show up in the right order of the string.

Here's a way to solve this:
- The longest digits in word form has 5 characters (three, seven, eight). 
- The next longest digits are 4 characters (four, five, nine).
- The remaining 3 are 3 characters long (one, two, six).

Perhaps this dictionary should be ordered such that longer digits are checked before shorter ones, to avoid letters in shorter digits being picked up beforehand.

```
numsAsWords = {
        'eight': '8',
        'three': '3',
        'seven': '7',
        'four': '4',
        'five': '5',
        'nine': '9',
        'one': '1',
        'two': '2',
        'six': '6', 
    }

```

This doesn't work, as we still fall into situations like this:

```
zoneight234
zon8234       # should be z1ight234
84         
```

Another approach, using the character system above:
- Take the first 5 characters of a string
- If a number in word form is present in it, replace it.
- Find the next 5 characters.

Let's split up the numAsWords list into 3 separate lists:

```
    longDigits = {
        'eight': '8',
        'three': '3',
        'seven': '7',
    }

    midDigits = {
        'four': '4',
        'five': '5',
        'nine': '9',
    }

    shortDigits = {
        'one': '1',
        'two': '2',
        'six': '6', 
    }
```

For each dict, starting with the long digits we can check if the key is present in the segment, and then replace it.

This gives us the correct answer with the sample input, but our answer is still incorrect with the final input.

Correction to the above. Turns out the following should be the case:

`oneight` should convert to 18. 

To fix this, I'll change the replace function to check the char just after the number replacement. A little bit hacky, but given as chars aren't read into the final sum it doesn't really matter.

This does work, and gives us the correct answer for part 2!

### Conclusions
It was a nice problem, I like that you had to be careful with using str.replace or Regex (as other people used). It forced you to think, which is good. For a 1st day, it's probably on the slightly harder end, but all in all, a fun problem to do. 

Documenting my thought process was helpful too, cause even though this took much longer than solving it, I have these notes to look back on. It also helps me see my thought process (though I probably could have explained some areas better). So I'll try to continue to do these notes where I can.

# Day 2
The goal is to determine which games would be possible, with the following number of cubes: ``12 red cubes, 13 green cubes, and 14 blue cubes.``

Each game has a certain number of rounds, where the Elf brings out some of the cubes in the bag, and counts the number of each occurence. The cubes are returned back into the bag after each round.

Rounds are separated by semi-colons. 

E.g.

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
```

With this game, it's possible that it would fit the number of cubes stated above. 

It's important to note, that you can't simply sum up the totals of the cubes in all rounds. As the cubes are returned after each one, the same cube could be picked up in future rounds.

To check that a game is possible with the above configuration, it's a matter of checking whether any round exceeds the configuration. 

At least that's what I can see at first glance.

Though I imagine there will be an annoying edge case somewhere that I'll discover.

The output is the sum of the game IDs where the game is possible with the above configuration.

## Algorithmic approach
I feel like python dictionaries are a good option to store the data. A dictionary for each round would work, with if statements to check if numbers exceed the configuration.

Here's what I'm thinking:
1. Iterate through each line in the file
2. Seperate each line with spaces
3. Extract the game ID
4. Create a list of dictionaries, where each dictionary is 1 round in a game.
5. Extract number of cubes and cube colour and store into the dictionary
6. For the cubes in each round, check if the colour ends in `;`, if it does, that's the end of a round. 
7. Check if that dictionary exceeds the configuration, if it does, stop the checking and add the game ID to a `total` variable.

Fairly straightforward approach. Slightly space intensive, but it should hopefully work.

## Code

The approach I took was to separate each input line by space. Which made sense in my head, but I soon realised that it made
parsing the inputs, very hard. 

I kept on creating dictionaries to try and store each game, but I didn't realise that if `2 green` appears twice in a game, it would get replaced completely (as dictionary keys must be unique).

So the dictionary approach, was completely wrong in this instance.

I was spending a lot of time just trying to get the inputs into a way that would make sense.

I decided to consult GPT to see how it would approach the parsing element of this problem.

```
## modified code based on what GPT gave me
for round in input_str.split(";"):
    print('round: ' + round)
    selections = round.split(",")
    print(selections)

    for selection in selections:
        print(selection)
        selection = selection.strip().split()
        print(selection)

# OUTPUT
round:  3 blue, 4 red       # current round
[' 3 blue', ' 4 red']       # current round into list
 3 blue                     # number and colour selection
['3', 'blue']               # separate colour and number
 4 red
['4', 'red']
```
Seeing that it first split the line by semi-colon, then by comma, made a lot more sense. This output makes it a lot easier to solve part 1. 

## Problems encountered

I fell into more parsing problems, trying to extract the Game ID from the string. It's easy to write something like:

`gameId = input_str[5]`

For single digit IDs. Once you get to double digits, the code would break.

After looking at the input data myself, I realised that game ID increments anyways, so I could just increment a counter and use that as the ID.

That meant that I could send the string that has the `Game XX:` element removed, making it easier for the algorithm to behave.

With that, part 1 is complete!

## Part 2 - what's changed?

Now the question has changed: What is the **fewest number of cubes** of each color that could have been in the bag to make the game possible?

The final output needs to be the power of a set of cubes (the number of cubes multiplied together), summed up.

This part 2 at a glance seems a lot easier than part 1. I imagine it's simply a matter of storing the highest number that someone rolls in a given round, for each colour. Then replacing it if the number increases.

This is where a dictionary can be helpful, as you can easily override and store the colour number pairs.

By changing the if statement to update the dictionary with the highest value, this solved part 2 quite effectively.

## Conclusions and lessons
From part 1, main lesson I'm learning is to actually look and study the input data. See what you notice and use that to help guide how you process the input.

It's also good to try parsing inputs in different ways, to see what output you get. Parsing by space made the problem really hard to solve, whereas dealing with each line as a string and using lists, was much easier.

Breaking it down to work on creating a function that works for 1 line, is good. It worked quite well for day 2, and I think that would be really useful going forward, where possible.

It's good to challenge and see where edge cases may occur. Note them down and see how you could approach them.

I've not really been using TDD that much for these challenges, as I feel simply documenting my thought process is effective for the early days. For future ones, I'll consider using TDD.

# Day 3
The goal of this challenge is to check whether a number is adjacent to a special character, in a 2D space.

E.g.

```
467..114..
...*......
..35..633.
......#...
617*......
```

In this section, `467, 35, 633` and  `617` are adjacent to a special character (anything that isn't a period or a number).

I've generally found 2D problems to be quite hard, I always end up with some complicated situation. I'm going to try and see if I can come up with a more optimal solution this time round.

## Algorithmic approach
2D arrays seem to be the best call for problems like this. 

1. Convert input into a 2D array, char separated
2. Iterate through the 2D array
3. If a special character is detected, check all neighbouring characters for a number
4. If a number is found, find out where the full number is (by checking just before and just after it) then add to the total
5. Change the chars where the number is to dots, so that they aren't picked up again (in case the number is next to another special character: edge case!)

Seems like a simple approach. 

I think I'll code a separate function to handle the surrounding character checking, and call it when a special character is detected. 

It could return the indexes where numbers are present, and then the main algorithm can determine where the number starts and ends.

It's input could be the surrounding array, like so:

```
| 7 . . |
| . * . |
| 3 5 . |
```

And it's output could show where the numbers are in relation to the main point. Like so:

```
[-1,-1]
[1, -1]
[0, 1]
```

To explain this better, we use vector logic from the central point. The reason it's written slightly backwards, is because array rows increase downwards rather than upwards.

```
| [-1,-1] [0,-1] [0,1] |
| [0,-1]  [0,0]  [0,1] |
| [1,-1]  [0,1]  [1,1] |
```

Using this reference, we can return the points and take them away from the actual central point to find their actual location in the big array.

It means that the function dealing with surrounding items, doesn't need the full array to function. This is a good example of abstraction, not giving functions more info than they need.

## Code









<!-- 
# Day 4 -->
