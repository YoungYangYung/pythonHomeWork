f = open('data.txt', 'r')
text = f.read().split('\n')

# 把数据处理成
# [
#     {
#         len: 5,
#         school: [],
#         country: ''
#     }
# ]

obj = {}
dataList = []
for t in text:
    if (t):
        l = t.split(',')
        if (obj.get(l[2])):
            obj[l[2]] += [l[1]]
        else:
            obj[l[2]] = [l[1]]

keys = list(obj.keys())
values = obj.values()

for i,v in enumerate(values):
    cObj = {
        "len": len(v),
        "school": v,
        "country": keys[i]
    }
    dataList.append(cObj)

dataList.sort(key = lambda x:x['len'], reverse=True)
for p in dataList:
    print('{}：{}：{}'.format(p['country'], p['len'], " ".join(p['school'])))