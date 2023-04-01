import pandas
from lib import cut
import config
from tqdm import tqdm
import json
import random


flags = [0, 0, 0, 0, 1]

# 闲聊的语料
xiaohunagji_path = r"G:\Python\XM_file\ChatBOT\chat_service\corpus\classify\origin_corpus\小黄鸡未分词.conv"
# 问答的语料
byhand_path = r"G:\Python\XM_file\ChatBOT\chat_service\corpus\classify\origin_corpus\手动构造的问题.json"
crawled_path = r"G:\Python\XM_file\ChatBOT\chat_service\corpus\classify\origin_corpus\爬虫抓取的问题.csv"

def keywords_in_line(line):
    # 判断line中是否存在不符合要求的词
    keywords_list = ["传智播客", "传智", "黑马程序员", "黑马", "python",
                     "人工智能", "c语言", "c++", "java", "javaee", "前端", "移动开发", "ui",
                     "ue", "大数据", "软件测试", "php", "h5", "产品经理", "linux", "运维", "go语言",
                     "区块链", "影视制作", "pmp", "项目管理", "新媒体", "小程序", "游戏开发", "c4d"]

    for word in line:
        if word in keywords_list:
            return True
        else:
            return False

def process_xiaohuangji(f_train, f_test):
    """处理小黄鸡语料"""
    flag = 0
    num_train = 0
    num_test = 0
    for line in tqdm(open(xiaohunagji_path, encoding="utf-8").readlines(), desc="小黄鸡"):
        # TODO 句子长度为1个字母，后期需改善
        if line.startswith("E"):
            flag = 0
            continue
        elif line.startswith("M"):
            # 第一个出现M
            if flag == 0:
                line = line[1:].strip()
                flag = 1
            else:
                # 不需要第二个出现的M开头句子
                continue

        line_cuted = cut(line)
        if not keywords_in_line(line_cuted):
            line_cuted = " ".join(line_cuted)+"\t"+"__label__chat"
            if random.choice(flags) == 0:
                f_train.write(line_cuted + "\n")
                num_train += 1
            else:
                f_test.write(line_cuted+"\n")
                num_test += 1
    return num_train, num_test

def process_byhand_data(f_train, f_test):
    """处理手动构造的数据"""
    total_lines = json.loads(open(byhand_path, encoding="utf-8").read())
    num_train = 0
    num_test = 0
    for key in total_lines:
        for lines in tqdm(total_lines[key], desc="byhand_data"):
            for line in lines:
                if "校区" in line:
                    continue
                line_cuted = cut(line)
                line_cuted = " ".join(line_cuted)+"\t"+"__label__QA"
                if random.choice(flags) == 0:
                    f_train.write(line_cuted + "\n")
                    num_train += 1
                else:
                    f_test.write(line_cuted + "\n")
                    num_test += 1
    return num_train, num_test

def process_crawled_data(f_train, f_test):
    """处理抓取的数据"""
    num_train = 0
    num_test = 0
    for line in tqdm(open(crawled_path, encoding="utf-8").readlines(), desc="crawled_data"):
        line_cuted = cut(line)
        line_cuted = "".join(line_cuted)+"\t"+"__label__QA"
        if random.choice(flags) == 0:
            f_train.write(line_cuted + "\n")
            num_train += 1
        else:
            f_test.write(line_cuted + "\n")
            num_test += 1
    return num_train, num_test

def process():
    f_train = open(config.classify_corpus_train_path, "a", encoding="utf-8")
    f_test = open(config.classify_corpus_test_path, "a", encoding="utf-8")
    # 1.处理小黄鸡
    num_chat_train, num_chat_test = process_xiaohuangji(f_train, f_test)
    # 2.处理手动构造的句子
    num_qa_train, num_qa_test = process_byhand_data(f_train, f_test)
    # 3. 处理抓取的句子
    _a,  _b= process_crawled_data(f_train, f_test)
    num_qa_train += _a
    num_qa_test += _b

    f_train.close()
    f_test.close()
    print(num_chat_train+num_qa_train, num_chat_test+num_qa_test)











