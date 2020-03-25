def main():
    #initial array of words
    arr = ["the", "floor", "plan", "has", "a", "plan", "for", "everyone", "in", "the", "floor", "floor", "the"]
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
    #creating a list to hold all max words
    all_max_words= []
    #finding the maximum amount of times a word has occured
    maxOccurance = max(word_counter, key = word_counter.get)
    #finding the word with the most occurances, although this will only find me one word
    #and there may be more words that share the same amount of occurances
    maxWord = (max(word_counter, key=word_counter.get))
    #adding the most occuring word in to list
    all_max_words.append(maxWord)
    #finding how many times it occured
    maxOccurance = word_counter.get(maxWord)
   #looping through dictionary and finding other words with occurances equal to the max word
   #this is finding words that have occured the same amount of times as our "max" and adding
   #them to the all max word list as long as the word isn't the original one
    for word in word_counter:
        if word_counter[word] == maxOccurance and word != maxWord:
            all_max_words.append(word)
    print(all_max_words)
    
    
    
        
if __name__ == '__main__':
	main()