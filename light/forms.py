from . import demo as forms
from django.template import Template
from material import Layout, Row, Fieldset
from colorful.widgets import ColorFieldWidget

PATTERN_CHOICES = [
    (0, "Solid Color"),
    (1, "Blink"),
    (2, "Pulse"),
    (3, "Sequence"),
    (4, "Rainbow"),
    (5, "Rainbow Fade"),
    (6, "RGB Bounce"),
]


class CommandForm(forms.Form):
    pattern = forms.ChoiceField(choices=PATTERN_CHOICES, initial="Solid Color")
    colors = forms.CharField(widget=ColorFieldWidget)
    iterations = forms.IntegerField(widget=forms.NumberInput, min_value=1, max_value=5)

    layout = Layout('pattern',
                    Row('colors', 'iterations'),)
                    # Fieldset('Personal details',
                    #          Row('first_name', 'last_name'),
                    #          'gender', 'receive_news', 'agree_toc'))

    template = Template("""
    {% form %}
        {% part form.pattern prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.colors prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.iterations prefix %}<i class="material-icons prefix">lock_open</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-light btn" type="submit">Submit</button>
    """)

    title = "Registration form"