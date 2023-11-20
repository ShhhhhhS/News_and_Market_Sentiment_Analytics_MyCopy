# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 20:23:57 2023

@author: chris
"""

# %% Libraries
import nltk
import spacy
from nltk.corpus import reuters
import pandas as pd
from collections import Counter

# %%  Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# %% Retuers data
# Extract 10 financial news headlines from the NLTK Reuters corpus
categories = ['money-fx', 'trade', 'grain', 'crude', 'interest']
reuters_texts = [reuters.raw(file_id) for file_id in reuters.fileids(categories=categories)[0:10]]

noun_phrases_list = []
verb_phrases_list = []
named_entities_list = []
organiations_list = []
geography_list = []

for idx, reuters_i in enumerate(reuters_texts, 1):
    # Process the news headline with spaCy
    doc = nlp(reuters_i)

    # Extract Noun Phrases (NP) and Verb Phrases (VP) using spaCy's dependency parsing
    noun_phrases    = [chunk.text for chunk in doc.noun_chunks]
    verb_phrases    = [token.text for token in doc if token.pos_ == 'VERB']
    named_entities  = [(ent.text, ent.label_) for ent in doc.ents]
    organiations    = [org[0] for org in named_entities if org[1]=="ORG"]
    geography       = [gpe[0] for gpe in named_entities if gpe[1]=="GPE"]
    
    # Count the occurrences of each word
    noun_phrases    = sorted(Counter(noun_phrases).items(), key=lambda x: x[1], reverse=True)
    verb_phrases    = sorted(Counter(verb_phrases).items(), key=lambda x: x[1], reverse=True)
    named_entities  = sorted(Counter(named_entities).items(), key=lambda x: x[1], reverse=True)
    organiations    = sorted(Counter(organiations).items(), key=lambda x: x[1], reverse=True)
    geography       = sorted(Counter(geography).items(), key=lambda x: x[1], reverse=True)
    
    # Store result
    noun_phrases_list.append(noun_phrases)
    verb_phrases_list.append(verb_phrases)
    named_entities_list.append(named_entities)
    organiations_list.append(organiations)
    geography_list.append(geography)

# %% Check results
i = 0

print(noun_phrases_list[i][0:10])
print(verb_phrases_list[i][0:10])
print(organiations_list[i][0:10])
print(geography_list[i][0:10])

# Does it make sense?
print(reuters_texts[i])

