#Excercise 4/Chapter6
def counter(word,let):
  count = 0
  for letter in word:
    if letter == let: 
      count = count + 1
  return count

word = "banana"
let = "a"
print (f'{let} occured {counter(word,let)} times in {word}')