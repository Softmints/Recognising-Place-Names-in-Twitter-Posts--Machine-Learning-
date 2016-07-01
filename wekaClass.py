import weka.core.jvm as jvm
import joinStrip

tempList = list()

jvm.start()

data_dir = "C:\Users\Softmints\Desktop\Diss\Code\WEKA"

from weka.core.converters import Loader
#Prepare ARFF Loader
loader = Loader(classname="weka.core.converters.ArffLoader")
#Assign ands load ARFF data file
data = loader.load_file(data_dir + "\TestDataEleventoTwentyTwo.arff")
data.class_is_last()

from weka.classifiers import Classifier
#Classify data using J48 classifer
cls = Classifier(classname="weka.classifiers.trees.J48", options=["-C", "0.3"])
cls.build_classifier(data)

for index, inst in enumerate(data):
	#Output predicition and distribution
    pred = cls.classify_instance(inst)
    dist = cls.distribution_for_instance(inst)
    print(str(index) + ": label index=" + str(pred) + ", class distribution=" + str(dist))
    
    if str(pred) == "0.0":
    	tempList.append(str(index))

print tempList

jvm.stop()