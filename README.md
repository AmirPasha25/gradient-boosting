# 🌳 Gradient Boosting – Intuition and Working (Regression)

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
