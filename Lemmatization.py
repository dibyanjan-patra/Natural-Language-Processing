# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:02:31 2020

@author: dibya
"""
import nltk
from nltk.stem import WordNetLemmatizer #used for lemmatization
from nltk.corpus import stopwords

paragraph = """Greetings to fellow citizens, for over four months the global community has been in the fight against Corona virus.
During this period more than 42 lakh people across the world have been infected with Corona. More than 2.75 Lakh people 
have died tragically. In India too, people have lost their near and dear ones.I express my heartfelt condolences to all.
Friends, a virus has destroyed the world. Crores of people around the world are facing a crisis. World all over is 
engaged in a battle to save precious lives. We have never seen or heard of such a crisis.This crisis is unthinkable 
as well as unprecedented for mankind.However-getting exasperated, losing heart or getting shattered, is not acceptable to
the mankind. We have to remain vigilant, closely monitor it, follow the rules of engagement in such a war, save ourselves 
and move ahead.Today, when the world is in crisis, we must strengthen our resolve. Our great resolve will help overcome this crisis.
Friends, we have been hearing since the last century that the 21st century belongs to India. We have seen how the world was before
Corona and the global systems in detail. Even after the infliction of the Corona crisis, we are constantly watching the situation as 
it unfolds across the globe. When we look at these two periods from India's perspective, it seems that the 21st century is the century
for India. This is not our dream, rather a responsibility for all of us.But what should be its trajectory?The state of the world today
teaches us that a (AtmaNirbhar Bharat) "Self-reliant India" is the only path .It is said in our scriptures - EshahPanthahThat is - self-sufficient India.
As a nation today we stand at a very crucial juncture. Such a big disaster is a signal for India,it has brought a message and an opportunity.
I will share my perspective with an example. When the Corona crisis started, there was not a single PPE kit made in India. 
The N-95 masks were produced in small quantity in India. Today we are in a situation to produce 2 lakh PPE and 2 lakh N-95 masks daily. 
We were able to do this because India turned this crisis into an opportunity.This vision of India - turning crisis into opportunity- is going
to prove equally effective for our resolve of self-reliant India.Today the meaning of the word self-reliance has changed in the global scenario.
The debate on Human Centric Globalization versus Economy Centralized Globalization is on. India's fundamental thinking provides a ray of hope to world.
The culture and tradition of India speaks of self-reliance and the soul is VasudhaivaKutumbakam.India does not advocate self-centric arrangements 
when it comes to self-reliance. India's self-reliance is ingrained in the happiness, cooperation and peace of the world.This is the culture which 
believes in the welfare of the world, for all the living creatures and the one which considers the whole world as a family. India's goals and 
actions impact the global welfare. When India is free from open defecation,it has an impact on the image of the world. Be it TB, malnutrition, 
polio, India's campaigns have influenced the world.International Solar Alliance is India's gift against Global Warming. The initiative of International
Yoga Day is India's gift to relieve stress. Indian medicines have given a fresh lease of life to the people in different parts of the world.These steps
have brought laurels for India and it makes every Indian feel proud. The world is beginning to believe that India can do very well, so much good for 
the welfare of mankind can give."""

#Tokenizing to sentences
sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

#Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])   #converting to words for every input sentence
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))] #set helps in taking unique stop words in english
    sentences[i] = ' '.join(words)