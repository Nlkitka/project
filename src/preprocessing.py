import pymorphy2
from nltk.corpus import stopwords
from src import regs

russian_stopwords = stopwords.words("russian")


class ClearText:
    def __init__(self, dict_id_text: dict):
        """
        :param dict_id_text: dict with key-post's id, value-post's text
        """
        self.dict_id_text = dict_id_text
        self.ready_list = []
        self.final_result = {}

    def get_result(self) -> dict:
        """
        a function from a dictionary of post id and text gets a dictionary with the
        post id and the value advertising or not
        :return: dict with  key-post's id, value-ad or not
        """
        keys = self.dict_id_text.keys()
        for key in keys:
            post_text = self.dict_id_text.get(key)
            morph = pymorphy2.MorphAnalyzer()
            word_list = post_text.split()
            processed_word_list = []
            for word in word_list:
                word = word.lower()  # in case they arenet all lower cased
                if word not in stopwords.words("russian"):
                    processed_word_list.append(morph.parse(word)[0].normal_form)

            get_result = regs.RegularEx(processed_word_list)
            result = get_result.get_result_add()
            self.final_result[key] = result
            processed_word_list.clear()
        return self.final_result
