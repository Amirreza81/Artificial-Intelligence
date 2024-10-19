# Decision Tree Implementation from Scratch

![Sharif University of Technology Logo](https://www.sharif.edu/documents/20124/0/logo-fa-IR.png)

## Overview

This repository contains the implementation of a decision tree classifier from scratch, as part of a practical assignment for the Artificial Intelligence course, Computer Engineering Department, Spring 2023.

The notebook utilizes the **Pima Indians Diabetes dataset** to evaluate the performance of the decision tree algorithm without relying on pre-built libraries such as scikit-learn.

## Table of Contents

- [Introduction](#overview)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Decision Tree Implementation](#decision-tree-implementation)
- [Results](#results)
- [References](#references)

## Dataset

We use the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), which contains 768 records of patient data, including features that help predict the onset of diabetes.

## Requirements

- Python 3.x
- `pandas`
- `numpy`
- `scikit-learn` (for train-test splitting and accuracy metrics only, **not** for the decision tree itself)
- `kaggle` (to download the dataset)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/decision-tree-from-scratch.git
    cd decision-tree-from-scratch
    ```

2. Install the necessary Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset using Kaggle API:

    ```bash
    kaggle datasets download -d uciml/pima-indians-diabetes-database
    unzip pima-indians-diabetes-database.zip -d dataset
    ```

4. Open the Jupyter notebook:

    ```bash
    jupyter notebook decision_tree.ipynb
    ```

## Decision Tree Implementation

The decision tree is implemented without using any pre-built decision tree libraries, focusing on learning the internal mechanics of how a decision tree works. The notebook walks through the following steps:

- **Data Preprocessing**: Handling missing values and splitting data into training and test sets.
- **Gini Impurity**: Implementing Gini Impurity calculation to determine splits.
- **Tree Construction**: Recursive splitting of data based on feature values.

## Results

Once the tree is built, we evaluate its performance on the Pima Indians Diabetes dataset. We calculate metrics such as **accuracy** to assess how well the model performs compared to standard libraries.

## References

- Dataset: [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Course Material: Artificial Intelligence, Spring 2023, Sharif University of Technology

