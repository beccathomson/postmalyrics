from django.shortcuts import render, redirect
from django import forms
from .forms import LyricInputForm
from datamuse import datamuse
import pandas as pd

def index(request): 
    output = ""

    if request.method == 'POST':
        form = LyricInputForm(request.POST)
        input_lyric = form.get_lyric()
        output = get_output(input_lyric)
    else:
        form = LyricInputForm(None) # initial load
    
    return render(request, 'index.html', {'form':form, 'output':output})


def get_output(input_lyric):

    # Get words that rhyme with input word
    api = datamuse.Datamuse()
    output = api.words(rel_rhy=input_lyric, max=50)
    sorted_output = sorted(output, key = lambda i: i['numSyllables'])
    final_output = [x['word'] for x in sorted_output]

    # Import main lyric table
    lyrics_tbl = pd.read_csv("kanye_lyrics.csv")
    


    return final_output