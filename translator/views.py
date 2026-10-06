from django.shortcuts import render
from googletrans import Translator
from asgiref.sync import async_to_sync
from .forms import TranslationForm


def translate_text(request):
    translated_text = ""

    if request.method == "POST":
        form = TranslationForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data["text"]
            source_language = form.cleaned_data["source_language"]
            target_language = form.cleaned_data["target_language"]

            try:
                translator = Translator()

                result = async_to_sync(translator.translate)(
                    text,
                    src=source_language,
                    dest=target_language
                )

                translated_text = result.text

            except Exception as e:
                translated_text = f"Translation failed: {e}"

    else:
        form = TranslationForm()

    return render(
        request,
        "translator/index.html",
        {
            "form": form,
            "translated_text": translated_text,
        }
    )