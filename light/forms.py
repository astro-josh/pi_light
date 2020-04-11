from django import forms
from material import Layout, Row, Fieldset


class CommandForm(forms.Form):
    name = forms.TextInput()
    message = forms.CharField(widget=forms.Textarea)

    layout = Layout('message',)
                    # Row('password', 'password_confirm'),
                    # Fieldset('Personal details',
                    #          Row('first_name', 'last_name'),
                    #          'gender', 'receive_news', 'agree_toc'))

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass