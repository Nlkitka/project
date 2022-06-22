import regex as re


class RegularEx:
    def __init__(self, word_list):
        self.words_list = word_list
        self.result = ""

    def find_add(self, word):
        try:
            regex = re.compile(r'(распродажа)|(cкидка)(выгодн(\w+))|(подписка)|(онлайн-курсам)|(заполнять)|'
                               r'(присоедин(я|и)ться)|(бесплатн(\w+))|(Получ(\w+))|(Подробн(\w+))|(смотреть)|'
                               r'(сслк(\w+))|(оформить)|(промокод)|(Презентация)|(стажировка)|(заявка)|'
                               r'(доставк(\w+))', re.IGNORECASE)
            return regex.search(word).group()

        except AttributeError:
            return "Рекламы нет"

    def get_result_add(self):
        for word in self.words_list:
            if self.find_add(word) != 'Рекламы нет':
                return "это реклама"
        return "это не реклама"
