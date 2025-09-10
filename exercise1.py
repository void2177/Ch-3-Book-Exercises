##Exercise 1
##Output:
## def repeat(text: str, times: int):
   ## for _ in range(times):
      ##  print(text)
## New code, but without "for"
## def repeat(text: str, times: int):
    ## print((text + "\n") * times, end="")
## Tested function from AI:
## def bright_side():
    ## print("Always look on the bright side of life.")
   ##  print("Always look on the bright side of life.")
## Asked again, got what I wanted
## def bright_side():
    ## first_half = "Always look on the"
    ## second_half = " bright side of life."
    ## phrase = first_half + second_half
   ##  print(phrase)
   ##  print(phrase)

   ## Asked AI whats wrong with this code
## def print_twice(string):
   ## print(cat)
   ## print(cat)
#AI said that the function is trying to take a parameter, string, but cat is not defined anywhere.
##Use string for the print twice, then use the function with the word in your parentheses
def print_twice(string):
    print(string)
    print(string)
print_twice("cat")