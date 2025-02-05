import info
class DataLoad:    # 클래스
    user = "집가고싶다"

    def __init__(self, creator):
        self.creator = creator
        self.file = open("theusdata.txt", 'r', encoding='utf8')
    
    def Get_All_Message(self):
        list = []
        for msg in self.file.readlines():
            txt = msg.split("|")
            newInfo = info.Info(txt[1], txt[2], txt[3], txt[4])
            list.append(newInfo)
        return list
    
    def Get_User(self):
        return self.user
