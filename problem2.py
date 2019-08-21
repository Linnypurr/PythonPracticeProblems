import random

class ProblemTwoClass:
    def __init__(self, input_train_file, output_probs_file, input_test_file,
    output_eval_file):
        self.input_train_file = input_train_file
        self.input_test_file = input_test_file
        self.output_probs_file = output_probs_file
        self.output_eval_file = output_eval_file

    def bigram_set_up(self):
        word_dictionary = {}
        word_list = []
        total_word_count = 0
        sent_word_list = []
        list_for_file = []

        with open(self.input_train_file) as in_file:
            lines_from_file = in_file.read().splitlines()

        for line in lines_from_file:
            if line == '':
                continue
            for word in line.lower().split():
                word_list.append(word)


        for word in range(1, len(word_list)):
            if word_list[word] not in word_dictionary:
                word_dictionary[word_list[word]] = {word_list[word - 1] : 1}
            elif word_list[word - 1] not in word_dictionary[word_list[word]]:
                word_dictionary[word_list[word]][word_list[word-1]] = 1
            else:
                word_dictionary[word_list[word]][word_list[word - 1]] += 1

        total_word_count = len(word_dictionary)

        for key in word_dictionary:
            for word in word_dictionary[key]:
                word_count = len(word_dictionary[key])
                word_dictionary[key][word] = word_dictionary[key].get(word)/word_count

        # print(word_dictionary)
        bigram_list = list(word_dictionary)
        random_bigram_list = random.sample(bigram_list, 100)

        with open(self.output_probs_file, "w") as out_file:
            for key in random_bigram_list:
                out_file.write('P(')
                out_file.write(str(key))
                out_file.write('|')
                values_list = list(word_dictionary[key])
                rand_index = random.randint(0, len(values_list) - 1)
                out_file.write(values_list[rand_index])
                out_file.write(') = ')
                out_file.write(str(word_dictionary[key][values_list[rand_index]]))
                out_file.write('\n')

        with open(self.input_test_file) as in_file:
            lines_from_file = in_file.read().splitlines()[0:100]

        for line in lines_from_file:
            sent_prob = 1
            if line == '':
                continue
            list_for_file.append(line)
            line = line.lower().split()
            for word in range(1, len(line)):
                if line[word] in word_dictionary and line[word-1] in word_dictionary[line[word]]:
                    sent_prob *= word_dictionary[line[word]].get(line[word-1])
                else:
                    sent_prob *= 0
            denom = pow(sent_prob, 1.0/(len(line)+1))
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
    problem_2 = ProblemTwoClass('doyle-27.txt', 'bigram_probs.txt', 'doyle-case-27.txt',
    'bigram_eval.txt')
    problem_2.bigram_set_up()
