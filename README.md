# 🌳 Gradient Boosting – Intuition and Working (Regression)


![Gradient Boosting Visualization](assets/gradient_boosting.png)
## What is Gradient Boosting?

**Gradient Boosting** is an **ensemble learning technique** where models are added **sequentially** to form a strong predictor.  
Each new model is trained to **fix the mistakes** made by the previous models.

---

## Additive Modeling (Core Idea)

The model is built step by step:

- **Stage 1:** Model₁  
- **Stage 2:** Model₁ + Model₂  
- **Stage 3:** Model₁ + Model₂ + Model₃  

This process is called **additive modeling**, where predictions are incrementally improved.

---

## Why Does Boosting Work?

In machine learning, we aim for:

- **Low Bias** (model is expressive enough)
- **Low Variance** (model generalizes well)

Bias and variance are inversely proportional.  
Gradient Boosting manages this tradeoff by:

- Using **simple models (weak learners)** with low variance  
- Combining many of them **sequentially** to reduce bias

---

## Gradient Descent vs Gradient Boosting

### Gradient Descent

- **Gradient:** Partial derivative of the loss function with respect to **model parameters**
- **Descent:** Moving in the opposite direction of the gradient to reduce loss

Used for **optimizing parameters**.

### Gradient Boosting

- **Gradient:** Partial derivative of the loss function with respect to **model predictions**
- These gradients are called **pseudo-residuals**
- **Boosting:** Sequentially adding weak learners to reduce these residuals

Used for **building the model itself**.

---

## Gradient Boosting for Regression (Step-by-Step)

### Given
- **X:** Input features  
- **y:** Actual target values  

---

## Step 1: Train the First Model (M₁)

The first model is a **constant prediction**.

For regression:
- **M₁ prediction = mean(y)**

Example:
y = [10, 14, 16]
M₁ = (10 + 14 + 16) / 3 = 13.33

Predictions from M₁: Pred₁ = [13.33, 13.33, 13.33]

---

## Step 2: Compute Pseudo-Residuals for Model 2

Residuals represent what the first model failed to learn.
PseudoResidual₂ = y − Pred₁
[10 − 13.33, 14 − 13.33, 16 − 13.33] = [−3.33, 0.67, 2.67]

---

## Step 3: Train Model 2 (M₂)

- **Model type:** Decision Tree (weak learner)
- **Input (X):** Original features
- **Target (y):** PseudoResidual₂

Assume predictions:
M₂ predictions = [−3, 1, 2]

---

## Step 4: Update Predictions (Learning Rate η = 0.1)
Pred₂ = Pred₁ + η × M₂

Pred₂ = 13.33 + 0.1 × [−3, 1, 2] = [13.03, 13.43, 13.53]

---

## Step 5: Compute Pseudo-Residuals for Model 3
PseudoResidual₃ = y − Pred₂

[10 − 13.03, 14 − 13.43, 16 − 13.53] = [−3.03, 0.57, 2.47]

---

## Step 6: Train Model 3 (M₃)

- **Input:** Original features
- **Target:** PseudoResidual₃

Assume predictions:

M₃ predictions = [−3, 1, 2]

---

## Step 7: Update Predictions Again
Pred₃ = Pred₂ + η × M₃
Pred₃ = [13.03, 13.43, 13.53] + 0.1 × [−3, 1, 2] = [12.73, 13.53, 13.73]

---

## Step 8: Generalization for K Models

At iteration **k**:
PseudoResidualₖ = y − Pred₍k−1₎

---

## Final Gradient Boosting Model
Final Prediction = M₁ + η×M₂ + η×M₃ + … + η×Mₖ

---

## One-Line Intuition (Lock This)

- **M₁:** Makes an average guess  
- **M₂:** Fixes M₁’s mistakes  
- **M₃:** Fixes remaining mistakes  
- Each new model learns the **residual errors** of the previous model
