sentence = "What is the Airspeed Velocity of the Unladen Swallow?"

sentenceList = sentence.split()
result = {word:len(word) for word in sentenceList}
print(result)