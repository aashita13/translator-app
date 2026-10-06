from django import forms


class TranslationForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter text to translate...',
                'rows': 6,
                'class': 'text-input',
            }
        ),
        label='Text to translate'
    )

    source_language = forms.ChoiceField(
        choices=[
            ('en', 'English'),
            ('hi', 'Hindi'),
            ('fr', 'French'),
            ('es', 'Spanish'),
            ('de', 'German'),
            ('it', 'Italian'),
            ('ja', 'Japanese'),
            ('ko', 'Korean'),
            ('zh-cn', 'Chinese'),
        ],
        label='From'
    )

    target_language = forms.ChoiceField(
        choices=[
            ('hi', 'Hindi'),
            ('en', 'English'),
            ('fr', 'French'),
            ('es', 'Spanish'),
            ('de', 'German'),
            ('it', 'Italian'),
            ('ja', 'Japanese'),
            ('ko', 'Korean'),
            ('zh-cn', 'Chinese'),
        ],
        label='To'
    )