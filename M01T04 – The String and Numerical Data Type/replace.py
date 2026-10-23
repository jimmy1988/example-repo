#Declare a sentence
sentence = 'The!quick!brown!fox!jumps!over!the!lazy!dog.'

#Replace all the exclamation marks with a space and assign it to a new variable
sentence_replace = sentence.replace('!',' ')
print(sentence_replace) #outputs The quick brown fox jumps over the lazy dog.
print(sentence_replace.upper()) #outputs THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.

#Reverse the string from end of the string to start but in reverse order
#leaving the begin and the end indexes will start from the beginning and the end
#Having -1 as the step will mean it will go in reverse order

print(f"{sentence_replace[::-1]}") #outputs .god yzal eht revo spmuj xof nworb kciuq ehT
