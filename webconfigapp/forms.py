from django import forms

class ShowCommandForm(forms.Form):
      send_command = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Enter command to run on device',
                'id':'send_command',
                'class': 'form-control',
                'aria-label': "Enter show command",
                'aria-describedby': 'button-addon2'
            }
        )
    )