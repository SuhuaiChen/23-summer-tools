import sentence_transformers.util
from sentence_transformers import SentenceTransformer
import pandas as pd
import re

df = pd.read_excel('input.xlsx')
contents = (df['反馈内容'])
pattern = '翻译： (.+)$'
queries = [re.findall(pattern, i) for i in contents]
queries = [i[0] for i in queries if i]
for i in queries:
    print(i)

# queries = queries[:5]

model = SentenceTransformer('moka-ai/m3e-base')

#Our sentences we like to encode

categories = ['主题更换为默认值', '下载4000、402、409、4002、100008', '壁纸更换为默认值', '无法应用、更换、访问、安装主题（不兼容）',
              '无法更改、安装、访问、自定义壁纸（动态壁纸）', '闹钟、铃声、声音', '其他问题', '动态壁纸', '无法整体应用主题(状态栏)',
              '无法连接网络', '广告通知推送太多', '主题被删除（不兼容）', '壁纸被删除（不兼容）', '无法整体应用主题', '无法预览主题',
              '主题、字体购买问题', '找不到字体页面', '无法删除主题、壁纸、图标、字体', '无法更改图标', '无法更改字体', '无法下载内容',
              '收藏显示不全', '服务器不可用', '墙纸较暗', 'UI配色随壁纸改变', '支付问题', '区域错误', '区域、App不兼容', '建议', '丢失文本',
              '更新问题', '主题下载丢失', '壁纸未加载', '无法更改壁纸', '无法整体应用字体', '翻译错误', '主题app问题', '字体显示异常',
              '无法安装字体', '关闭壁纸轮播', '无法关闭弹出壁纸', '无法安装图标', '无法收藏主题', '无法下载字体', '无法更新版本', '无法删除壁纸轮播',
              '没有字体选项卡', '壁纸轮播']
#Sentences are encoded by calling model.encode()
query_emb = model.encode(queries)
corpus_emb = model.encode(categories)
# Print the embeddings
# for sentence, embedding in zip(sentences, embeddings):
#  print("Sentence:", sentence)
#  print("Embedding:", embedding)
#  print("")

matched_categories_list = sentence_transformers.util.semantic_search(query_emb, corpus_emb, 5, 10, 1)

print('GENERATING LABELS\n', '*'*50)

for query, matched_categories in zip(queries, matched_categories_list):
    print('potential categories of %s:' % query)
    for matched_category in matched_categories:
        print(categories[matched_category['corpus_id']]) #, matched_category['score']

# TODO: Output to an excel file with the same sheet names as the original feedback collection file


if __name__ == '__main__':
    print('end')
