# reate a function that takes in a list of  `key` and list of `value` argument
# that returns a dictionary of key/value pairs.

# Write your function here.
def dictionary_pairs(keys, vals):
    return {key:val for key, val in zip(keys, vals)}

print(dictionary_pairs(["name", "age", "food"], ["James", 24, "steak"])) #> {'Name': 'James', 'Age': 24, 'Food': 'steak'}
print(dictionary_pairs(["name", "age", "food"], ["Vivian", 21, "sushi"])) #> {'Name': 'Vivian', 'Age': 21, 'Food': 'sushi'}
print(dictionary_pairs(["name", "age", "food"], ["Alex", 6, "chocolate"])) #> {'Name': 'Alex', 'Age': 6, 'Food': 'chocolate'}