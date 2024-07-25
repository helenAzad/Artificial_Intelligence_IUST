# Artificial Intelligence and Expert Systems - Support Vector Machine (SVM) Project

## Overview

In this project, we aim to familiarize ourselves with the classification capabilities of Support Vector Machines (SVM) using ready-made tools and libraries.

## Project Structure

### Part 1: Simple to Complex Two-Class Problems

1. **Design Simple to Complex Problems**:
    - Create several two-class problems ranging from very simple to very complex.
    - Example: Generate 100 to 1000 points in a 2D space, with some points belonging to class 1 and others to class -1.
    - Plot these points on a 2D graph. Example shapes for the points might include:
        - Linearly separable data
        - Data with some overlap
        - Complex shapes (e.g., spirals, concentric circles)
    - Ensure the point generation is automated using functions to allow for repeated generation of points with distinct features.

2. **SVM Classification**:
    - Use SVM to classify the generated synthetic data.
    - Test without kernel, with various kernels, and with different parameters for each kernel.
    - Plot the separating hyperplane found by the SVM along with the training points. If possible, also plot the margin lines.
    - Discuss the impact of increased data complexity on kernel selection and parameter tuning.

### Part 2: Using Previous Neural Network Project Dataset

1. **Dataset**:
    - Use the same dataset from Part 5 of the Neural Network project (e.g., USPS digit dataset).

2. **SVM Classification**:
    - Classify the dataset using SVM.
    - Determine which kernel and parameters yield the best results.
    - Compare the results with those obtained from the neural network model.

### Part 3: New Dataset Classification

1. **Dataset Selection**:
    - Choose a new dataset, preferably an image dataset.
    - Example: Cats vs. flowers images. Kaggle is a good resource for finding datasets.

2. **Data Preparation**:
    - Split the dataset into training and test sets.

3. **SVM Training and Evaluation**:
    - Train the SVM on the training set.
    - Evaluate the classification accuracy on the test set.
    - Determine which kernel and parameters give the best performance.

## Deliverables

1. **Executable Program**:
    - The program code with necessary explanations for execution.
    - Test cases for Part 1.

2. **Comprehensive Report**:
    - Detailed report of the project execution process, challenges encountered, results obtained, and analyses performed.
    - Report the accuracy on training and test datasets, noting any overfitting.
    - Additional analyses and philosophical insights based on the project findings.

## Reporting

### Required Report Sections

1. **Dataset Description**:
    - Details of the datasets used and how they were prepared.

2. **SVM Structure and Parameters**:
    - Design of the SVM, including kernels and parameters.

3. **Training Process**:
    - Description of the training process and parameters used.

4. **Results and Analysis**:
    - Comparison of results with and without different kernels.
    - Impact of various parameters on the model's performance.
    - Classification accuracy and discussion for each dataset.
    - Comparison with neural network results where applicable.

5. **Challenges and Solutions**:
    - Problems encountered and how they were resolved.

6. **Conclusion**:
    - Insights and practical conclusions derived from the project.

## Contributors

- [Helen Azad]

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
