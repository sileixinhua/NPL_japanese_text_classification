import numpy as np

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

	f_1 = open("./test_data/エンタ.txt",'r', encoding='UTF-8')
	while True:
	  line_1=f_1.readline()
	  if line_1:
	    postingList_1.append(line_1)
	    word_number_1 = word_number_1 + 1
	  else:
	    break

	f_2 = open("./test_data/スポー.txt",'r', encoding='UTF-8')
	while True:
	  line_2=f_2.readline()
	  if line_2:
	    postingList_2.append(line_2)
	    word_number_2 = word_number_2 + 1
	  else:
	    break

	f_3 = open("./test_data/地域.txt",'r', encoding='UTF-8')
	while True:
	  line_3=f_3.readline()
	  if line_3:
	    postingList_3.append(line_3)
	    word_number_3 = word_number_3 + 1
	  else:
	    break

	f_4 = open("./test_data/国際.txt",'r', encoding='UTF-8')
	while True:
	  line_4=f_4.readline()
	  if line_4:
	    postingList_4.append(line_4)
	    word_number_4 = word_number_4 + 1
	  else:
	    break

	f_5 = open("./test_data/国内.txt",'r', encoding='UTF-8')
	while True:
	  line_5=f_5.readline()
	  if line_5:
	    postingList_5.append(line_5)
	    word_number_5 = word_number_5 + 1
	  else:
	    break

	f_6 = open("./test_data/経済.txt",'r', encoding='UTF-8')
	while True:
	  line_6=f_6.readline()
	  if line_6:
	    postingList_6.append(line_6)
	    word_number_6 = word_number_6 + 1
	  else:
	    break

	f_7 = open("./test_data/科学.txt",'r', encoding='UTF-8')
	while True:
	  line_7=f_7.readline()
	  if line_7:
	    postingList_7.append(line_7)
	    word_number_7 = word_number_7 + 1
	  else:
	    break

	postingList=[]
	postingList = np.concatenate((postingList_1,postingList_2,postingList_3,postingList_4,postingList_5,postingList_6,postingList_7))
	classVec = ["エンタ","スポー","地域","国際","国内","経済","科学"]
	return postingList,classVec

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

mydata,classVec = loadDataSet()

vocabList = createVocabList(mydata)

def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

sVec = [setOfWords2Vec(vocabList,inputset) for inputset in mydata]

def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix) 
    numWords = len(trainMatrix[0])
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0 
    p1Denom = 2.0

    p1Vect = np.log(p1Num/p1Denom)
    p0Vect = np.log(p0Num/p0Denom)

    return p0Vect,p1Vect

p0Vec,p1Vec = trainNB0(sVec,classVec)

def classifyNB(vec2Classify, p0Vec, p1Vec):
    p1 = sum(vec2Classify * p1Vec)    
    p0 = sum(vec2Classify * p0Vec)
    if p1 > p0:
        return "スポー"
    else:
        return "エンタ"

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    p0V,p1V = trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry = ['銭形', '警部', '日テレ','共同','制作','制作','ビジネス','モデル']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V))

testingNB()