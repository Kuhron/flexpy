import math

# Kris's library
from corpus_toolkit import corpus_tools as ct

from flexpy.Corpus import Corpus
from flexpy.Text import Text


def get_form_group_text_only(wordform):
    return wordform.text


def get_form_group_first2(wordform):
    # test function: first two letters of token
    return wordform.text[:2]


def get_form_group_last2(wordform):
    # test function: last two letters of token
    return wordform.text[-2:]


# has problems with some wordforms having more than one root pos, e.g. {"Verb", None}
# this is a problem with how the data is labeled, need to clean up word classes if use this
# def get_form_group_pos(wordform):
#     return wordform.get_root_pos()


def get_form_group_last_morpheme(wordform):
    morph_type = wordform.morph_types[-1]
    form = wordform.forms[-1]
    if form is None:
        return "None"
    elif morph_type in [None, "None"]:
        return "None"
    elif morph_type in ["root", "stem"]:
        form_notation = form
    elif morph_type == "bound root":
        form_notation = "*" + form
    elif morph_type == "suffix":
        form_notation = "-" + form
    elif morph_type == "prefix":
        form_notation = form + "-"
    elif morph_type == "enclitic":
        form_notation = "=" + form
    elif morph_type == "proclitic":
        form_notation = form + "="
    else:
        raise Exception("unknown morph type: {}".format(morph_type))
    gloss = wordform.glosses[-1]
    return "{} ({})".format(form_notation, gloss)


def get_form_group_last_morpheme_form(wordform):
    return wordform.forms[-1]


def get_form_group_last_morpheme_gloss(wordform):
    return wordform.glosses[-1]


def group_wordforms(tokenized, grouping_function):
    new_tokenized = []
    for text in tokenized:
        new_text = group_wordforms_in_text(text, grouping_function)
        new_tokenized.append(new_text)
    return new_tokenized


def group_wordforms_in_text(text, grouping_function):
    new_text = []
    for token in text:
        new_token = grouping_function(token)
        new_text.append(new_token)
    return new_text


# this function is copied directly from https://github.com/kristopherkyle/corpus_toolkit/blob/b5f0eba13dee60a0b56a25c5f3f900fe7c8c8cb4/build/lib/corpus_toolkit/corpus_tools.py
# and then modified for the sake of me being able to turn in the assignment sooner
def modified_collocator(
        corpus_in_target_terms,
        corpus_in_collocate_terms,
        target, left=4,right=4, stat="MI", cutoff=5, ignore=None,
        ): #returns a dictionary of collocation values
    # "in target terms" means the items in the corpus are converted
    # - in such a way that certain targets are treated the same
    # - e.g. you want to see which words correlate most with any verb
    # - so you modify the corpus to replace all verbs with "V", and that is 
    # - the corpus_in_target_terms argument
    # "in collocate terms" means the items in the corpus are converted
    # - in such a way that the collocates may be grouped similarly
    # - so in the "what collocates with any verb" analysis
    # - you may want all target verbs to be treated the same,
    # - but not all collocate verbs; you want the collocate verbs to retain their form
    # the target param is, of course, in target terms

    if ignore is None:  # no mutable default args
        ignore = []

    def corpus_iterator(corpus):
        for x in corpus:
            yield x

    # corpus, freq_corp = itertools.tee(corpus) #this makes two versions of the iterator so that it can be processed twice
    corp_freq_target_terms = ct.frequency(corpus_iterator(corpus_in_target_terms)) #use the frequency function to create frequency list
    corp_freq_colloc_terms = ct.frequency(corpus_iterator(corpus_in_collocate_terms))

    # these are number of TOKENS, not number of types (the values in the dict are counts of each type)
    nwords_target_terms = sum(corp_freq_target_terms.values()) #get corpus size for statistical calculations
    nwords_colloc_terms = sum(corp_freq_colloc_terms.values())
    assert nwords_target_terms == nwords_colloc_terms
    nwords = nwords_target_terms

    collocate_freq = {} #empty dictionary for storing collocation frequencies
    r_freq = {} #for hits to the right
    l_freq = {}  #for hits to the left
    stat_dict = {} #for storing the values for whichever stat was used
    
    def freq(l,d): #this takes a list (l) and a dictionary (d) as arguments
        for x in l: #for x in list
            if x in ignore:
                continue
            if x not in d: #if x not in dictionary
                d[x] = 1 #create new entry
            else: #else: add one to entry
                d[x] += 1
    
    #begin collocation frequency analysis
    for text_in_target_terms, text_in_colloc_terms in zip(corpus_in_target_terms, corpus_in_collocate_terms):
        assert len(text_in_target_terms) == len(text_in_colloc_terms)
        if target not in text_in_target_terms: #if target not in the text, don't search it for other words
            continue
        else:
            last_index = len(text_in_target_terms) -1 #get last index number
            for i in range(len(text_in_target_terms)):
                word_in_target_terms = text_in_target_terms[i]
                word_in_colloc_terms = text_in_colloc_terms[i]
                if word_in_target_terms == target:
                    start = i-left #beginning of left span
                    end = i + right + 1 #end of right span. Note, we have to add 1 because of the way that slices work in python
                    if start < 0: #if the left span goes beyond the text
                        start = 0 #start at the first word
                    #words to the right
                    lspan_list = text_in_colloc_terms[start:i] #for counting words on right
                    freq(lspan_list,l_freq) #update l_freq dictionary
                    freq(lspan_list,collocate_freq) #update collocate_freq dictionary
                    
                    rspan_list = text_in_colloc_terms[i+1:end] #for counting words on left. Note, have to add +1 to ignore node word
                    freq(rspan_list,r_freq) #update r_freq dictionary
                    freq(rspan_list,collocate_freq) #update collocate_freq dictionary
    
    #begin collocation stat calculation

    for x in collocate_freq:
        observed = collocate_freq[x]
        if observed < cutoff: #if the collocate frequency doesn't meet the cutoff, ignore it
            continue
        else:
            # TODO: this way of comparing frequencies among different form groupings might not be statistically sound
            expected = (corp_freq_target_terms[target] * corp_freq_colloc_terms[x])/nwords #expected = (frequency of target word (in entire corpus) * frequency of collocate (in entire corpus)) / number of words in corpus

            if stat == "MI": #pointwise mutual information
                mi_score = math.log2(observed/expected) #log base 2 of observed co-occurence/expected co-occurence
                stat_dict[x] = mi_score
            elif stat == "T": #t-score
                t_score = math.log2((observed - expected)/math.sqrt(expected))
                stat_dict[x] = t_score
            elif stat == "freq":
                stat_dict[x] = collocate_freq[x]
            elif stat == "right": #right frequency
                if x in r_freq:
                    stat_dict[x] = r_freq[x] 
            elif stat == "left":
                if x in l_freq:
                    stat_dict[x] = l_freq[x]
                
    return(stat_dict) #return stat dict


def report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms):
    words_of_interest = ["aji", "ni", "andu"]
    metrics = ["MI", "T"]
    for word in words_of_interest:
        for metric in metrics:
            collocates = modified_collocator(
                corpus_in_target_terms,
                corpus_in_collocate_terms,
                word, left=4, right=4, stat=metric, cutoff=5, ignore=[]
            )
            print("----\nCollocations for {} using stat={}:".format(word, metric))
            ct.head(collocates, hits=10)


if __name__ == "__main__":
    project_name = "Bongu"
    project_dir = "/home/wesley/.local/share/fieldworks/Projects/"
    corpus = Corpus(project_dir, project_name)
    # print("\n-- all texts in corpus:")
    # for text in corpus.texts:
    #     print(text)

    texts_to_omit = [None, "None", "*Nouns", "*Ungram.", "*Random", "*Verbs"]
    wordform_contents = corpus.get_wordform_contents(
        texts_separated=True,
        paragraphs_separated=False,
        texts_to_omit=texts_to_omit,
    )
    # print(wordform_contents)

    # test grouping functions
    target_grouping_function = get_form_group_text_only
    grouping_functions = [
        # get_form_group_first2,
        # get_form_group_last2,
        get_form_group_last_morpheme,
        # get_form_group_last_morpheme_gloss,
        # get_form_group_last_morpheme_form,
    ]
    for grouping_function in grouping_functions:
        corpus_in_target_terms = group_wordforms(wordform_contents, target_grouping_function)
        corpus_in_collocate_terms = group_wordforms(wordform_contents, grouping_function)
        print("\n-- reporting pronoun collocations")
        report_pronoun_collocations(corpus_in_target_terms, corpus_in_collocate_terms)
