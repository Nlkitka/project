import json
import vk_requests

ID_GROUP = '-150622463'
TOKEN = '37e26ec9ba743c1dc24045ed673e1ccc863d6beafe9ae89d902e7b3e1c5543469c27656b3fde900d00321'
api = vk_requests.create_api(service_token=TOKEN)


class ParsAllId:
    def __init__(self):
        self.all_texts_from_posts = []
        self.all_texts_and_id_post = {}

    def pars_id_posts(self):
        posts = api.wall.get(owner_id=ID_GROUP, count=99)
        p = '../data/raw.json'
        with open(p, 'w', encoding='utf-8') as file:
            json.dump(posts, file, indent=2, ensure_ascii=False)

    def get_text(self):
        with open('../data/raw.json', encoding='utf-8') as f:
            data = json.load(f)
        return data['items'][0]['text']

    def get_posts_text_and_id(self):
        with open('../data/raw.json', encoding='utf-8') as f:
            data = json.load(f)
        for item in data['items']:
            self.all_texts_from_posts.append(item['text'])
            self.all_texts_and_id_post[str(item['id'])] = item['text']


testobj = ParsAllId()
testobj.pars_id_posts()
testobj.get_posts_text_and_id()
# print(testobj.get_text())
