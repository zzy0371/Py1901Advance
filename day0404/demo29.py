"""
1requests 发出web请求
2response 得到相应
3re 提取信息
"""
import requests,re
response = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html",)
# print(response.text)
# 使用re提取 股票名 股票代码 股票最新价
# 获取所有股票信息
result = re.search(r'<tbody class="tbody_right" id="datalist">(.*?)</tbody>',response.text,re.S)
# print(result.group(1))
result = re.findall(r'<tr>(.*?)</tr>',result.group(1))
# print(result)
with open('data.txt', 'w',encoding='utf8') as f:
    for r in result:
        r1 = re.findall(r'<td.*?>(.*?)</td>', r)
        # print(r1[0],r1[1],r1[2])
        id = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">\1</a>', r1[0])
        # print(id.group(1))
        name = re.search(r'<a href="//stock.quote.stockstar.com/(.*?).shtml">(.*?)</a>', r1[1])
        # print(name.group(2))
        price = re.search(r'<span class="red">(.*?)</span>', r1[2])
        print(price.group(1))
        info = "股票代码  "+str(id.group(1))+"股票名称  "+str(name.group(2))+"股票价格  "+str(price.group(1))
        f.write(info)
        f.write('\n')