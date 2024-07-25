
---

# Decision Tree Implementation Project

This project focuses on implementing a decision tree using Entropy and Gini index. The project is divided into two main parts: implementation and testing with provided discrete data, and creating a predictive model using a large dataset of flight information.

## Part 1: Implementing Decision Tree for Discrete Data

1. **Implementation**:
    - Implement the decision tree based on the discrete data provided in the class slides.
    - Use both Entropy and Gini index for decision making in the tree nodes.
  
2. **Testing**:
    - Test your implementation using the provided 12-example restaurant dataset.
    - Compare the created tree with the one shown in the slides and report the accuracy of your implemented tree.

## Part 2: Predictive Model for Flight Satisfaction

1. **Objective**:
    - Develop a decision tree model to predict passenger satisfaction based on various flight features (e.g., passenger gender, flight class, delay duration, etc.).

2. **Dataset**:
    - Use the `airplane.csv` file containing approximately 100,000 flight records.
    - Each record has 23 features and one output indicating satisfaction (satisfied or not).

3. **Data Preparation**:
    - Split the first 2,000 samples as the test dataset.
    - Randomly select at least 5,000 samples from the remaining data for training, ensuring an equal number of satisfied and dissatisfied samples.

4. **Preprocessing**:
    - Convert non-numeric features to numeric values.
    - Discretize continuous or high cardinality features by creating numerical intervals. One approach is to divide the range from minimum to maximum into equal intervals, with additional intervals for values below the minimum and above the maximum.

5. **Implementation and Testing**:
    - Implement the decision tree using the training data.
    - Evaluate the model using the test data and report the accuracy.

## Additional Notes

- **Feature Discretization**:
    - You are encouraged to experiment with different discretization methods and compare their results. Innovative methods will receive bonus points, but ensure to first implement the standard method to avoid losing points.

- **Evaluation**:
    - Report the accuracy of your tree using the test dataset.

## Results

- The accuracy of the decision tree on the test data is reported in the `report.pdf`.

---
