from fuzzywuzzy import fuzz, process
  
def search(targets, input, threshold):
    match,score = process.extractOne(input, targets, scorer=fuzz.token_set_ratio) #this is a tuple to access the match and score

    if score >= threshold: # check similarity between input and expected inputs
        return match
    else:
        return None