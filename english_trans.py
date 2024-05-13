import googletrans
# import open

translator = googletrans.Translator()

inStr = str(input())

outStr = translator.translate(inStr, dest = 'en', src = 'ko')

print("번역된 문장 : ", outStr.text, sep=' ')
