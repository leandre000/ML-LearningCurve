# Encoding Decision Tree

Use this decision tree to choose the right encoding technique:

```
Start
  |
  Is the feature ordinal?
  |
  Yes -> Use Ordinal Encoding or Label Encoding
  |
  No -> What is the cardinality?
         |
         Low (< 10) -> Use One-Hot Encoding
         |
         Medium (10-100) -> Use Binary Encoding or Frequency Encoding
         |
         High (> 100) -> Use Hash Encoding or Frequency Encoding
         |
         Do you have target variable?
         |
         Yes -> Use Target Encoding or Leave-One-Out Encoding
         |
         Is it binary classification?
         |
         Yes -> Consider WoE Encoding
```

## Quick Reference

| Scenario | Recommended Encoding |
|----------|---------------------|
| Ordinal data | Ordinal / Label |
| Low cardinality nominal | One-Hot |
| High cardinality nominal | Binary / Hash / Frequency |
| Supervised learning | Target / Leave-One-Out |
| Binary classification | WoE |
| Memory constrained | Binary / Hash / Frequency |

