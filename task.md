# Instructions

## 💪 This is a difficult challenge! 💪

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number.

For Love Scores **less than 10** or **greater than 90**, the message should be:

_"Your score is *x*, you go together like coke and mentos."_

For Love Scores **between 40 and 50**, the message should be:

_"Your score is *y*, you are alright together."_

Otherwise, the message will just be their score. e.g.:

_"Your score is *z*."_

## These functions will help you:

[lower()](https://www.w3schools.com/python/ref_string_lower.asp)
[count()](https://www.w3schools.com/python/ref_list_count.asp)

## Example Input 1
```
Kanye West
Kim Kardashian
```
## Example Output 1
```
The Love Calculator is calculating your score...
Your score is 42, you are alright together.
```
## Example Input 2
```
Brad Pitt
Jennifer Aniston
```
## Example Output 2
```
The Love Calculator is calculating your score...
Your score is 73.
```