#this program calculates the mass of the lightest particle (stau) in the dataset "dataset-supersymmetry-1.txt"

from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("SusyStau")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split()
    StauMass = float(fields[1])
    return (1,StauMass)    

lines = sc.textFile("dataset-supersymmetry-1.txt")
stau = lines.map(parseLine)     #gives the mass as a list key-value pairs
lighteststau=stau.reduceByKey(lambda x,y: min(x,y))       #find the minimum value
results = stau.collect()



print "The lighest Stau mass is = " + str(lighteststau.collect()[0][1])+" GeV"

#OutPut: The lighest Stau mass is = 14.8735 GeV
