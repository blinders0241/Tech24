import speech_recognition as sr
# from pydub import AudioSegment

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
FilePath = r"C:\Users\asiddique\Videos\CovertedFile\\"

class SpeechText:
    def __init__(self):
        pass

    def writeToTextFile(self, text , filename = "NewText.txt"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(text)
            return "Success"
        except Exception as e:
            print(e)
            return "Failed"
        
    def Covert_2_text(self, filename = 'WeeklySyncMeeting.wav'):
        # Reading Audio file as source
        # listening the audio file and store in audio_text variable
        with sr.AudioFile(FilePath + filename) as source:
            audio_text = r.listen(source)
            print(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            try:
                text = r.recognize_google(audio_text)
                print(text)
            except Exception as e:
                print(e)
            # print(text)
            # msg = SpeechText().writeToTextFile(self, text)
            # print(text)
            # print(msg)
            
        except Exception as e:
            print("An error occurred:")
            print(e)
        


SpeechText().Covert_2_text()