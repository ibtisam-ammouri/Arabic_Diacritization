import re
import pickle 

in_file = r"C:\Users\ibtis\Documents\Dissertation_Local\Git_Repo\Bin_Data\big-harakat-arabic-sentences-list"

with open (in_file, "rb") as f:
    arabic_target_sentences_list = pickle.load(f)

for sent in arabic_target_sentences_list:
    for word in sent:
        ind = sent.index(word)
        has_harakat = re.search(r'[\u064B-\u0652\u0670]+', word)
        if not has_harakat:
            sent[ind] = '0'
        else:
            sent[ind] = ' '.join(map(str, [ord(char) for char in re.sub(r'[\u0600-\u064A]+', '', word)]))

#print ("Check samples: ", arabic_target_sentences_list[12:20])