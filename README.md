# 👩🏾‍💻 Advent Of Code 2023

Main goals:
- To learn how to break down problems into it's moving parts
- To identify clear edge cases and handle them before testing the code on the input data
- To use test-driven development to handle the edge cases against the given sample input

Going to document my thought process here, considering different algorithmic approaches.

**Language**: Python.

## Daily notes:

[Day 1: Trebuchet?! (String Manipulations)](#day-1) 
<!-- [Day 2: Cube Conundrum](#day-2) \ -->
<!-- [Day 3: ...](#day-3) \
[Day 4: ...](#day-4)  -->

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

I'll see if I can return the runtime of both approaches.

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



<!-- # Day 2

# Day 3

# Day 4 -->
