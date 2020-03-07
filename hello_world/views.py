from django.shortcuts import render, redirect
from django import forms
from .forms import LyricInputForm
from datamuse import datamuse

def index(request): # initial load
    output = ""

    if request.method == 'POST':
        form = LyricInputForm(request.POST)
        input_lyric = form.get_lyric()
        print("GOT A LYRIC:  "+input_lyric)
        api = datamuse.Datamuse()
        output = api.words(rel_rhy=input_lyric, max=7)
    else:
        form = LyricInputForm(None)
    
    return render(request, 'index.html', {'form':form, 'output':output})


# def search_lyrics(request):
#     # output =""
#     form = LyricInputForm(request.POST or None)
#     if request.method == 'POST':
#         output = ""
#         form = LyricInputForm(request.POST or None)
#         input_lyric = form.get_lyric()
#         print("GOT A LYRIC:  "+input_lyric)
#         api = datamuse.Datamuse()
#         output = api.words(rel_rhy=input_lyric, max=7)
#         # need to render the results now...
#         return render(request, 'index.html', {'form': form})  
#     else:
#         return render(request, 'index.html', {'form': form})

