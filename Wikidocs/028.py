lang = 'python'
#lang[0] = 'P' # This will throw error since string variable is immutable. You should use lang.replace('p', 'P') or make a new string variable and use upper().
print(lang)
new_lang = lang[0].upper() + lang[1:]
print(new_lang)