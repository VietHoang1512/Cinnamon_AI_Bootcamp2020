# Assignment report
## Mentor: Levi
## Name: Phan Viet Hoang


### 1/ My work
- Preprocess [data](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)
- Build a Neural Language Model with LSTM using Keras deep learning framework
- This language model able to generate a paragraph on its own with few input words 


The complete implementation (including dataset and model) can be found [here](https://drive.google.com/drive/folders/1bgMF5qKkEkFlQcilg3q-0Wdi32DETUYP?usp=sharing)

### 2/ Questions:

#### How do we use RNN for language modeling?

- My approach is slicing the input text into sequence of characters. Given a bunch of sequences RNN will be trained to predict 
    the output-the following character at each time step.
- Traditional RNN's architecture (and also others advanced versions) is perfect for modelling languages because 
    language is a sequence of words and each next word is dependent on the words that come before it, 
    since RNNs can maintain an internal state that depends on the previously seen elements
- For each input sequence, the corresponding targets contain the same length of text, except shifted one character to the right.

This is how my model look alike
<p align="center">
  <img width="800" height="300" src="https://user-images.githubusercontent.com/52401767/75263867-20762480-5821-11ea-9cd7-ee7a59c46372.png">
</p>

<p align="center"> 
  <em>Figure 1. RNN language model</em>
</p>

#### What is the loss function for training our RNN LM? How can we evaluate the performance of our LM?
- Crossentropy will be used like in the case of classifcation tasks because we've added the dense layer on each time step
- Metric for  the quality of generated text in my assigment is [BLEU score](https://en.wikipedia.org/wiki/BLEU)

#### What factors of RNN affect the performance of our LM? Go into the details how they affect our LM.
- RNN's performance in capturing long term dependencies: advanced architectures seems to be better choice than the vanilla one thanks to update gate (GRU) and both update gate and a forget gate (LSTM) 
    
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/52401767/75311085-4be02a00-5888-11ea-8269-ad3dfac4ed4b.png">
</p>

<p align="center"> 
  <em>Figure 2. GRU and LSTM</em>
</p>
    
- Number of hidden unit: this is a measure for learning capacity of a neural network,
  it reflects the number of learned parameters. The bigger it is, the more complex model
    
<p align="center">
<img width="500" height="300" src="https://user-images.githubusercontent.com/52401767/75310871-9c0abc80-5887-11ea-9fff-11688f8513f4.png">
</p>

<p align="center"> 
<em>Figure 3. LSTM and number hidden unit</em>
</p>

#### How can we reduce the information missing problem of RNN in training our LM? Show their effects on our LM’s performance:
![1_TTmYy7Sy8uUXxUXfzmoKbA](https://user-images.githubusercontent.com/52401767/75311575-cf4e4b00-5889-11ea-9587-05f03b0f70ed.gif)

We can try other advanced RNN model and compare their performance (just replace one layer and retain not only model architecture but also hyperparameters combination):

- Traditional RNN
- LSTM
- GRU

##### (The detailed comparision is presented in python notebook file)

### 3/ References:

[1] [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation?hl=fi)
[2] [Hướng dẫn chi tiết về cơ chế của LSTM và GRU trong NLP](https://blog.chappiebot.com/h%C6%B0%E1%BB%9Bng-d%E1%BA%ABn-chi-ti%E1%BA%BFt-v%E1%BB%81-c%C6%A1-ch%E1%BA%BF-c%E1%BB%A7a-lstm-v%C3%A0-gru-trong-nlp-a1bd9346b209)
[3] [CS224n: Natural Language Processing with Deep Learning](http://web.stanford.edu/class/cs224n/)

