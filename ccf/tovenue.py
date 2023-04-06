from EasyLogin import EL
a=EL(cachedir="__pycache__")

category={
    "ccf": [
        "计算机体系结构/并行与分布计算/存储系统", 
        "计算机网络", 
        "网络与信息安全", 
        "软件工程/系统软件/程序设计语言", 
        "数据库/数据挖掘/内容检索",
        "计算机科学理论",
        "计算机图形学与多媒体",
        "人工智能",
        "人机交互与普适计算",
        "交叉/综合/新兴",
    ],
    "tsinghua": [
        "高性能计算",
        "计算机网络",
        "网络与信息安全",
        "理论计算机科学",
        "系统软件与软件工程",
        "数据库与数据挖掘",
        "人工智能与模式识别",
        "计算机图形学与多媒体",
        "人机交互与普适计算",
        "综合与交叉"
    ]
}

flag="ccf"
#flag="tsinghua"

KNOWN={
    "usenix":["USENIX Annual Technical Conference", "USENIX Annual Technical Conference, General Track"],
    "sigmod":"SIGMOD Conference",
    "vldb":"Proc. VLDB Endow.",
    "mm":'ACM Multimedia',
    "visualization":['IEEE Trans. Vis. Comput. Graph.', 'IEEE VIS'],
    "nips":'NeurIPS',
    "cscw":'Proc. ACM Hum. Comput. Interact.',
    "huc":"ISWC",
    "coco":"CCC",
}

for idx, line in enumerate(open(f"{flag}_a.txt")):
    if idx%2==0:
        prefix = "journals"
    else:
        prefix = "conf"
    for short in line.split():
        x=a.get(f"https://dblp.org/search/publ/api?q=stream%3Astreams%2F{prefix}%2F{short}%3A&h=1000&format=json", o=True, cache=True)
        #print(x.json())
        if short not in KNOWN:
            vs = set()
            for i in x.json()["result"]["hits"]["hit"]:
                if not "venue" in i["info"]:
                    continue
                if isinstance(i["info"]["venue"], str):
                    vs.add(i["info"]["venue"])
                else:
                    #print(i)
                    vs.update(i["info"]["venue"])
            res = sorted(i for i in vs if "@" not in i and "workshop" not in i.lower())
            if len(res)>1 and short in [i.lower() for i in res]:
                res = [i for i in res if i.lower()==short]
        #print(category[idx//2], prefix, short, res, sep="\t")
        else:
            res = KNOWN[short]
            if isinstance(res, str):
                res=[res]
        for r in res:
            print(flag, category[flag][idx//2], prefix, short, r, sep="\t")