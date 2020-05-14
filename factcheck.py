import spacy
from nltk import Tree

nlp = spacy.load('en_core_web_sm')
doc = nlp("""Kustomer, which has raised more than $170 million and is now valued at $710 million (per PitchBook), said it is not disclosing the financial terms of the deal.""")

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
