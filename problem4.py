# Question #4:
# use dataset above
# 1. get the average engagement rate, only count those data with > 0 engagements
# 2. group the data into nano, micro, macro and celebrity influencers
# nano followers > 100 < 200
# micro followers > 201 < 5000
# macro followers > 5001 < 50000
# celebrity followers > 50001 and more
# undetermined below 100

# Identify how many are nano, micro, macro and celebrity
# 3. What is the average followers of the nanos
# 4. What is the average followers of the micros
# 5. What is the average followers of the macros
# 6. What is the average followers of the celebrities
# 7. What is the average followers of the undetermined

import pandas
import numpy as np

# GET CSV CONTENT #

influencers = pandas.read_csv('crawl_result.csv')

# GET AVERAGE FUNCTION #
def getTotalAverage(data):
    total = 0.0
    count = 0

    for i in data:
        if i > 0 and i != "inf":
            count += 1
            total += i

    return total/count

def groupByFollowers(data):
    result = {
        'nano': {"count": 0, "followers": 0}, 
        'micro': {"count": 0, "followers": 0}, 
        'macro': {"count": 0, "followers": 0}, 
        'celebrity': {"count": 0, "followers": 0}, 
        'undetermined': {"count": 0, "followers": 0}
        }

    for i in data:
        if i >= 100 and i <= 200:
            result['nano']['count'] += 1
            result['nano']['followers'] += i
        elif i >= 201 and i <= 5000:
            result['micro']['count'] += 1
            result['micro']['followers'] += i
        elif i >= 5001 and i <= 50000:
            result['macro']['count'] += 1
            result['macro']['followers'] += i
        elif i >= 50001:
            result['celebrity']['count'] += 1
            result['celebrity']['followers'] += i
        else:
            result['undetermined']['count'] += 1
            result['undetermined']['followers'] += i

    return result

grouped = groupByFollowers(influencers['followers'])
for g in grouped:
    print("Total number of {} influencers: {}".format(g, grouped[g]['count']) )
    print("Average followers of {} influencers: {}".format(g, grouped[g]['followers']/grouped[g]['count']) )
    print("=================================")


print("Total Average Engagement Rate: {}".format(getTotalAverage(influencers['est_er'].replace([np.inf, -np.inf], np.nan)))) 
