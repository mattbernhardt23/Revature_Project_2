from pathlib import Path
from pyspark import SparkContext, SparkConf

def load():
    conf = SparkConf().setAppName("Load").setMaster("local")

    sc = SparkContext(conf = conf)
    path = Path(__file__).parent / "../data/data_team_3.csv"
    
    data_team_3_rdd = sc.textFile(path.as_uri)

    return data_team_3_rdd.map(lambda x: x.split(','))