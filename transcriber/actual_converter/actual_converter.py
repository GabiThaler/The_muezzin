from faster_whisper import WhisperModel
import pkg_resources
from logger.loger_manager import Logger


class Transcriber:
    def __init__(self):
        self.loger = Logger.get_logger()
    def Transcriber_activator(self,path):
        result = ""
        #בחירת גודל הקובץ
        model_size = "small"

        #בחירת המעבד והמחשב שמשתמשים בו
        model = WhisperModel(model_size, device="cpu", compute_type="float32")

        #בחירת הקובץ שנתמלל ושפה
        segments, info = model.transcribe(path, language="en")


        #עוברים בלולאה על התמלול ומדפיסים לפי חלקים וכותבים ממתי עד מתי בשניות ואת המלל
        for segment in segments:
            result += segment.text
        self.loger.info(f"Transcriber activated {segments}")
        return result
