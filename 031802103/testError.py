import os

class MyError(Exception):
    pass
class TextNoExistError(MyError):        #文件不存在
    def __init__(self, file_a):
        self.fa = file_a
    def __str__(self):
        return self.fa+ "该文件不存在！"

class TextEmptyError(MyError):          #文件无内容
    def __init__(self, file_a):
        self.fa = file_a
    def __str__(self):
        return self.fa+ "该文件啥都没有！"