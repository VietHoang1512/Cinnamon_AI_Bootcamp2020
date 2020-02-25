# Assignment report
## Mentor: Levi
## Name: Phan Viet Hoang


### 1/ My work
- Preprocess [data](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)
- Build a Neural Language Model with LSTM using Keras deep learning framework
- This language model able to generate a paragraph on its own with few input words 


The complete implementation (including dataset and model) can be found [here](https://drive.google.com/drive/folders/1bgMF5qKkEkFlQcilg3q-0Wdi32DETUYP?usp=sharing)

### 2/ Questions:

- How do we use RNN for language modeling?

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

- What is the loss function for training our RNN LM?
Crossentropy will be used like in the case of classifcation tasks because we've added the dense layer on each time step

- How can we evaluate the performance of our LM?



- What factors of RNN affect the performance of our LM? Go into the
details how they affect our LM.

- How can we reduce the information missing problem of RNN in training
our LM? Show their effects on our LM’s performance



### 3/ References:

[1] [Text generation with an RNN](https://www.tensorflow.org/tutorials/text/text_generation?hl=fi)
[] []()
[] []()
[] []()
