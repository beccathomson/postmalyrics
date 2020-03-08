from django.shortcuts import render, redirect
from django import forms
from .forms import LyricInputForm
from datamuse import datamuse
import pandas as pd
import random

NUM_ROWS = 10

def index(request): 
    rhymes = ""
    nicki = ""
    kanye = ""
    mia = ""
    postie = ""
    placeholder = True

    if request.method == 'POST':
        form = LyricInputForm(request.POST)
        input_lyric = form.get_lyric()
        rhymes = get_rhymes(input_lyric)
        nicki = get_artist_lyrics("nicki_lyrics.csv", input_lyric, rhymes)
        kanye = get_artist_lyrics("kanye_lyrics.csv", input_lyric, rhymes)
        mia = get_artist_lyrics("mia_lyrics.csv", input_lyric, rhymes)
        postie = get_artist_lyrics("posty_lyrics.csv", input_lyric, rhymes)

    else:
        return render(request, 'index.html', {'placeholder':placeholder})
    
    return render(request, 'index.html', {'form':form, 'rhymes':rhymes, 'nicki':nicki, 'kanye':kanye, 'mia':mia, 'postie':postie})


def get_rhymes(input_lyric):
    # Get words that rhyme with input word
    api = datamuse.Datamuse()
    rhymes = api.words(rel_rhy=input_lyric, max=50)
    sorted_output = sorted(rhymes, key = lambda i: i['numSyllables'])
    rhymes = [x['word'] for x in sorted_output]
    return [word.replace('"', '') for word in rhymes]


def get_artist_lyrics(artist_file, input_lyric, rhymes):
    # Import main lyric table
    lyrics_tbl = pd.read_csv(artist_file)
    
    # Get table of rhyming lines (<= NUM_ROWS)
    rhyme_tbl = lyrics_tbl[lyrics_tbl["END_WORD"].isin(rhymes)]  # filter lyric table to only rhyming lines

    if (len(rhyme_tbl) < 1):
        rhyme_tbl = ""
    else:
        if (len(rhyme_tbl) > NUM_ROWS):
            new_tbl = pd.DataFrame(columns = ["LINE", "END_WORD"])
            for i in range (0, NUM_ROWS):
                rand = random.sample(range(len(rhyme_tbl)), NUM_ROWS)
                new_tbl.append(rhyme_tbl.iloc[rand])
            # rhyme_tbl = new_tbl
        rhyme_tbl = rhyme_tbl["LINE"] # take only the column with desired lyric
    
    return rhyme_tbl