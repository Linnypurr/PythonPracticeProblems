class ProblemOneClass:
    def __init__(self, input_train_file, output_probs_file, input_test_file,
    output_eval_file):
        self.input_train_file = input_train_file
        self.input_test_file = input_test_file
        self.output_probs_file = output_probs_file
        self.output_eval_file = output_eval_file

    def unigram_set_up(self):
        word_dictionary = {}
        total_word_count = 0
        list_for_file = []

        with open(self.input_train_file) as in_file:
            lines_from_file = in_file.read().splitlines()

        for line in lines_from_file:
            if line == '':
                continue
            for word in line.lower().split():
                word_dictionary[word] = word_dictionary.get(word, 0) + 1

        total_word_count = len(word_dictionary)

        for key in word_dictionary:
            word_dictionary[key] = word_dictionary.get(key) / total_word_count

        with open(self.output_probs_file, "w") as out_file:
            for key in word_dictionary:
                out_file.write('P(')
                out_file.write(str(key))
                out_file.write(') = ')
                out_file.write(str(word_dictionary[key]))
                out_file.write('\n')

        with open(self.input_test_file) as in_file:
            lines_from_file = in_file.read().splitlines()[0:100]

        for line in lines_from_file:
            if line == '':
                continue
            sent_prob = 1
            list_for_file.append(line)
            for word in line.lower().split(" "):
                if word in word_dictionary:
                    sent_prob *= word_dictionary[word]
            denom = pow(sent_prob, 1.0/len(line))
            if denom != 0:
                calc_perplexity = 1/ denom
            else:
                calc_perplexity = 0
            list_for_file.append(calc_perplexity)

        with open(self.output_eval_file, "w") as out_file:
            for item in range(1, len(list_for_file), 2):
                out_file.write('\"')
                out_file.write(str(list_for_file[item-1]))
                out_file.write('\" Sentence perplexity: ')
                out_file.write(str(list_for_file[item]))
                out_file.write('\n')

if __name__ == '__main__':
    problem_1 = ProblemOneClass('doyle-27.txt', 'unigram_probs.txt', 'doyle-case-27.txt'
    ,'unigram_eval.txt')
    problem_1.unigram_set_up()
