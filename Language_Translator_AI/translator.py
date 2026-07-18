from deep_translator import GoogleTranslator


def translate_text(text, source_language, target_language):
    """
    Translate text using Google Translate.

    Args:
        text (str): Text to translate.
        source_language (str): Source language code (e.g. "en", "auto").
        target_language (str): Target language code (e.g. "ur").

    Returns:
        str: Translated text or an error message.
    """
    if not text.strip():
        return ""

    try:
        translator = GoogleTranslator(
            source=source_language,
            target=target_language
        )
        return translator.translate(text)

    except Exception as e:
        return f"Translation Error: {e}"
