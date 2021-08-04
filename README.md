# spark_jobs
default structured streaming job for apache spark

# Requirements
 - Linux (I used ubuntu on digital Ocean)
 - tmux (my favorite terminal multiplexer tool and is pretty cool)
 -  java 
 -  kafka
 -  spark
 -  python > 3.6
 -  Patience ( Welcome to the world of deprecated imports and utils yoh!)
 
# Steps to reproduce

Beware of deprecated methods in spark >2.* so if you use it you cannot access structured streaming.

1)Brew Coffee , Lots of it
2)install java
3) install kafka
4) install spark
5) install pyspark
6) start kafka
7) start spark
8) proceed to spark conf folder 
    - copy log.properties.default to log.properties
    - remove INFO with WARN (This one really pissed me off , logs kept streaming and I couldnt find my outputs)
9)create a python folder
10)add the py_spark.py and save
11)Ensure you have netcat installed then run nc -l 9999
12)use spark_submit found in /spark_installation_path/bin/spark_submit
    - use the following command  /spark_installation_path/bin/spark_submit  /python_script_job_path/spark_job.py localhost 9999
    
 ## Output

![alt text](https://github.com/davidmungai/spark_jobs/blob/main/Capture.PNG?raw=true)

## Spark running jobs
![alt text](https://github.com/davidmungai/spark_jobs/blob/main/Capture2.PNG?raw=true)
