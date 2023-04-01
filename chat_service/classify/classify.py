"""
意图识别模型封装
"""
import config
import fasttext

class Classify:
    def __init__(self):
        """
        加载训练好的模型
        """
        self.model = fasttext.load_model(config.classify_model_path)  # 加载模型

    def predict(self, sentence_cuted):
        """
        预测输入数据的结果，准确率
        :param sentence_cuted: 分词之后的句子
        :return: (label, acc)
        """
        result1 = self.model.predict(sentence_cuted)
        # 把所有label和acc转化到label_chat上比较其准确率
        for label, acc in zip(*result1):
            if label == "__label__chat":
                label = "__label__QA"
                acc = 1-acc
            # 判断准确率
            if acc > 0.95:
                return "QA", acc
            else:
                return "chat", 1-acc
















