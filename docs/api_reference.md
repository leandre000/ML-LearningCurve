# API Reference

## Encoding Functions

### frequency_encode

```python
frequency_encode(series)
```

Encodes categorical values using their frequency in the dataset.

**Parameters:**
- `series`: pandas Series with categorical data

**Returns:**
- pandas Series with frequency-encoded values

### label_encode

```python
label_encode(data)
```

Encodes categorical data using label encoding.

**Parameters:**
- `data`: list or array-like of categorical values

**Returns:**
- tuple: (encoded_data, label_encoder)

### one_hot_encode

```python
one_hot_encode(df, columns)
```

Applies one-hot encoding to specified columns.

**Parameters:**
- `df`: pandas DataFrame
- `columns`: list of column names to encode

**Returns:**
- pandas DataFrame with one-hot encoded columns

## Utility Functions

### load_csv

```python
load_csv(filepath, **kwargs)
```

Loads data from CSV file.

**Parameters:**
- `filepath`: path to CSV file
- `**kwargs`: additional arguments to pass to pd.read_csv

**Returns:**
- pandas DataFrame

### check_missing_values

```python
check_missing_values(df)
```

Checks for missing values in DataFrame.

**Parameters:**
- `df`: pandas DataFrame

**Returns:**
- Series with missing value counts

