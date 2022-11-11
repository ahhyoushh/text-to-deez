from gtts import gTTS
import sys
import os

cache_root = "~/projects/text-to-deez/cache"

def say(txt, language, slow: bool=False):
    textobj = gTTS(text=txt, lang=language, slow=slow)
    textobj.save(f'text.mp3')
    os.system(f"mpg123 text.mp3")


if sys.argv[1] == 'say':


    text_list = sys.argv[2:]
    text = ' '
    for ele in text_list:
        text += f'{ele} '
    say(text, 'en', False)
    print("Done")
