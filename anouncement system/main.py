import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    myText = str(text)
    language = "hi"
    myOb =gTTS(text=myText,lang=language,slow=False)
    myOb.save(filename)

def mergeaudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined = combined + AudioSegment.from_mp3(audio)
    return combined

def announcementSkelton():
    audio =AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dheyan dijiye
    start = 88000
    end = 90000
    audioPro = audio[start:end]
    audioPro.export('1_hindi.mp3', format= 'mp3')

    # 2 is from-city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 is via-city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3", format="mp3")

    # 6 is to-city

    # 7 - Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 is train no and name

    # 9 - Generate kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 is platform number

    # 11 - Generate par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def announcementGenerator(filename):
    df = pd.read_excel(filename)
    print(df)
    for index,item in df.iterrows():
    # 2 is from-city
        textToSpeech(item['from'],"2_hindi.mp3")
    # 4 is via-city
        textToSpeech(item['via'],"4_hindi.mp3")
    # 6 is to-city
        textToSpeech(item['to'],"6_hindi.mp3")
    # 8 is train no and name
        textToSpeech(item['train_no']+' '+item['train_name'],"8_hindi.mp3")
    # 10 is platform number
        textToSpeech(item['platform'],"10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]
        announcement = mergeaudio(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ == "__main__":
    announcementSkelton()
    announcementGenerator('announce_hindi.xlsx')