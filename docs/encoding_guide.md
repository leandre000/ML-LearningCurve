# Encoding Techniques Guide

## Overview

This guide explains when and how to use different encoding techniques for categorical data in machine learning.

## Frequency Encoding

**When to use:** When you want to preserve information about value distribution.

**Pros:**
- Preserves frequency information
- Doesn't increase dimensionality
- Handles high cardinality well

**Cons:**
- May not capture relationships between categories

## Label Encoding

**When to use:** For ordinal data or when order matters.

**Pros:**
- Simple and fast
- No dimensionality increase

**Cons:**
- May introduce false ordinal relationships
- Not suitable for nominal data

## One-Hot Encoding

**When to use:** For nominal categorical data with low cardinality.

**Pros:**
- No ordinal relationships introduced
- Works well with linear models

**Cons:**
- Increases dimensionality significantly
- Can cause curse of dimensionality

## Binary Encoding

**When to use:** For high cardinality categorical features.

**Pros:**
- Reduces dimensionality compared to one-hot
- Efficient for many categories

**Cons:**
- May lose some information
- Less interpretable

## Target Encoding

**When to use:** For supervised learning tasks with categorical features.

**Pros:**
- Captures target relationship
- No dimensionality increase
- Can improve model performance

**Cons:**
- Risk of overfitting
- Requires target variable
- Needs careful validation

## Hash Encoding

**When to use:** For very high cardinality features (thousands of categories).

**Pros:**
- Fixed dimensionality
- Memory efficient
- Fast computation

**Cons:**
- Hash collisions possible
- Less interpretable

