from fuzzywuzzy import fuzz, process

def valid_command(command):
    score = fuzz.ratio(command.lower(), "substitute")

    if score >= 80: # check similarity between inputted command and expected command
        return True
    else:
        return None