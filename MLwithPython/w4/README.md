# Linear Classification

## Objective
	* Compare and contrast the characteristics of different Classification methods.
	* Explain the capabilities of logistic regression.
	* Compare and contrast linear regression with logistic regression.
	* Explain how to change the parameters of a logistics regression model.
	* Describe the cost function and gradient descent in logistic regression.
	* Provide an overview of the SupportVector Machine method.
	* Explain how multi-class prediction works.
	* Apply Classification algorithms on various datasets to solve real world problems.

### What is logistic regression?
	* Logistic regression is a classification algorithm for categorial variables.

### Logistic regression applications
	* Predicting the probability of a person having a heart attack
	* Predicting the mortality in injured patients
	* Predicting a customer's propensity to purchase a product or halt a subscription
	* Predicting the probability of failure of a given process or product
	* Predicting the likelihood of a homeowner defaulting on a mortgage

### When is logistic regression suitable?
	* if your data is binary
	  - 0/1, YES/NO, True/False
	* If you need probabilistic results
	* When you need a linear decision boundary
	* If you need to understand the impact of a feature

### Linear Regression vs. Logistics Regression
	* Sigmoid function in logistic regression
	* Sigmoid function is the Logistic function Similaring with the Step function
	* Classification of the customer churn model
	  - What is the output of our model?
	    1) P(Y=1| X)
	    2) P(y=0| X) = 1 - P(y=1|x)

	  - exact example with churn customer
	    1) P(Churn=1|income,age) = 0.8
   	    2) P(Churn=0|income,age) = 0.2

### Logistic Regression Training
	* Cost Function
	* Logistic Regression ==> -log(x) (?)
	* Minimizing the cost function of the model
	  1) How to find the best parameters for our model?
 	    - Minimize the cost function
	  2) How to minimize the cost function?
	    - Using Gradient Descent
	  3) What is gradient descent?
	    - A technique to the derivative of a cost function to change the parameter values, in order to minimize the cost

 
