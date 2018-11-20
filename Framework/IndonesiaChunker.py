
# coding: utf-8

# In[1]:


import nltk, re, pprint


# In[ ]:


class IndonesiaChunker:
    grammar = """
        NP: {<NN|NNP>+<CC><NN|NNP|NNG>+}
        NP: {<PRP><CC><NN|NNP|NNG>}
        NP: {<NN|NNP><CC><PRP>}
        NP: {<NN>+<CDO>}
        NP: {<NN>+<JJ>}
        NP: {<NN>+<DT>}
        NP: {<NN>+<PRP>}
        NP: {<NN>+<NNP>+}
        NP: {<NNP>+<NN>+}
        NP: {<CDI|CDP><NN>+<CDI|CDP>*}
        NP: {<CDI|CDP>*<NN>+<CDI|CDP>}
        NP: {<NN>+}
        NP: {<NNP>+}
        NP: {<NNG>}
        NP: {<FW>+}
        NP: {<NP><NP>+}
        NP: {<PRP>}
        NP: {<NP><CDO>}
        NP: {<NP><JJ>}
        NP: {<NP><DT>}
        NP: {<CDI|CDP><NP>}
        NP: {<NP><CC><NP>}
        PP: {<IN><NP>}
        PP: {<IN><NN|NNP|NNG>}
        PP: {<IN><CDP>}
        ADVP: {<IN><JJ>}
        ADJP: {<JJ><CC><JJ>}
        ADJP: {<JJ><RB>}
        ADJP: {<RB><JJ>}
        ADJP: {<JJ>+}
        ADVP: {<RB>}
        NP: {<NP><ADJP>}
        VP: {<NEG>*<VBI><CC><VBI>}
        VP: {<NEG>*<VBT><CC><VBT>}
        VP: {<NEG>*<VBI|VBT>}
        VP: {<NEG>*<VP><NP><PP>}
        VP: {<NEG>*<VP><PP>+}
        VP: {<NEG>*<VP><NP>}
        VP: {<NEG>*<MD><VP>}
        VP: {<NEG>*<VP><IN>*<ADJP>}
        VP: {<NEG>*<ADJP><VP>}
        VP: {<NEG>*<VP><ADVP>}
        VP: {<NEG>*<ADVP><VP>}
        PP: {<IN><VP>}
        PP: {<IN><VBI|VBT>}
    """
    def __init__(self):
        print "Indonesia Chunker Created"
    def stdChunker(self, sentence):
        cp = nltk.RegexpParser(self.grammar)
        result = cp.parse(sentence)
        return result

