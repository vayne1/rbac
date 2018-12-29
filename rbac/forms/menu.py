from django import forms
from rbac import models
from django.utils.safestring import mark_safe
from rbac.forms.base import FormControlModelFrom

class MenuModelForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        fields = ['title','icon']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'icon':forms.RadioSelect(
                choices=[
                    ['fa-edit',mark_safe('<i class="fa fa-edit" aria-hidden="true"></i>')],
                    ['fa-check-circle',mark_safe('<i class="fa fa-check-circle" aria-hidden="true"></i>')],
                    ['fa-check-square',mark_safe('<i class="fa fa-check-square" aria-hidden="true"></i>')],
                    ['fa-cloud-download',mark_safe('<i class="fa fa-cloud-download" aria-hidden="true"></i>')],
                    ['fa-flag',mark_safe('<i class="fa fa-flag" aria-hidden="true"></i>')],
                    ['fa-frown-o',mark_safe('<i class="fa fa-frown-o" aria-hidden="true"></i>')],
                    ['fa-key',mark_safe('<i class="fa fa-key" aria-hidden="true"></i>')],
                    ['fa-info-circle',mark_safe('<i class="fa fa-info-circle" aria-hidden="true"></i>')],
                    ['fa-male',mark_safe('<i class="fa fa-male" aria-hidden="true"></i>')],
                    ['fa-mobile',mark_safe('<i class="fa fa-mobile" aria-hidden="true"></i>')],
                    ['fa-mouse-pointer',mark_safe('<i class="fa fa-mouse-pointer" aria-hidden="true"></i>')],
                    ['fa-soccer-ball-o',mark_safe('<i class="fa fa-soccer-ball-o" aria-hidden="true"></i>')],
                    ['fa-tv',mark_safe('<i class="fa fa-tv" aria-hidden="true"></i>')],
                    ['fa-user-circle',mark_safe('<i class="fa fa-user-circle" aria-hidden="true"></i>')],
                    ['fa-plus',mark_safe('<i class="fa fa-plus" aria-hidden="true"></i>')],
                    ['fa-folder-open-o',mark_safe('<i class="fa fa-folder-open-o" aria-hidden="true"></i>')],
                    ['fa-cloud-download',mark_safe('<i class="fa fa-cloud-download" aria-hidden="true"></i>')],
                    ['fa-commenting',mark_safe('<i class="fa fa-commenting" aria-hidden="true"></i>')],
                    ['fa-cube',mark_safe('<i class="fa fa-cube" aria-hidden="true"></i>')],
                    ['fa-hand-pointer-o',mark_safe('<i class="fa fa-hand-pointer-o" aria-hidden="true"></i>')],
                    ['fa-map-o',mark_safe('<i class="fa fa-map-o" aria-hidden="true"></i>')],
                    ['fa-map-marker',mark_safe('<i class="fa fa-map-marker" aria-hidden="true"></i>')],
                    ['fa-phone',mark_safe('<i class="fa fa-phone" aria-hidden="true"></i>')],
                    ['fa-power-off',mark_safe('<i class="fa fa-power-off" aria-hidden="true"></i>')],
                ],
                attrs={'class':'clearfix'}
            )
        }

class SecondMenuModelForm(FormControlModelFrom):
    class Meta:
        model = models.Permission
        exclude = ['pid']


class PermissionMenuModelForm(FormControlModelFrom):
    class Meta:
        model = models.Permission
        fields = ['title','name','url']


class MultiAddPermissionForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')


class MultiEditPermissionForm(forms.Form):
    id = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,

    )

    pid_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(attrs={'class': "form-control"}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['pid_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('id', 'title')