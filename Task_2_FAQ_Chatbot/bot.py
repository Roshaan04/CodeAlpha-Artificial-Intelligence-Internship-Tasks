import spacy
from faq_data import faq

nlp = spacy.load("en_core_web_md")


def get_response(user_input):

    user_doc = nlp(user_input.lower())

    best_match = None
    best_score = 0

    for question in faq.keys():

        question_doc = nlp(question.lower())

        similarity = user_doc.similarity(question_doc)

        if similarity > best_score:
            best_score = similarity
            best_match = question

    # confidence threshold
    if best_score > 0.6:
        return faq[best_match]

    return "Sorry, I didn't understand that. Can you rephrase?"