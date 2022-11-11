from gtts import gTTS
import sys
import os

def say(txt, language, slow: bool=False):
    textobj = gTTS(text=txt, lang=language, slow=slow)
    textobj.save('cache/text.mp3')
    os.system("mpg123 ./cache/text.mp3")


if sys.argv[1] == 'say':


    text_list = sys.argv[2:]
    text = ' '
    for ele in text_list:
        text += f'{ele} '
    say(text, 'en', False)
    print("Done")
