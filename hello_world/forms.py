from django import forms

class LyricInputForm(forms.ModelForm):
    lyric = forms.CharField(label='input_lyric', max_length=100)

    def __init__(self, *args, **kargs):
        super(LyricInputForm, self).__init__(*args, **kargs)