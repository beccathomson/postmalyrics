from django import forms

class LyricInputForm(forms.Form):
    lyric = forms.CharField(label='input_lyric', max_length=100)

    def get_lyric(self):
        return self.data['lyric']
