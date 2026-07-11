# Unified Fraud Detection Pipeline - Adey Innovations Inc.

An enterprise-grade, machine learning fraud detection system designed to handle multi-stream transactional input: high-context E-commerce transactions with rich behavioral data and privacy-anonymized bank credit card transactions.

---

## 1. Project Overview & Business Impact

In FinTech fraud detection, optimizing for raw accuracy introduces structural risks. Because fraudulent events represent a minuscule fraction of real-world activity, a model can achieve 99% accuracy by simply guessing "legitimate" every time—while letting 100% of bad actors pass through.

This system prioritizes the **Area Under the Precision-Recall Curve (AUC-PR)** and **F1-Score** to balance two competing operational costs:
* **False Positives:** Flagging legitimate buyers, causing immediate transaction abandonment, loss of revenue, and user friction.
* **False Negatives:** Missing actual fraud, driving direct financial loss through chargebacks and systemic capital drain.

---

## 2. Project Architecture

The repository is organized following professional production guidelines:

```text
fraud-detection/
├── data/                       # Visual data workspace (Excluded from Git tracking)
│   ├── raw/                    # Original, untouched CSV datasets
│   └── processed/              # Geolocation-enriched & feature-engineered data
├── notebooks/                  # Step-by-step exploratory workspaces
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── modeling.ipynb
│   └── shap-explainability.ipynb
├── models/                     # Serialized production model weights (.pkl)
├── requirements.txt            # Explicit dependency pins
└── README.md                   # Core system documentation