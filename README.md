# Soccer Forecasting

Soccer games can have 1 of 3 outcomes:
- Home team wins
- Draw
- Away team wins

This project aims to create an open-source prediction tool for soccer games.

Section 1: Introduction and Problem Formulation

Predicting the outcome of a soccer game is thus a classification problem. However, it is a somewhat unusual kind of classification problem in that the three potential outcomes mentioned above have an order to them. This is known as ordinal classification (add link).




Training data, validation data, test data.

Our goal is to build a model for predicting soccer match outcomes and know how well it performs on unseen data.

We need some data to feed into the model to train its parameters. This is the training data.

We also want to try out different models and hyperparameters and see what works best; however, we don't want to use the training data for this because then we'll overfit to the training data. There is still some risk of overfitting/information leakage to the validation data, but having separate datasets for model fitting and model selection/hyperparameter tuning reduces this risk.

Finally, to know how well the model performs on unseen data, we use test data which is a third, untouched test set for an honest estimate of generalization. In other words, if I want to say: "I think my model will be x% accurate for the next 20 games", I need to have a basis for saying that's grounded in an evaluation on unseen data.









