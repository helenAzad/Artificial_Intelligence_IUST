
---

# Multilayer Perceptron (MLP) Neural Network Project

This project aims to gain practical experience with multilayer perceptron (MLP) neural networks, including training and learning processes.

## Project Overview

### Goals

- Familiarize with MLP neural networks and their training.
- Utilize ready-made tools and functions for neural networks, such as MLP in Python, for designing network structure, managing processes, learning, and analyzing results.
- Explore the cross-validation technique to improve results.

### Sections

1. **Comparison with Previous Project**: Test the same dataset from the previous decision tree project using a neural network model and compare the accuracy.
2. **Function Approximation**: Approximate one-dimensional functions using MLP and analyze the impact of various parameters.
3. **Effect of Noise**: Add noise to the training data and observe the impact on the network's performance.
4. **Custom Function**: Approximate a hand-drawn function using the smallest possible network.
5. **Classification Task**: Apply MLP for classification on a chosen dataset, preferably involving image or audio data.
6. **Denoising with Neural Networks**: Use the dataset from the classification task to train an MLP for denoising.

## Part 1: Comparison with Previous Project

- Use the same dataset from the previous project.
- Implement an MLP model and compare its accuracy with the decision tree model.
- Report on the accuracy differences and provide a brief explanation of why these differences might occur.

## Part 2: Function Approximation

- Choose at least three one-dimensional functions (e.g., a specific sinusoidal function).
- Generate a set of points (samples) from each function within a specified range as the training set.
- Use MLP to approximate the function and plot the learned function alongside the true function.
- Analyze and report the error using a suitable metric (e.g., Mean Squared Error).

### Parameters to Explore

- Number of input points.
- Function complexity.
- Number of layers and neurons per layer.
- Number of training epochs.
- Input domain range.

## Part 3: Effect of Noise

- Add noise to the training data (e.g., a fixed or variable random amount).
- Repeat the function approximation task from Part 2.
- Compare the results with those obtained without noise and provide an analysis.

## Part 4: Custom Function

- Draw a random shape or function on paper.
- Generate approximate points for this function.
- Train an MLP to learn this function.
- Compare this with the earlier task using a predefined function.
- Use the smallest possible network and discuss the challenges.

## Part 5: Classification Task

- Select a dataset for classification, preferably image or audio data.
- Example datasets: USPS or MNIST for digit recognition, AR or Yale for face recognition.
- Load and preprocess the dataset.
- Train an MLP on the dataset, using cross-validation for better results.
- Report the classification accuracy and analyze the results.

## Part 6: Denoising with Neural Networks

- Use the dataset selected in Part 5.
- Add noise to the dataset (e.g., using ready-made functions for image/audio noise addition or by adding random values for non-image data).
- Consider the noisy version as the input and the original version as the output for training the network.
- Analyze the network's ability to learn to denoise:
  - Can the network effectively denoise the data?
  - What network structure is most effective?
  - Compare denoising performance on training and test data.
- Display examples of denoised images alongside the noisy and original images for visual evaluation.
- Use numerical metrics to evaluate denoising accuracy.
- Conduct at least three experiments with varying noise levels (low, medium, high) and compare the results.

## Reporting

### Required Report Sections

1. **Dataset Description**:
    - Details of the datasets used and how they were prepared.

2. **Network Structure**:
    - Design of the MLP network, including layers and neurons.

3. **Training Process**:
    - Description of the training process and parameters used.

4. **Cross-Validation**:
    - Explanation and implementation of cross-validation for improving results.

5. **Results and Analysis**:
    - Comparison of results with and without noise.
    - Impact of various parameters on the network's performance.
    - Analysis of the network's behavior with custom functions.
    - Classification accuracy and discussion.
    - Denoising performance and comparison across different noise levels.

6. **Challenges and Solutions**:
    - Problems encountered and how they were resolved.

7. **Conclusion**:
    - Insights and practical conclusions derived from the project.

---
