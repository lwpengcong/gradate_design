import pandas as pd 
import numpy as np 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import seaborn as sns
import matplotlib.pyplot as plt


class faultidentify():
    def __init__(self):
        self.filepath = ""
        self.encoding_path = 'd:/py3.7_workspace/data/encodering.csv'

    def load_data(self,filepath):
        self.filepath = filepath
        # df = pd.read_csv(filepath)
        # 数据预处理
        # faultinfo_1，有32种故障代码，每一种故障代码我看一个维度，有的话是1，没有的话是0，这样每一条数据就对应着一个32维的特征向量。

        # one-hot编码

        # define label
        self.labeldata1 = ['0x00000001H','00000002H','00000004H','00000008H','00000010H','00000020H','00000040H','00000080H','00000100H','00000200H','00000400H','00000800H','00001000H','00002000H'
        ,'00004000H','00008000H','00010000H','00020000H','00040000H','00080000H','00100000H','00200000H','00400000H','00800000H','01000000H','02000000H','04000000H','08000000H'
        ,'10000000H','20000000H','40000000H','80000000H']

        self.labeldata = [0x00000001,0x00000002,0x00000004,0x00000008,0x00000010,0x00000020,0x00000040,0x00000080,0x00000100,0x00000200,0x00000400,0x00000800,0x00001000,0x00002000
        ,0x00004000,0x00008000,0x00010000,0x00020000,0x00040000,0x00080000,0x00100000,0x00200000,0x00400000,0x00800000,0x01000000,0x02000000,0x04000000,0x08000000
        ,0x10000000,0x20000000,0x40000000,0x80000000]

        self.data_all = pd.read_csv(self.filepath)

        self.data = pd.read_csv(self.filepath, usecols = [43])
        #读取第43列的前200行
        # data = pd.read_csv("d:/py3.7_workspace/data/faultinfo_1.csv", usecols = [43])
        #'00004000H'是列名
        self.data.loc[self.data['00004000H'] == '00000002H'] = 0x00000002
        self.data.loc[self.data['00004000H'] == '00000080H'] = 0x00000080
        self.data.loc[self.data['00004000H'] == '00000200H'] = 0x00000200
        self.data.loc[self.data['00004000H'] == '00004000H'] = 0x00004000
        self.data.loc[self.data['00004000H'] == '00080000H'] = 0x00080000
        self.data.loc[self.data['00004000H'] == '00200200H'] = 0x00200200
        self.data.loc[self.data['00004000H'] == '00204000H'] = 0x00204000
        self.data.loc[self.data['00004000H'] == '00280000H'] = 0x00280000
        self.data.loc[self.data['00004000H'] == '10000000H'] = 0x10000000
        self.data.loc[self.data['00004000H'] == '10020000H'] = 0x10020000
        self.data.loc[self.data['00004000H'] == '80000400H'] = 0x80000400
        self.data.loc[self.data['00004000H'] == '80000600H'] = 0x80000600
        self.data.loc[self.data['00004000H'] == '80000800H'] = 0x80000800
        self.data.loc[self.data['00004000H'] == '80000A00H'] = 0x80000A00
        self.data.loc[self.data['00004000H'] == '80000C00H'] = 0x80000C00
        self.data.loc[self.data['00004000H'] == '80000E00H'] = 0x80000E00
        self.data.loc[self.data['00004000H'] == '80002000H'] = 0x80002000
        self.data.loc[self.data['00004000H'] == '80200400H'] = 0x80200400
        self.data.loc[self.data['00004000H'] == '80200800H'] = 0x80200800
        self.data.loc[self.data['00004000H'] == '80200A00H'] = 0x80200A00
        self.data.loc[self.data['00004000H'] == '80200E00H'] = 0x80200E00
        self.data.loc[self.data['00004000H'] == '80202000H'] = 0x80202000
        self.data.loc[self.data['00004000H'] == '80202800H'] = 0x80202800
        self.data.loc[self.data['00004000H'] == '80202A00H'] = 0x80202A00
        self.data.loc[self.data['00004000H'] == '80202E00H'] = 0x80202E00
        self.data.loc[self.data['00004000H'] == '80204400H'] = 0x80204400
        # print(data)

        self.testdatatable = [0]*32
        self.list1 = []

    
    def encoding(self):
        # integer encode
        
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.labeldata)
        # print(integer_encoded)
        # binary encode
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
        # print(onehot_encoded)
        return onehot_encoded
    #将数据集进行编码


    def faultdiv(self):
        # integer encode
        label_encoder = LabelEncoder()
        integer_encoded = label_encoder.fit_transform(self.labeldata)
        # print(integer_encoded)
        # binary encode
        onehot_encoder = OneHotEncoder(sparse=False)
        integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
        onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
        # print(onehot_encoded)
        return onehot_encoded
        for datai in self.data['00004000H']:
            for i in range(0,32):
                x = 31-i
                if (datai - self.labeldata[x]) >= 0:
                    datai = datai - self.labeldata[x]
                    # print(datai)
                    testdatatable = testdatatable + onehot_encoded[i]
            self.list1.append(testdatatable)
            self.testdatatable = [0]*32

        # print(list1)

        #编码后生成一个csv文件
        name = list(reversed(self.labeldata1))
        self.test = pd.DataFrame(columns = name ,data = self.list1)
        self.test.to_csv(self.encoding_path , encoding='utf-8')
        return self.test

    def account(self):
        #测试集各类故障数目
        # datacount = pd.read_csv("d:/py3.7_workspace/data/faultdis.csv")
        data = self.data
        data['00004000H'] = data['00004000H'].apply(lambda x: str(hex(x))[:2]+'0'*(10-len(str(hex(x))))+str(hex(x))[2:])
        data_count = data.groupby("00004000H").size().to_dict()
        data_count = sorted(data_count.items(), key=lambda x:x[1], reverse=True)[:7]
        xx = [k[0] for k in data_count]
        yy = [min(k[1], 50000) for k in data_count]
        sns.barplot(x=xx, y=yy)
        plt.xticks(rotation=15)
        plt.show()
        # print(data_count)
        # print(type(data_count))
        return data_count

    def kmeans_label(self):
        # k-means算法实现
        # 生成聚类标签
        from sklearn.cluster import KMeans
        # kmeans=KMeans(n_clusters = 10 , max_iter = 10)   #n_clusters:number of cluster
        kmeans=KMeans(n_clusters = 32 , max_iter = 1000)
        kmeans.fit(self.test)
        np.savetxt('d:/py3.7_workspace/data/keans_labels.txt', kmeans.labels_)
        uniques = np.unique(kmeans.labels_)
        return uniques
        # print(uniques)
        # onehot_inverse = onehot_encoder.inverse_transform(kmeans.labels_)
        # print(onehot_inverse)