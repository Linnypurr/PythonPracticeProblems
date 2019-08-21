import random

class ProblemThreeClass:
    def __init__(self, input_train_file, output_probs_file, input_test_file,
    output_eval_file):
        self.input_train_file = input_train_file
        self.input_test_file = input_test_file
        self.output_probs_file = output_probs_file
        self.output_eval_file = output_eval_file

    def bigram_set_up(self):
        word_dictionary = {}
        word_list = []
        list_for_file = []
        sent_word_list = []
        total_word_count = 0
        laplace_smooth = 0.1

        with open(self.input_train_file) as in_file:
            lines_from_file = in_file.read().splitlines()

        for line_index in lines_from_file:
            if line_index == '':
                continue
                #TODO: IS THIS JUST A WORD? YOURE SLPTTING A LINE INTO A ????
            for word_index in line_index.lower().split():
                word_list.append(word_index)
        # TODO: ALEAST LOOK UP DEFAULT DICT, DONT HAVE TO UES
        # TODO: WORD INDEX?
        # TODO:  CANT WE COMBINE THESE TWO LOOPS?
        for word_index in range(1, len(word_list)):
            if word_list[word_index] not in word_dictionary:
                word_dictionary[word_list[word_index]] = {word_list[word_index - 1] : 1}
            elif word_list[word_index - 1] not in word_dictionary[word_list[word_index]]:
                word_dictionary[word_list[word_index]][word_list[word_index-1]] = 1
            else:
                word_dictionary[word_list[word_index]][word_list[word_index - 1]] += 1
        #TODO: ARE WE SURE THIS IS TO THE TOTAL WORD COUNT? I MEAN YOU HAVE A WORD_LIST right above it, why arent we getting the count from that ?
        total_word_count = len(word_dictionary)

# TODO: DONT SAY KEY, ITS NOT A KEY, ITS A BIGRAM
        for key in word_dictionary:
            for word_index in word_dictionary[key]:
                word_count = len(word_dictionary[key])
                # TODO WHY MIX [] AND .GET()
                word_dictionary[key][word_index] = word_dictionary[key].get(word_index)/word_count

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

# TODO: SEEMS LIKE A SEPARET FUNCTION DOING SOMETHING DIFFERENT THAT THN THE ABOVE STUFF
        with open(self.input_test_file) as in_file:
            lines_from_file = in_file.read().splitlines()[0:100]

        total_word_count = total_word_count * laplace_smooth

        for line_index in lines_from_file:
            if line_index == '':
                continue
            sent_prob = 1
            #TODO list for which file? this is just a new list for a new file? why not have a list for file for lines 52:63
            list_for_file.append(line_index)
            line_index = line_index.lower().split()
            for word in range(1, len(line_index)):
                if line_index[word] in word_dictionary and line_index[word-1] in word_dictionary[line_index[word]]:
                    sent_prob *= word_dictionary[line_index[word]].get(line_index[word-1])

                else:
                    word_prob = laplace_smooth
                    self.update_dictionary(word_dictionary, total_word_count)
                    sent_prob *= word_prob
                    #TODO: DUMB VARIABLE NAME DENOM? no shit its a the denomenator
            denom = pow(sent_prob, 1.0/(len(line_index)+1))
            if denom != 0:
                calc_perplexity = 1/denom
            else:
                calc_perplexity = 0
            list_for_file.append(calc_perplexity)

        with open(self.output_eval_file, "w") as out_file:
            for item in range(1, len(list_for_file), 2):
                #TODO WHY SO MANY WRITES? JUST DO ONE FUCKING STRING AND WRITE THAT
                out_file.write('\"')
                out_file.write(str(list_for_file[item-1]))
                out_file.write('\" Sentence perplexity: ')
                out_file.write(str(list_for_file[item]))
                out_file.write('\n')

#TODO WHAT ARE WE UPDATING IT WITH?
    def update_dictionary(self, word_dictionary, total_word_count):
        laplace_smooth = 0.1
        for key in word_dictionary:
            for word in word_dictionary[key]:
                word_count = len(word_dictionary[key])
                word_dictionary[key][word] = (word_dictionary[key].get(word) + laplace_smooth) /word_count
        return word_dictionary


if __name__ == '__main__':
    problem_3 = ProblemThreeClass('doyle-27.txt', 'smooth_probs.txt', 'doyle-case-27.txt',
    'smoothed_eval.txt')
    problem_3.bigram_set_up()
