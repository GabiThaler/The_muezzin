import base64


class Calculating_BDS_danger:
    def __init__(self):
        pass




    #פונקציה שממירה מהצפנה לאנגלית
    def decoding(self,string:str)->str:
        decoded_bytes = base64.b64decode(string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

    #נחלק את הטסט העוין לרשימה שנעבור עליו ובחרנו רשימה כי ככה מחלקים לפי פסיקים וא יש צמד נבדוק אותם כצמד
    def string_to_list(self,string:str)->list:
        result = string.split(',')
        return result

    #פןנקציה שמחשבת את כמות המילים העוינות ביחס לכצות המילים בטקסט
    def Calculating_danger_percentages(self,text:str , danger_text:list , veary_danger_text:list)->float:
        count = 0
        result = {}
        result1 ={}
        for word in danger_text:
            result[word] = text.count(word)

        for word in veary_danger_text:
            result1[word] = text.count(word)

        for i in result1:
            count += result1[i]
        count *=2
        for i in result:
            count += result[i]
        #אם יש תוצאה של 0 זה אומר שהטקסט בכלל לא מסוכן ולכן יהיה תוצאה של 100 שקומר שממש לא מסוכן
        if count == 0:
            return 100
        #אם יש מילים אז נחשב את רמת הסכנה לפי יחס המילים המסוכנות לכמות המילים בטקסט
        return count / len(text)


    #פונקציה שבודקת האם מסוכן או לא. אם יותר מעשר אז אין סכנה כי לא דיברו הרבה ביחס לשיחה
    def is_text_danger(self,count:float)->bool:
        if count < 10:
            return True
        return False


    #פונקציה שמחזירה כמה הסכנה
    def danger_lavel(self, count:float)->str:
        if count > 10:
            return "none"
        elif count >5:
            return "medium"
        else:
            return "high"
