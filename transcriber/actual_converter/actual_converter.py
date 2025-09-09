from faster_whisper import WhisperModel
import pkg_resources


class Transcriber:
    def __init__(self):
        pass
    def Transcriber_activator(self,path):
        result = ""
        #בחירת גודל הקובץ
        model_size = "small"

        #בחירת המעבד והמחשב שמשתמשים בו
        model = WhisperModel(model_size, device="cpu", compute_type="float32")

        #בחירת הקובץ שנתמלל ושפה
        segments, info = model.transcribe(path, language="en")

        # Print the detected language and its probability.
        # print(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")

        #עוברים בלולאה על התמלול ומדפיסים לפי חלקים וכותבים ממתי עד מתי בשניות ואת המלל
        for segment in segments:
            print(type(segment.text))
            result += segment.text
            print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        return result
