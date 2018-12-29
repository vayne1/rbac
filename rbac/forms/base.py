from django import forms


class FormControlModelFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormControlModelFrom,self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'