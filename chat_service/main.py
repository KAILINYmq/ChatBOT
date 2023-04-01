# from prepar_corpus.prepar_user_dict.test_user_dict import test_user_dict
from lib.cut_sentence import cut

if __name__ == "__main__":
    s = "Python难不难， 果真，过，哈"
    print(cut(s, with_sg=False, use_stopwords=True))
    