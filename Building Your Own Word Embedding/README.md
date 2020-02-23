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

#### 2.1/ How does each method take into account the context of each word?
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

#### 2.2/ What property of those mathematical models?
- Low-dimensional embeddings capture huge statistical information

Both Skip-gram and Glove try to leverage word co-occurence statistics, by low-rank approximation to word-word cooccurence probabilities (SVD or neural networks based)
- Low dimensional embeddings work better than high-dimensional ones

The embedding dimensionality of word vectors: neither too small, nor too large. Too few parameters make the model incapable 
of fitting to the signal; too many parameters potentially cause computational resource and memory wasting

- Correlation between semantic relations and directions

These unsupervised model automatically organize concepts and learn implicitly
the relationships between them, as during the training we did not provide any supervised information about them

<p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/52401767/75103512-fc062680-562d-11ea-903b-1b6db512bf8c.png">
</p>

<p align="center"> 
  <em>Figure 4. Words representations in Euclidean space</em>
</p>


#### 2.3/ What are the key distinction between the 2 models: Skip gram and Glove?

- **Skip Gram** : Feed forward **neural network based model** to find word embeddings 

The Skip-gram model takes the input as each word in the corpus, sends them to a hidden layer (embedding layer) and from there it predicts the context words

- **Glove** : based on **matrix factorization** techniques on the word-context matrix 

The number of “contexts” is of course large, since it is essentially combinatorial in size. So then we factorize this matrix to yield a lower-dimensional which can explain most of the variance in the high-dimensional data (SVD based)

### 3/ Mentor's extra questions:
3.1/ How Back propagation through time work?

#### There are 2 main phases in training a vanilla recurrent neural network:
- Feed forward
<p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/52401767/75105954-e3a50480-564b-11ea-9111-25375cd4a0f7.png">
</p>

<p align="center"> 
  <em>Figure 5. Feed forward phase</em>
</p>

where:

  Training data is a corpus of text which is a sequence of words <img src="http://www.sciweavers.org/tex2img.php?eq=x_1%2C%20x_2%2C%20...%2C%20x_n&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0"  border="0" alt="x_1, x_2, ..., x_n" width="104" height="15" />
  
   Feed into RNN-LM; compute output distribution for every step t.
   
   Loss function on step t is cross-entropy between predicted probability
   
   Average this to get overall loss for entire training set: 

<img src="https://user-images.githubusercontent.com/52401767/75106343-32ec3480-564e-11ea-86eb-1f356a13080f.png" align="center"  width="300" height="60" />

-  Backward phase

<p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/52401767/75106506-00433b80-5650-11ea-9398-603b9c8cdaea.png">
</p>

<p align="center"> 
  <em>Figure 6. Back propagation</em>
</p>


3.2/ The problem of gradient descent in RNN?

#### Like the case of mentor's first question, there also exist 2 problems training the RNN:

- Vanishing gradient descent

<p align="center">
  <img width="450" height="300" src="https://user-images.githubusercontent.com/52401767/75106635-3fbe5780-5651-11ea-9096-817078448253.png">
</p>

<p align="center"> 
  <em>Figure 7. Vanishing gradient descent</em>
</p>

- Exploding gradient descent

Conversely, when these figures are large, the gradient get larger and larger as it backpropagate futher

#### Proof:

We already have <img src="https://user-images.githubusercontent.com/52401767/75109202-d12ec900-5653-11ea-8a9d-9094a06d9b30.png" align="center"  width="300" height="60" /> (the current hidden state is a function of the previous one) (*)


On the other hand, performing eigendecomposition on the right hand side matrix, we receive the eigenvalues **λ1,λ2,⋯,λn**
where **|λ1|>|λ2|>⋯>|λn|**

(*) implies that subsequent time steps, will result in scaling the change with a factor equivalent to **λi**.

So we have the sequence **λ1iΔh1, λ2iΔh2, ... λniΔhn**:

- if **λ1>1** it will cause the gradient exploding
- and **λ1<1** will  potentially cause the gradient vanishing



### 4/ References:

[1] [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

[2] [Distributed Representations of Words and Phrases and their Compositionality](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)

[3] [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)

[4] [What is the difference between word2Vec and Glove ?](https://machinelearninginterview.com/topics/natural-language-processing/what-is-the-difference-between-word2vec-and-glove/)

[5] [Word Embeddings: Explaining their properties](https://www.offconvex.org/2016/02/14/word-embeddings-2/)

[6] [CS224n: Natural Language Processing with Deep Learning](http://web.stanford.edu/class/cs224n/)

[7] [Vanishing And Exploding Gradient Problems](https://www.jefkine.com/general/2018/05/21/2018-05-21-vanishing-and-exploding-gradient-problems/)
