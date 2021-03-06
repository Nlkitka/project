from src import parser
import preprocessing
import receive


if __name__ == '__main__':
    """
    the main function, by launching which the project will work
    """
    pars_info = parser.ParsAllId()
    pars_info.pars_id_posts()
    pars_info.get_posts_text_and_id()
    text_check_add = preprocessing.ClearText(pars_info.all_texts_and_id_post)
    print(text_check_add.get_result())
    receive.send_mes(text_check_add.get_result())