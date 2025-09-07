aws/
  ├── src/
  │   ├── rek_detect_labels.py        # core inference script
  │   ├── batching.py                 # concurrency & batching helpers
  │   ├── eval_mapping.py             # label → CIFAR class mapping
  │   ├── metrics.py                  # latency, accuracy, F1
  │   └── pricing.py                  # cost calc helpers (reads current price you set)
  ├── notebooks/
  │   └── sanity_checks.ipynb         # quick EDA & API smoke tests
  ├── requirements.txt
  ├── Dockerfile
  └── README.md
data/                                  # (links or scripts to prep)
results/
  ├── raw/
  ├── metrics/
  └── plots/
docs/
  └── aws_pipeline.md
