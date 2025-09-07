from pathlib import Path
import os

class Mata_data_processor:
    def __init__(self):
        self.resolt={}

    def Process(self,path):
        self.resolt["path"]=path
        self.resolt["name"] = path.name
        self.resolt["info"] ={}
        self.resolt["info"]["size"] = path.stat().st_size
        self.resolt["info"]["type"] = path.suffix
        self.resolt["info"]["Creation time"] = path.stat().st_ctime
        self.resolt["info"]["Last modification time"] = path.stat().st_mtime
        self.resolt["info"]["Last access time "] = path.stat().st_atime
        self.resolt["info"]["User ID of owner"] = path.stat().st_uid
        self.resolt["info"]["User ID of group"] = path.stat().st_gid
        stat_info = path.stat()
        print(stat_info)
        for k,v in self.resolt.items():
            print(k,v)

