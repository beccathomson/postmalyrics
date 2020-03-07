from django.shortcuts import render, redirect
from django import forms
from .forms import LyricInputForm

# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})

def search_lyrics(request):
    print("HELP ME")
    form = LyricInputForm(request.POST or None)
    if request.method == 'POST':
        form = LyricInputForm(request.POST or None)
        input_lyric = form.cleaned_data.get("inputLyric")
        print("GOT A LYRIC"+input_lyric)
        return render(input_lyric)
        # return redirect('search')
    else:
        return render(request, 'hello_world.html', {'form': form})    