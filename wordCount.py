def main():
    #initial array of words
    arr = ["the", "floor", "plan", "has", "a", "plan", "for", "everyone", "in", "the", "floor"]
    #sorting array
    arr.sort()
    #initializing a dictionary for words and their occurance
    word_counter = {}

    #looping through the array, if the word exists in the counter we add one
    #if not we start it at one
    for word in arr:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    
    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
    print(word_counter)
    
    
    
        
if __name__ == '__main__':
	main()