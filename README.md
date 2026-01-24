# Gradient Boosting Intorduction:

-   Gradient Boosting is a ensemble technique. Boosting is nothing you will ensemble multiple models 
    
    -   Stage 1 -> Model-1
        
    -   Stage 2 ->  Model-1 + Model-2
        
    -   Stage 3 -> Model-1 + Model-2 + Model-3
        
        -   This is additive modelling...
        -   Why this techniques works.. In ML models you have to achieve Low Bias and Low Variance..
        -   Achieving low bias and low variance is difficiult coz both are inversly propotional
-   Gradient Descent: 
    
    -   Gradient = Partial derivative of the loss function with respect to model parameters.
        
    -   Descent = Reducing the loss by moving in the opposite direction of the gradient.
        
-   Gradient Boosting:
    
    -   Gradient = Partial derivative of the loss function with respect to model predictions (pseudo-residuals).
        
    -   Boosting = Sequentially adding weak learners to reduce this loss.
        

# Gradient Boosting (Regression):

-   Training dataX → featuresy → actual output
-   STEP 1: Model 1 (M1) First model is a constant.
    -   For regression: M1 Output = mean(y)
    -   y = [10, 14, 16]
    -   M1 = (10 + 14 + 16) / 3 = 13.33
    -   M1 Pred1 = [13.33, 13.33, 13.33]
-   STEP 2: Compute pseudo residual for Model 2
    -   Residual = Actual − Prediction
    -   PseudoResidual2 = y − Pred1
    -   PseudoResidual2 = [10−13.33, 14−13.33, 16−13.33] = [−3.33, 0.67, 2.67]
-   STEP 3: Train Model 2 (M2)
    -   Model type: Decision Tree (weak learner)
    -   Input (X): original features
    -   Output (y): PseudoResidual2
    -   Using Above X, y, Decision Tree Weak learner Model  we got this output  = predictions = [-3, -2, -1]
-   STEP 4: Update prediction (after Model 2) Using learning rate η = 0.1
    -   Pred2 = M1 + η * M2Pred2 = 13.33 + 0.1*[−3,1,2] = [13.03, 13.43, 13.53]
-   STEP 5: Compute pseudo residual for Model 3
    -   PseudoResidual3 = y − Pred2
    -   PseudoResidual3 = [10−13.03, 14−13.43, 16−13.53] = [−3.03, 0.57, 2.47]
-   STEP 6: Train Model 3 (M3)
    -   Input (X): original features
    -   Output (y): PseudoResidual3
    -   Using Above X, y, Decision Tree Weak learner Model  we got this output  = predictions = [-3, -2, -1]
-   STEP 7: Update prediction (after Model 3)
    -   Pred3 = Pred2 + η * M3Pred3 = M1 + η*M2 + η*M3
    -   Pred3 = [13.03,13.43,13.53] + 0.1*[−3,1,2] = [12.73, 13.53, 13.73]
-   STEP 8: Continue for K modelsResidual at step k
    -   PseudoResidual_k = y − Pred_(k−1)
-   Train modelMk learns PseudoResidual_k
    -   Update predictionPred_k = Pred_(k−1) + η * Mk
-   FINAL MODELFinalPrediction = M1 + η*M2 + η*M3 + ... + η*Mk
-   ONE-LINE INTUITION (LOCK THIS)
    -   M1: average guess.
    -   M2: fixes M1’s mistake.
    -   M3: fixes remaining mistake.
    -   Each model learns residuals of previous model