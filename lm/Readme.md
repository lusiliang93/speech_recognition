Scripts:
1) combine.py

Function:

• Compile all train files or test files together

Results:

•	heldout_plain.txt

•	train_plain.txt

2) chinese_sw.py

   english_sw.py

Function:

•	generate separate English and Chinese document for L1 and L2 according to the paper

•	generate switch pairs 

Results:

•	english_train.txt

•	chinese_train.txt

•	chinese_heldout.txt

•	englisth_heldout.txt

•	switch (train)

•	switch1 (test)

•	switch_chn (train)

•	switch1_chn (test)

3)  ngram-count -text english_train.txt -lm eng.lm -kndiscount3 -order 2

    ngram-count -text chinese_train.txt -lm chn.lm -kndiscount3 -order 2

Function:

•	generate english or Chinese model with SRILM

Results:

•	eng.lm

•	chn.lm

4) clean_lm.py

Function:

•	generate cleaned bi-grams without code-switching

Results:

•	cleaned_eng.lm

•	cleaned_chn.lm

5) preprocess.ipynb

Function:

•	generate bigram with code-switching from English language model eng.lm and Chinese language model chn.lm

Results:

•	eng_sw.txt

•	sw_eng.txt

•	chn_sw.txt

•	sw_chn.txt

6) eng_chn.py

   chn_eng.py

Function:

•	generate bigrams with code-switching to replace ‘<sw>’
	
Results：

•	eng_chn.txt

•	chn_eng.txt

7) Compile all the files eng_chn.txt, chn_eng.txt, cleaned_eng.lm and cleaned_chn.lm together to generate the dual language model dlm.lm:

Middle results:

•	bi_eng.lm

•	bi_chn.lm

•	uni_eng.lm

•	uni_chn.lm

Final result:

•	dlm.lm


