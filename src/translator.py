import googletrans
import json
import re

class Translator:
    
    def __init__(
        self,
        fileName,
        sourceLanguage,
        destinationLanguages
    ):
        self.__fileName = fileName
        self.__sourceLanguage=sourceLanguage
        self.__destinationLanguages=destinationLanguages
        self.__googleTranslator =  googletrans.Translator()
        
    def translate(self):
        loaded_json = self.__getJSON()
        for destLanguage in self.__destinationLanguages:
            print("==============================================")
            print("Translating from "+self.__sourceLanguage.upper() + " to " + destLanguage.upper() )
            for word in loaded_json:
                joinStringSpace = re.sub(r"(\w)([A-Z])", r"\1 \2", word)
                if destLanguage == self.__sourceLanguage:
                    loaded_json[word] = joinStringSpace.title()
                else:
                    loaded_json[word] = self.__getTranslate(joinStringSpace,destLanguage)	
            self.__writeJSON(destLanguage,loaded_json)

    def __getTranslate(self,word,destLanguage):
        translatedText = self.__googleTranslator.translate(word,src=self.__sourceLanguage,dest=destLanguage).text
        return translatedText.title()

    def __getJSON(self):
        filePathAndName = self.__fileName + ".json"
        with open("./src/data/"+filePathAndName,'r') as fp:
            return json.load(fp)

    def __writeJSON(self,fileName,data):
        print("Writing "+fileName+" language file")
        fullFile = './src/output/' + fileName + '.json'
        with open(fullFile,'w',encoding='utf8') as fp:
            json.dump(data,fp,ensure_ascii=False,indent=4)
        print("Wrote "+fileName+" language file")
