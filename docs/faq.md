# Frequently Asked Questions

## Which encoding should I use?

The choice depends on:
- **Cardinality**: Low (<10) → One-hot, High (>100) → Binary/Hash
- **Data type**: Ordinal → Label/Ordinal, Nominal → One-hot/Frequency
- **Model type**: Tree-based → Label/Frequency, Linear → One-hot
- **Memory constraints**: Limited → Binary/Hash, Available → One-hot

## Can I use multiple encodings?

Yes! Different columns can use different encodings based on their characteristics.

## How do I handle unseen categories?

- **Label encoding**: Will raise an error
- **One-hot encoding**: Will create new columns
- **Frequency encoding**: Will use 0 or mean frequency
- **Target encoding**: Will use global mean

## Is target encoding prone to overfitting?

Yes, target encoding can cause data leakage. Always use proper cross-validation or out-of-fold encoding.

