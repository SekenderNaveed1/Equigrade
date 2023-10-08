def sub_weighted_avg(weight1, weight2, score1, score2):
    wholePercent = 100
    weight1Percent = weight1 / wholePercent
    weight2Percent = weight2 / wholePercent

    avg1 = score1 / wholePercent
    avg2 = score2 / wholePercent

    weightAvg1 = weight1Percent * avg1
    weightAvg2 = weight2Percent * avg2

    weightSum = weightAvg1 + weightAvg2
    totalWeight = weight1Percent + weight2Percent

    sub_weightAvg = (weightSum / totalWeight) * wholePercent
    return round(sub_weightAvg, 2)

print(sub_weighted_avg(40, 60, 85, 90))
#NOTICE: 0-5 rounds down, 6-9 rounds up