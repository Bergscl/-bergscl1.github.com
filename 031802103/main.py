# -*- coding: utf-8 -*-

import sys
import jieba
import jieba.posseg as pseg
from jieba import analyse
import os
import testErrors


class SimilarityMethod(object):

    def __init__(self, file_a, file_b):  # 初始化类
        str_a = ''
        str_b = ''
        try:
            if not os.path.isfile(file_a):                  #file_a文件不存在的异常处理
                raise testError.TextNoExistError(file_a)
            elif not os.path.getsize(file_a):                #file_a文件无内容的异常处理
                raise testError.TextEmptyError(file_a)
        except Exception as e:
            print(e)
            os._exit(0)

        else:
            with open(file_a, 'r', encoding='UTF-8') as f:
                for line in f.readlines():
                    str_a += line.strip()
                f.close()
        try:
            if not os.path.isfile(file_b):
                raise testError.TextNoExistError(file_b)
            elif not os.path.getsize(file_b):
                raise testError.TextEmptyError(file_b)
        except Exception as e:
            print(e)
            os._exit(0)
        else:
            with open(file_b, 'r', encoding='UTF-8') as f:
                for line in f.readlines():
                    str_b += line.strip()
                f.close()

        self.str_a = str_a  # 将文档内容读入字符串
        self.str_b = str_b

    def SplitWords(self, str_a):  # 将读入的字符串分词，返回分词后的字符串（空格隔开）
        wordsa = pseg.cut(str_a)
        cuta = ""
        seta = set()
        for key in wordsa:
            cuta += key.word + " "
            seta.add(key.word)
        return [cuta, seta]

    def JaccardSim(self, str_a, str_b):  # 计算Jaccard相似系数
        seta = self.SplitWords(str_a)[1]
        setb = self.SplitWords(str_b)[1]
        sa_sb = 1.0 * len(seta & setb) / len(seta | setb)
        return sa_sb

if __name__ == '__main__':
    a = SimilarityMethod(sys.argv[1], sys.argv[2])
    sys.stdout = open(sys.argv[3], mode='w', encoding='utf-8')
    print('%.2f' % a.JaccardSim(a.str_a, a.str_b))
