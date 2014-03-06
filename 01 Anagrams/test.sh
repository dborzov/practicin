#!/bin/bash
time cat ../in/word_corpus.txt| python naive.py > naive.report
echo Now Union Find!
time cat ../in/word_corpus.txt| python union-find.py > union-find.report