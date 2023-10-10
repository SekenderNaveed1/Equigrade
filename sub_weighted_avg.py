def weighted_avg(weights, scores):
    wholePercent = 100
    
    weights_percent = [] #weights convert percent
    for w in weights:
        weights_percent.append(w / wholePercent)
    
    scores_percent = [] #scores convert percent
    for s in scores:
        scores_percent.append(s / wholePercent)
    
    # Calculate weighted averages and total weight
    weighted_avgs = []
    lenght = len(weights_percent)
    for i in range(lenght):
        weighted_avgs.append(weights_percent[i] * scores_percent[i])
    
    total_weight = sum(weights_percent)
    
    # Calculate the final weighted average
    final_weighted_avg = sum(weighted_avgs) * wholePercent
    return final_weighted_avg
