
import cleanup
import pdb

class Dictogram(dict):
    def __init__(self, word_text):
        '''Everytime this dictogram class is instantiated word text is given'''
        self.word_text = word_text


    '''Generates a dictogram given a piece of text'''
    def generate_histogram(self):
        '''This function generates our histogram for us'''
        word_frequency = {}
        cleaned_text = cleanup.clean_given_text(self.word_text)[:100]
        for word in cleaned_text:
            word_occurences = cleaned_text.count(word)
            word_frequency[word] = word_occurences
        return word_frequency


    def generate_histogram_weights(self):
        #This function essentially generates the weights or the relative occurence of the words in the histogram
        weight_dictionary = {}
        sum_values = sum(self.generate_histogram().values())
        cleaned_text = cleanup.clean_given_text(self.word_text)
        for word in cleaned_text:
            word_occurences = self.word_text.count(word)
            weighted_occurences = word_occurences / sum_values
            weight_dictionary[word] = weighted_occurences
        return weight_dictionary

    def generate_specific_frequency_of_word(self, user_inputted_word):
        specific_word_frequency = {}
        user_inputted_word = str(input())
        cleaned_text = cleanup.clean_given_text(self.word_text)
        if user_inputted_word in cleaned_text:
            specific_word_occurence = cleaned_text.count(user_inputted_word)
            specific_word_frequency[user_inputted_word] = specific_word_occurence
        return specific_word_frequency


dictogram = Dictogram("robert_greene.txt")
print(dictogram.generate_histogram_weights())