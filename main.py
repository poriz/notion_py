from pprint import pprint
from crawling import c_data
from dotenv import dotenv_values
from notion_client import Client
from datetime import datetime
from sts import sts_module
sts = sts_module()
cr = c_data()
config = dotenv_values(".env")
notion_secret = config.get('NOTION_TOKEN')

content_list=cr.run_code()
contents=sts.sts_func(content_list)
contents = contents[:20]
# for i in contents:
#     print(i)
# 페이지 넣는 링크
for title,link in contents:

    notion = Client(auth=notion_secret)
    pages = notion.search(filter={"property": "object", "value": "page"})
    # pprint(pages)
    # retrieved_page = notion.pages.retrieve(page_id='')
    # pprint(retrieved_page['properties'])

    page_sample = notion.pages.retrieve(page_id='534f4768-579e-43bf-8772-e5faa4726e28')
    properties_new = page_sample['properties']
    # pprint(properties_new)
    properties_new['날짜']['date']['start'] = datetime.now().strftime("%Y-%m-%d")

    properties_new['링크']['url'] = f'{link}'

    # properties_new['상태']['select']['name'] = '생성' 생성 그대로 유지
    properties_new['이름']['title'][0]['plain_text'] = f'{title}'
    properties_new['이름']['title'][0]['text']['content'] = f'{title}'

    del properties_new['날짜']['id']
    del properties_new['링크']['id']
    del properties_new['상태']['id']
    del properties_new['상태']['select']['id']

    notion.pages.create(parent={'database_id': '89399f5d-8e29-40b2-9417-14b84a1ac727'},properties=properties_new)