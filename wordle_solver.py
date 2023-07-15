# Name: Tarun Ajjarapu

class WordleSolver:

    def __init__(self):
        self.__all_words = []
        self.get_words()

    def get_guess(self, feedback):
        """
        Make a guess for the current round of Wordle.
        :param feedback: A list of strings representing the guesses so far
        and the feedback for those guesses in the current game of Wordle.
        If feedback is empty then this is the first guess.
        The order of the elements of feedback is [feedback_1, guess_1,
        feedback_2, guess_2, ...]
        All strings are length 7.
        The feedback strings consist of G, O, and -.
        G for GREEN, correct letter in correct spot.
        O for letter in word but not in right spot.
        - for letter not in word.
        :return: A string that is in __all_words and is the next guess.
        """
        current_words = self.__all_words
        feedback_count = 0
        guess_count = 1
        while feedback_count < len(feedback):
            next_words = []
            feedback_val = feedback[feedback_count]
            guess = feedback[guess_count].lower()
            if feedback_val == 'GGGGGGG':
                return guess.lower()
            for word in current_words:
                curr = list(word)
                index = 0
                matches = True
                while matches and index < 7:
                    if guess == word:
                        matches = False
                    elif feedback_val[index] == 'G':
                        if guess[index] != word[index]:
                            matches = False
                        else:
                            curr.remove(guess[index])
                    index += 1
                index = 0
                while matches and index < 7:
                    if feedback_val[index] == 'O':
                        if guess[index] == word[index]:
                            matches = False
                        elif guess[index] not in curr:
                            matches = False
                        else:
                            curr.remove(guess[index])
                    index += 1
                index = 0
                while matches and index < 7:
                    if feedback_val[index] == '-':
                        if guess[index] in curr:
                            matches = False
                    index += 1
                if matches:
                    next_words.append(word)
            current_words = next_words
            feedback_count += 2
            guess_count += 2
        if feedback_count == 0:
            return 'NASTIER'
        max_val = 0
        res = current_words[0]
        for word in current_words:
            total_val = self.word_value(set(word))
            if total_val > max_val:
                max_val = total_val
                res = word
        return res.lower()

    def word_value(self, word):
        """
        This function determines the value of the word based on the weight
        :param word: a set of a word to be used for comparison
        :return: a double value for the total weight of the word
        """
        word_freq = [8.5, 1.97, 4.62, 3.39, 11.16, 1.96, 2.48, 2.57, 7.54,
                     0.05, 1.29, 5.48, 2.78, 6.65, 7.16, 2.8, 0.04, 7.58, 5.73,
                     6.95, 3.63, 0.99, 1.73, 0.15, 1.9, 0.07]
        total = 0
        for curr in word:
            total += word_freq[ord(curr) - ord('a')] * 7
        return total

    def get_words(self):
        """ Read the words from the dictionary file and place them
        in the __all_words instance variable.
        We assume the  required files are in the current working directory
        and is named all_words_5.txt. We also assume all words are
        seven letters long, one word per line.
        Returns a set of strings with all the words from the file.
        """
        with open('all_words_7.txt', 'r') as data_file:
            all_lines = data_file.readlines()
            for line in all_lines:
                self.__all_words.append(line.strip())

    def show_words(self):
        """
        Debugging method to check file was read in correctly.
        :return: None
        """
        print(len(self.__all_words))
        for word in self.__all_words:
            print(word)

def main():
    wordle = WordleSolver()

if __name__ == '__main__':
    main()