from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("SusyStau")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split()
    StauMass = float(fields[1])
    return (1,StauMass)

lines = sc.textFile("dataset-supersymmetry-1.txt")
stau = lines.map(parseLine)
lighteststau=stau.reduceByKey(lambda x,y: min(x,y))
results = stau.collect()



print "The lighest Stau mass is = " + str(lighteststau.collect()[0][1])+" GeV"

#OutPut: The lighest Stau mass is = 14.8735 GeV
