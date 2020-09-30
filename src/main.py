import sys
from googletrans import LANGUAGES
import os
from translator import Translator

def supportedLanguagesCode():
    print("===================== Support Language =====================")
    print("\t\t\tLANGUAGE = LANGUAGE CODE")
    for lang in LANGUAGES:
        print(f"\t\t\t{LANGUAGES[lang]} => {lang}")
    print("===================== Support Language =====================")

def languageCode():
    langCode = input("Enter the default source language code: ")
    if not LANGUAGES.get(langCode):
        print("Not Supported Language Code")
        return languageCode()
    return langCode

def fileName():
    print("Example file names: Default-Language, Language-TR, Words-En, etc... ")
    file = input("Enter the default language file name : ")
    if(os.path.exists("./src/data/"+file+".json")):
        return file
    print("Not find file")
    return fileName()

#supportedLanguagesCode()
defaultLanguageCode = "en"#languageCode()
defaultLanguageFileName ="word-en" #fileName()
desctinationLanguages=["tr","de","en"]##[]
print("input is 0(Zero) to complete")
# while True:    
#     languageCode = input("Enter destination language code : ")
#     if languageCode=="0":
#         break
#     if languageCode not in LANGUAGES:
#         print("Not Supported Language Code")
#         continue
#     desctinationLanguages.append(languageCode)
print(list(desctinationLanguages))    
translator = Translator(defaultLanguageFileName,defaultLanguageCode,desctinationLanguages)
translator.translate()