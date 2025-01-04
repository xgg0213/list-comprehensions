# Create a function that takes in a `string`. Using list comprehension, the
# function should return all of the vowels from the string.

# Write your function here.
def vowels(str):
    vowels=('a','e','i','o','u')
    return [x for x in str if x.lower() in vowels]

print(vowels("An amazing person")) #> ['A', 'a', 'a', 'i', 'e', 'o']
print(vowels("Coding is cool")) #> ['o', 'i', 'i', 'o', 'o']
print(vowels("People are NICE")) #> ['e', 'o', 'e', 'a', 'e', 'I', 'E']
