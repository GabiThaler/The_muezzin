from pathlib import Path

class Mata_data_processor:
    def __init__(self):
        self.resolt={}

    def Process(self,path):
        self.resolt["path"]=path
        for k,v in self.resolt.items():
            print(k,v)




# הקטע קוד הבא מקבל את המאטא דאטא של הנתיב שאתה נותן לו
#
#
#
# from pathlib import Path
# import datetime
#
# # Create a Path object for a file
# file_path = Path(r"C:\data_project_muezzin")
#
# # Create the file for demonstration purposes if it doesn't exist
# # if not file_path.exists():
# #     file_path.touch()
#
# # Get the stat result object
# stat_info = file_path.stat()
# print(stat_info)
#
# # Access various metadata attributes
# print(f"File size: {stat_info.st_size} bytes")
# print(f"Last modification time (timestamp): {stat_info.st_mtime}")
# print(f"Last access time (timestamp): {stat_info.st_atime}")
# print(f"Creation time (timestamp): {stat_info.st_ctime}")
# print(f"File mode/permissions: {oct(stat_info.st_mode)}")
# print(f"Inode number: {stat_info.st_ino}")
# print(f"Device: {stat_info.st_dev}")
# print(f"Number of hard links: {stat_info.st_nlink}")
# print(f"User ID of owner: {stat_info.st_uid}")
# print(f"Group ID of owner: {stat_info.st_gid}")
#
#
# # Convert timestamps to human-readable datetime objects
# print(f"Last modified: {datetime.datetime.fromtimestamp(stat_info.st_mtime)}")


# עד כאןןןןןןןןןןןןןן
#
# #הקטע קוד הבא עובר על התייקיה ומוצא את הנתיב של כל קובץ בתייקיה
# target_path = Path(r"C:\Data_muezzin\podcasts")
# count=0
# for file in target_path.iterdir():
#     if file.is_file():
#         count += 1
#         print(file)

#
# # עד כאן


# from pathlib import Path
#
# target_directory = Path("C:\data_project_muezzin")
# count=0
# for file_path in target_directory.rglob("*"): # Finds all files and directories recursively
#     if file_path.is_file():
#         print(f"Found recursive file: {file_path.name} at {file_path}")
#         count+=1
# print(count)