from django import forms

class LyricInputForm(forms.ModelForm):
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)

    def __init__(self, *args, **kargs):
        super(LyricInputForm, self).__init__(*args, **kargs)

    class Meta:
        model = User
        fields = '__all__'