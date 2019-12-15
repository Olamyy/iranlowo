from googletrans import Translator

from iranlowo.models import get_model_path


def googletrans_detect_language(text):
    client = Translator()
    result = client.detect(text)
    return result.lang, result.confidence


def fasttext_detect_language(text):
    model_path = get_model_path('fasttext_langid_model')
    try:
        import fasttext
        model = fasttext.load_model(model_path)
        result = model.predict(text, k=1)
        return result[0][0].split("__label__")[1], result[1][0]
    except ImportError:
        raise ImportError("The fastText module is needed for this function. You can install it here https://github.com/facebookresearch/fastText/tree/master/python")
