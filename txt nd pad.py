# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 12:13:02 2020

@author: dibya
"""
####  Using Api's #################
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'i Love my dog',
    'i love my cat'
    ]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)
########################## End ###################################\

#### Text to sequences  ###########
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'i Love my dog',
    'i love my cat',
    'You love my dog',
    'Do you think my dog is awesome'
    ]

tokenizer = Tokenizer(num_words = 100)
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

seq = tokenizer.texts_to_sequences(sentences)
print(seq)
  ##############################
#### Padding ##########
from tensorflow.keras.preprocessing.sequence import pad_sequences
sentences = [
    'i Love my dog',
    'i love my cat',
    'You love my dog',
    'Do you think my dog is awesome'
    ]

tokenizer = Tokenizer(num_words = 100, oov_token= "<oov>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

seq = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(seq)
#or
paded2 = pad_sequences(seq, padding='post')
print(paded2)
