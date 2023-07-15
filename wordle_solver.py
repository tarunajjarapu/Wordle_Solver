# Name: Tarun Ajjarapu


class WordleSolver:

    def __init__(self):
        self.__all_words = []
        self.get_words()

    def get_words(self):
        
        with open('all_words_7.txt', 'r') as data_file:
            all_lines = data_file.readlines()
            for line in all_lines:
                self.__all_words.append(line.strip())

    def show_words(self):
        print(len(self.__all_words))
        for word in self.__all_words:
            print(word)

def main():
    wordle = WordleSolver()

if __name__ == '__main__':
    main()