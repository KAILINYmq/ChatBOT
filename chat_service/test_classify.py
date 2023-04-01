"""测试分类相关的api"""
from classify.build_model import build_classify_model, get_classify_model
from classify.classify import Classify

if __name__ == "__main__":
    # model = get_classify_model()
    # text = ["哈哈哈"]
    # ret = model.predict(text)
    # print(ret)
    classify = Classify()
    ret = classify.predict("python")
    print(ret)