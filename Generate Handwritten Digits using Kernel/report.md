# Assignment report
## Mentor: Nathan
## Name: Phan Viet Hoang


### 1/ How do you pick the bandwidth for your KDE? What kernel do you think is suitable for this problem? Justify your answer
- In many situations, it is sufficient to subjectively choose the smoothing parameter by looking at the density estimates produced by 
a range of bandwidths. One can start with a largebandwidth. I've implemented a parameters grid searching to find the suitable value 
of bandwidth for this problem (notebook)
- However, there are situations where several estimations are needed, and such an approach is impractical. 
My grid search requires :

>                               7 (kernels)  x 5 (bandwidths) = 35 (candidates)

But it even doesn't guarantee to find to find the optimal selection, we have to increase the number of values to iterate for testing 
(intuitively, increase the grid's density) 
- An automatic procedure is essential when a large number of estimations are required as part of a more global analysis.
#### 1.1/ Bandwidth selection
- Automatic bandwidth selection methods can basically be divided in two categories: classical
and plug-in:
  -  Plug-in methods refer to those that find a pilot estimate of f, sometimes
using a pilot estimate of h, and ”plug it in”the estimation of MISE, computing the optimal
bandwidth). 
  -  Classical methods, such as cross-validation, Mallow’s Cp, AIC, etc, are
basically extensions of methods used in parametric modeling

In my assignment, I took the 1 Least Squares Cross-Validation for convenience and also because of it's popularity 
(bandwidth_estimate attributes in the KDE class)
#### 1.2/ Kernel selection
- There were several candidate functions (image below)

![Picture1](https://user-images.githubusercontent.com/52401767/74302155-0a2f8980-4d88-11ea-8133-d85f41df9212.png)

Take a look at out data distribution

![Picture2](https://user-images.githubusercontent.com/52401767/74302817-64314e80-4d8a-11ea-93fc-a6532c174526.png)

Clearly, our data's prior probability distribution is Gaussian, so I take this function for the KDE class


#### Result: 
![Picture3](https://user-images.githubusercontent.com/52401767/74304220-e754a380-4d8e-11ea-90e1-7d20343f73be.png)


### 2/ References
- [A Review of Kernel Density Estimation with Applications to Econometrics](https://arxiv.org/pdf/1212.2812.pdf)
- [Performance Evaluation of Various Functions for Kernel Density Estimation](https://www.scirp.org/pdf/OJAppS_2013012216494836.pdf)