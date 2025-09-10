from BDS_calculator import calculating_BDS_danger
from BDS_calculator import text_clener
from logger.loger_manager import Logger

class Manager_BDS_calculator:
    def __init__(self):
        #הגדרה של הרשימות העוינות
        self.text_clener = text_clener.Clener()
        self.calculater = calculating_BDS_danger.Calculating_BDS_danger()
        self.logger = Logger.get_logger()
        self.Hostile_list = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        self.very_hostile_list = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"


    #מנקה ומכין את הרשימה של המילים המסוכנות שנוכל לבדוק כמה פעמים קיימים בקובץ
    def clean_text(self):
        self.logger.info("Starting to calculate the level of danger")
        self.Hostile_list = self.calculater.decoding(self.Hostile_list)
        self.very_hostile_list = self.calculater.decoding(self.very_hostile_list)
        self.Hostile_list = self.text_clener.Converting_text_to_lowercase(self.Hostile_list)
        self.very_hostile_list= self.text_clener.Converting_text_to_lowercase(self.very_hostile_list)
        self.Hostile_list = self.calculater.string_to_list(self.Hostile_list)
        self.very_hostile_list = self.calculater.string_to_list(self.very_hostile_list)


    #הפונקציה שמהלת את כל הבדיקה
    def managemer(self, text:str)-> dict:
        result = {}
        #מנקים אצ הטקסט שנוכל לבדוק
        text = self.text_clener.Removing_punctuation_marks(text)
        text = self.text_clener.Remove_special_characters(text)
        text = self.text_clener.Removing_unnecessary_whitespace_characters(text)
        text = self.text_clener.Converting_text_to_lowercase(text)
        self.logger.debug(f"the clean text: {text}")

        bds_percent = self.calculater.Calculating_danger_percentages(text,self.Hostile_list ,self.very_hostile_list)
        self.logger.debug(f"the bds_percent of :{text}, is :{bds_percent}")
        threshold = self.calculater.is_text_danger(bds_percent)
        bds_threat_level = self.calculater.danger_lavel(bds_percent)
        result['bds_percent'] = bds_percent
        result['threshold'] = threshold
        result['bds_threat_level'] = bds_threat_level
        self.logger.debug(f"result of :{text}, is :{result}")
        return result



