import pandas as pd 
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

class fault_analysis():
    
    def __init__(self):
        self.filepath = ""
    
    def load_data(self,load_filepath):
        self.load_filepath = load_filepath
        self.df = pd.read_csv(load_filepath)
        self.df = self.df.iloc[:,1:]

    def itemsets(self):
        frequent_itemsets = apriori(self.df,min_support=0.05,use_colnames=True)	# use_colnames=True表示使用元素名字，默认的False使用列名代表元素
        # frequent_itemsets = apriori(df,min_support=0.05)
        frequent_itemsets.sort_values(by='support',ascending=False,inplace=True)	# 频繁项集可以按支持度排序
        # print(frequent_itemsets[frequent_itemsets.itemsets.apply(lambda x: len(x)) >= 1])  # 选择长度 >=1 的频繁项集
        return frequent_itemsets
    def rules(self):   
        frequent_itemsets = apriori(self.df,min_support=0.05,use_colnames=True)	# use_colnames=True表示使用元素名字，默认的False使用列名代表元素
        # frequent_itemsets = apriori(df,min_support=0.05)
        frequent_itemsets.sort_values(by='support',ascending=False,inplace=True)	# 频繁项集可以按支持度排序
        association_rule = association_rules(frequent_itemsets,metric='confidence',min_threshold=0.1)	# metric可以有很多的度量选项，返回的表列名都可以作为参数
        association_rule.sort_values(by='leverage',ascending=False,inplace=True)    #关联规则可以按leverage排序
        return association_rule
        # association_rule.to_csv('d:/py3.7_workspace/data/mlxtend_apriori.csv' , encoding='utf-8')