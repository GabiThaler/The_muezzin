import re
import string

class Clener:

    #פונקציה שמנקה את הטקסט מסימני פיסוק
    def Removing_punctuation_marks(self,text):
        #פונקציה מובנת בפייתון שמנקה טקסטים מסימני פיסוק
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    # פונקציה להסרת סימני פיסוק ותווים מיוחדים
    def Remove_special_characters(self,text):
        cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return cleaned_text

    #מסירים רווחים מיותרים
    def Removing_unnecessary_whitespace_characters(self,text):
        clean_text = " ".join(text.split())
        return clean_text


    #ממירים את כל האותיות לאותיות קטנות
    def Converting_text_to_lowercase(self,text):
        clean_text = text.lower()
        return clean_text