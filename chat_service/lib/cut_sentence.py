"""
分词
"""
import jieba
import jieba.posseg as psg
import config
import string
from lib import stopwords
import logging


# 关闭jieba log输出
jieba.setLogLevel(logging.INFO)

jieba.load_userdict(config.user_dict_path)
# 准备英文字符
letters = string.ascii_lowercase+"+"

def cut_sentece_by_word(sentence):
    """实现中文英文分词"""
    result = []
    temp = ""
    for word in sentence:
        # 把英文单词进行拼接
        if word.lower() in letters:
            temp += word
        else:
            # 出现中文，把中文添加到结果中
            if temp != "":
                result.append(temp.lower())
                temp = ""
            result.append(word.strip())
    # 判断最后的字符是否为英文
    if temp != "":
        result.append(temp.strip())
    return result

def cut(sentence, by_word=False, use_stopwords=False, with_sg=False):
    """
    :param sentence: 句子
    :param by_word: 是否按照单个字分词
    :param use_stopwords: 是否使用停用词
    :param with_sg: 是否返回词性
    :return:
    """
    if by_word:
        result = cut_sentece_by_word(sentence)
    else:
        result = psg.lcut(sentence)
        result = [(i.word, i.flag) for i in result]
        if not with_sg:
            result = [i[0] for i in result ]
    # 是否使用停用词
    if use_stopwords:
        result = [i for i in result if i not in stopwords]
    return result

if __name__ == '__main__':
    a = "python和c++哪个难?hello"
    print(cut_sentece_by_word(a))