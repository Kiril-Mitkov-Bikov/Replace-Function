from dirty_words_function import replace_dirty_words

# Test with only one lower case dirty word
print(replace_dirty_words("I am a fucking genius and I don't give a fuck.", ['fuck']))

# Test with two lower case dirty words
print(replace_dirty_words("I am a fucking genius and I don't give a fuck. I am better than all of you, bastards.",
                          ['fuck', 'bastard']))

# Test with dirty word that has one upper case letter
print(replace_dirty_words("I am a fucking genius and I don't give a Fuck. I am better than all of you, bastards.",
                          ['fuck', 'bastard']))

# Test with upper cae dirty word
print(replace_dirty_words("I am a fucking genius and I don't give a FUCK. I am better than all of you, bastards.",
                          ['fuck', 'bastard']))

# Test with a word in brackets
print(replace_dirty_words("I am a fucking genius and I don't give a (FUCK). I am better than all of you, bastards.",
                          ['fuck', 'bastard']))

# Test with a word ending with ellipsis
print(replace_dirty_words("I am a fucking genius and I don't give a (FUCK). I am better than all of you, bastards...",
                          ['fuck', 'bastard']))
