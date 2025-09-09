from pathlib import Path, WindowsPath
import os
import json


class Mata_data_processor:
    def __init__(self):
        self.resolt={}
    #בונה מילון עם השם נתיב ופרטים על הקובץ
    def Building_dictionary_with_the_metadata(self,path):
        self.resolt["path"] = path
        self.resolt["name"] = path.name
        self.resolt["info"] ={}
        self.resolt["info"]["size"] = path.stat().st_size
        self.resolt["info"]["type"] = path.suffix
        self.resolt["info"]["Creation time"] = path.stat().st_ctime
        self.resolt["info"]["Last modification time"] = path.stat().st_mtime
        self.resolt["info"]["Last access time "] = path.stat().st_atime
        self.resolt["info"]["User ID of owner"] = path.stat().st_uid
        self.resolt["info"]["User ID of group"] = path.stat().st_gid
        return self.resolt


    #אנחנו עוברים על כל המילון ובודקים האם יש ערך שלא מתאים בjson כגון נתיב ואם כן ממירים אותו ואם כן ממירים אותו
    def _prepare_for_json_serialization(self, obj):
        if isinstance(obj, dict):
            return {k: self._prepare_for_json_serialization(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._prepare_for_json_serialization(elem) for elem in obj]
        elif isinstance(obj, WindowsPath):
            return str(obj)  # Convert WindowsPath to string
        else:
            return obj

    #ממיר את המילון לjson
    def dict_to_json(self,dict):
        return  json.dumps(dict)


