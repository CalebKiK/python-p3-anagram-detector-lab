# your code goes here!

class Anagram:
    def __init__(self, anagram_word):
        self._anagram_word = anagram_word
        
    def match(self, word_list):
        anagram_list = []
        
        self.word_list = word_list
        for word in self.word_list:
            each_letter_possible_word = [letter for letter in word]
            each_letter_anagram_word = [letter for letter in self._anagram_word]
            if sorted(each_letter_possible_word) == sorted(each_letter_anagram_word):
                anagram_list.append(word)
        
        return anagram_list
            

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))