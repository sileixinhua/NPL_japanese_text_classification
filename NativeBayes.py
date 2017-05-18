import numpy as np

#原始数据和标注
def loadDataSet():
	# エンタ,スポー,地域,国際,国内,経済,科学
	postingList_1=[] # エンタ
	postingList_2=[] # スポー
	postingList_3=[] # 地域
	postingList_4=[] # 国際
	postingList_5=[] # 国内
	postingList_6=[] # 経済
	postingList_7=[] # 科学
	classVec = ["エンタ","スポー","地域","国際","国内","経済","科学"]
	word_number_1 = 0 # エンタ
	word_number_2 = 0 # スポー
	word_number_3 = 0 # 地域
	word_number_4 = 0 # 国際
	word_number_5 = 0 # 国内
	word_number_6 = 0 # 経済
	word_number_7 = 0 # 科学

	# エンタ数据读取
	f_1 = open("./test_data/エンタ.txt",'r', encoding='UTF-8')
	while True:
	  line_1=f_1.readline()
	  if line_1:
	    postingList_1.append(line_1)
	    # print (postingList[word_number])
	    word_number_1 = word_number_1 + 1
	  else:
	    break

	# スポー数据读取
	f_2 = open("./test_data/スポー.txt",'r', encoding='UTF-8')
	while True:
	  line_2=f_2.readline()
	  if line_2:
	    postingList_2.append(line_2)
	    # print (postingList[word_number])
	    word_number_2 = word_number_2 + 1
	  else:
	    break

	# 地域数据读取
	f_3 = open("./test_data/地域.txt",'r', encoding='UTF-8')
	while True:
	  line_3=f_3.readline()
	  if line_3:
	    postingList_3.append(line_3)
	    # print (postingList[word_number])
	    word_number_3 = word_number_3 + 1
	  else:
	    break

	# 国際数据读取
	f_4 = open("./test_data/国際.txt",'r', encoding='UTF-8')
	while True:
	  line_4=f_4.readline()
	  if line_4:
	    postingList_4.append(line_4)
	    # print (postingList[word_number])
	    word_number_4 = word_number_4 + 1
	  else:
	    break

	# 国内数据读取
	f_5 = open("./test_data/国内.txt",'r', encoding='UTF-8')
	while True:
	  line_5=f_5.readline()
	  if line_5:
	    postingList_5.append(line_5)
	    # print (postingList[word_number])
	    word_number_5 = word_number_5 + 1
	  else:
	    break

	# 経済数据读取
	f_6 = open("./test_data/経済.txt",'r', encoding='UTF-8')
	while True:
	  line_6=f_6.readline()
	  if line_6:
	    postingList_6.append(line_6)
	    # print (postingList[word_number])
	    word_number_6 = word_number_6 + 1
	  else:
	    break

	# 科学数据读取
	f_7 = open("./test_data/科学.txt",'r', encoding='UTF-8')
	while True:
	  line_7=f_7.readline()
	  if line_7:
	    postingList_7.append(line_7)
	    # print (postingList[word_number])
	    word_number_7 = word_number_7 + 1
	  else:
	    break

	postingList=[]
	postingList = np.concatenate((postingList_1,postingList_2,postingList_3,postingList_4,postingList_5,postingList_6,postingList_7))
	# print (classVec)
	# print (word_number_1)
	# print (word_number_2)
	# print (word_number_3)
	# print (word_number_4)
	# print (word_number_5)
	# print (word_number_6)
	# print (word_number_7)
	classVec = ["エンタ","スポー","地域","国際","国内","経済","科学"]
	return postingList,classVec

#创建词汇表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

mydata,classVec = loadDataSet()

vocabList = createVocabList(mydata)

#句子转向量
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

sVec = [setOfWords2Vec(vocabList,inputset) for inputset in mydata]

#贝叶斯分类器训练函数
#输入参数是文档向量矩阵、每篇文档类别标签
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)  #参与训练的文档数
    numWords = len(trainMatrix[0])   #特征数量
    pAbusive = sum(trainCategory)/float(numTrainDocs)  #每篇文档属于侮辱性文档的概率
    p0Num = np.ones(numWords)     #初始化都为1的矩阵 防止出现词汇概率0
    p1Num = np.ones(numWords)      #初始化都为1的矩阵
    p0Denom = 2.0   #初始化为2 因为侮辱句和非侮辱句概率为0.5
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i] #侮辱句向量相加
            p1Denom += sum(trainMatrix[i])  #侮辱句词汇数量相加
        else:
            p0Num += trainMatrix[i] #非侮辱句向量相加
            p0Denom += sum(trainMatrix[i]) #非侮辱句词汇数量相加
    p1Vect = np.log(p1Num/p1Denom)          # 防止概率过小 取对数，跟后面贝叶斯公式计算概率对应
    p0Vect = np.log(p0Num/p0Denom)
    # p1Vect = p1Num / p1Denom  # 侮辱句子向量和/总得侮辱句中的词汇数量= 侮辱句中 每个词出现的概率
    # p0Vect = p0Num / p0Denom  # 非侮辱句中每个词出现的概率
    return p0Vect,p1Vect,pAbusive

p0Vec,p1Vec,pAbusive = trainNB0(sVec,classVec)

#朴素贝叶斯分类函数
#输入参数为 要分类的向量、以及上面函数计算得到的三个概率
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #根据贝叶斯公式计算是侮辱性句子的概率
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry = ['銭形', '警部', '日テレ','共同','制作','制作','ビジネス','モデル']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

testingNB()