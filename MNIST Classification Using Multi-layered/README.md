# Assignment report
## Mentor: Nathan
## Name: Phan Viet Hoang

### 1/ My work
- Derive the gradient formula for each weight set in each layer.
- Use it and implement the back propagation and use it to train the network
with the experiments enumerated below.
 - Split MNIST into training and testset by the ratio of 8 : 2
 - Experiment with different hidden dimmension (number of hidden units):
20, 50, 100.
 - Experiment with different epochs: 20, 50, 100.
 - Experiment with different input scaling: 0-to-1, 0-to-255, etc.
 - Experiment with different learning rate: 0.1, 0.001, etc.
 - Experiment with different momentumn factors: 0.9, 0.8, 0.1, 0.0
 
### 2/ Report
####  2.1/ How does the number of hidden units affect the training
- Number of hidden units rise also increase model's accuracy (more parameters to learn and extract features)
but it also reduce the training speed

![hs](https://user-images.githubusercontent.com/52401767/74319983-6e674300-4db2-11ea-97cd-60ad6cac6ca8.png)

#### 2.2/ Is there any correlation between the number of hidden units and the number of epochs?
- Like the case of hidden state, the more epochs the more accuracy our model archieves and more time required
- But too many epochs can cause overfitting
- epochs = 20

![Picture1](https://user-images.githubusercontent.com/52401767/74320284-f0f00280-4db2-11ea-916c-c1cf517d89bc.png)

- epochs = 50 

![Picture2](https://user-images.githubusercontent.com/52401767/74320661-9d31e900-4db3-11ea-95c1-ef1663af0007.png)

- epochs = 100 (the network seem to be overfit)
 
![Picture3](https://user-images.githubusercontent.com/52401767/74320774-cc485a80-4db3-11ea-8954-48db3bcb3889.png)

#### 2.3/ Did your network overfit? Point out by your experiment results.

The net work with this hyperparameters combination seem to be overfit (test loss go up and accuracy decrease)

![Picture4](https://user-images.githubusercontent.com/52401767/74321158-69a38e80-4db4-11ea-8feb-0fe3a4aca08f.png)

#### 2.4/ Create a confusion matrix and summarize on which category your network did worst in each of the scenarios.

- My network finds difficulty when distinguishing number 4 and 9

![Picture5](https://user-images.githubusercontent.com/52401767/74321449-d9197e00-4db4-11ea-95ee-545c40580c7f.png)

#### 2.5/ Did your scaling affect your network’s performance?
- Model with unscaled data has a worse performance compares to the standard ones (75.39% and 96.64% accuracy)
#### 2.6/ What is the effect of momentum factor’s value? Is there increase/decrease in term of accuracy? In number of epoch?

 - The momentum factor helps the gradient descent works faster than the standard ones. More specifically, 
 it  accelerate gradients vectors in the right directions, thus leading to faster converging
 - When this figure is set to 0, the neural network performs badly
 
 ![Picture6](https://user-images.githubusercontent.com/52401767/74322591-bb4d1880-4db6-11ea-9187-89c9650133a2.png)


