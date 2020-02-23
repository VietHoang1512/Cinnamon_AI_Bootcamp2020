# Assignment report
## Mentor: Levi
## Name: Phan Viet Hoang


### 1/ My work
- Data Gathering and extracting text from HTML, XML
  - [Wikidump](https://dumps.wikimedia.org/backup-index.html)
  - [Cornell Movie Dialog Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)
- Text preprocessing
  - Word tokenize
  - Remove noisy characters
  - Lower case and lematize
- Implement Glove and Skip-gram models
- Visualize the the embedded words using  Tensorboard

The complete implementation (including dataset and model) can be found [here](https://drive.google.com/drive/folders/1bgMF5qKkEkFlQcilg3q-0Wdi32DETUYP?usp=sharing)

### 2/ Questions:

##### 2.1/ How does each method take into account the context of each word?
- **Bag of words** (sklearn's countvectorizer in my case) discards grammar, word order and **ignores the context**, each sentence or document is  represented as the set of its words, considering each word count as a feature (this also cause a fact that there exist some words which are presumed to be uninformative but have high frequency on represent vector). Any others information about the **order or structure of words** in the document is **disregarding**. The model is only concerned with whether specific words occur in the document, not where in the document.

<p align="center">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/52401767/75102560-03263800-5620-11ea-85a7-9aab465a42e4.jpg">
</p>

<p align="center"> 
  <em>Figure 1. Bag-of-words</em>
</p>



- **Skip Gram** model is an efficient method for learning vector representations that **capture** a large 
number of **precise syntactic and semantic word relationships**. Moreover, , many of these learned
vectors can be represented as linear translations. For example, the result of a vector calculation 
vec(“Madrid”) - vec(“Spain”) + vec(“France”) is closer to vec(“Paris”) than to any other word vector. This architecture's aim is to predict the context from the target word

<p align="center">
  <img width="240" height="300" src="https://user-images.githubusercontent.com/52401767/75102525-85fac300-561f-11ea-837a-b3b1ef4964cc.png">
</p>

<p align="center"> 
  <em>Figure 2. Skip-gram</em>
</p>

- **Glove** is another efficient word embedding method, in which ratios of word-word co-occurrence probabilities have the potential for encoding some form of meaning.
This ratio is defined as:

<p align="center">
  <img width="1500" height="150" src="https://user-images.githubusercontent.com/52401767/75102723-b728c280-5622-11ea-9900-d8166cc3faf9.jpg">
</p>

<p align="center"> 
  <em>Figure 3. Ratio of co-occurrence probabilities</em>
</p>

This ratio gives us hints on the relations between three different words. If the ratio is large, the probe word is related to wᵢ but not wⱼ. Intuitively, we are maintaining the **relationship** among all these embedding vectors

##### 2.2/ What property of those mathematical models?

##### 2.3/ What are the key distinction between the 2 models: Skip gram and Glove?

### 3/ Mentor's extra questions:
- How BPTT work?
- The problem of gradient descent in RNN?
