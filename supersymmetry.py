#this program calculates the mass of the lightest particle (stau) in the dataset "dataset-supersymmetry-1.txt"

from pyspark import SparkConf, SparkContext
import collections

#to use all the cores of your computer replace local by local[*]

conf = SparkConf().setMaster("local").setAppName("SusyStau")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split()
    StauMass = float(fields[1])
    return (1,StauMass)     # returns the mass of the stau as the value in the key value pair with key as 1

lines = sc.textFile("dataset-supersymmetry-full.txt")
stau = lines.map(parseLine)
lighteststau=stau.reduceByKey(lambda x,y: min(x,y))
results = stau.collect()


print "The lighest Stau mass is = " + str(lighteststau.collect()[0][1])+" GeV"

#OutPut: The lighest Stau mass is = 14.8735 GeV
