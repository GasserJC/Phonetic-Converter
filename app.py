import eng_to_ipa as ipa
import numpy as np
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
import ipalhabet
from ipalhabet import ALPHABET

LENGTH = 75

def FeatureOptimize( phrase ):
    #Cut Phrase to a length of 100
    phrase = phrase[0:LENGTH].lower()
    phrase = phrase.zfill(LENGTH)
    #convert to ascii values, then change to numpy array
    num_phrase = []
    for char in phrase:
        char = ord(char) - 96
        if(char < 0):
            char = 1
        num_phrase.append(char)
    num_phrase = np.array(num_phrase)
    num_phrase = to_categorical(num_phrase, 27)

    #num_phrase = (np.arange(107) == num_phrase[...,None]).astype(int)
    #Zero Fill from the front
    #num_phrase = num_phrase.zfill(100)

    #There are 107 IPA characters

    #Return Feature Optimized Phrase
    return num_phrase

def OneHotEncode( numerated_phrase ): #do differently
    # define universe of possible input values
    # define a mapping of chars to integers
    char_to_int = dict((c, i) for i, c in enumerate(alphabet))
    int_to_char = dict((i, c) for i, c in enumerate(alphabet))

    # integer encode input data
    integer_encoded = [char_to_int[char] for char in numerated_phrase]
    print(integer_encoded)
    # one hot encode
    onehot_encoded = list()
    for value in integer_encoded:
	    letter = [0 for _ in range(len(alphabet))]
	    letter[value] = 1
	    onehot_encoded.append(letter)
    

phrase = "i make elavting music you make elevator music"
print(phrase)
print("Feature Optimize . . .")
phrase = FeatureOptimize(phrase)
print(str(len(phrase)) + " by " + str(len(phrase[0])))
print(phrase)
