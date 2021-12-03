'''
Module for translating text between French and English
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText = None):
    '''
    Takes English text and returns the French translation
    '''
    if englishText is None:
        return ""
    translation = language_translator.translate(
            text = englishText,
            target = "fr",
            source = "en"
        ).get_result()
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText = None):
    '''
    Takes French text and returns the English translation
    '''
    if frenchText is None:
        return ""
    translation = language_translator.translate(
            text = frenchText,
            target = "en",
            source = "fr"
        ).get_result()
    return translation["translations"][0]["translation"]
