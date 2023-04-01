import fasttext
import config

def build_classify_model():
    model = fasttext.train_supervised(config.classify_corpus_train_path, epoch=20, wordNgrams=1, minCount=5)
    model.save_model(config.classify_model_path)

def get_classify_model():
    """加载model"""
    model = fasttext.load_model(config.classify_model_path)
    return model

def eval():
    """模型评估"""
    pass
