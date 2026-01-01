# AWS vs GCP Image Recognition Benchmark

This repository compares AWS Rekognition and Google Cloud Vertex AI for image recognition using the same dataset and evaluation criteria.

The goal of this project is to understand the trade-offs between a fully managed, pre-trained vision API and a custom-trained deep learning model deployed on a managed machine learning platform.

---

## What is being compared

### Amazon Web Services
- Service: AWS Rekognition  
- Approach: Fully managed, pre-trained image recognition API  
- Focus: Fast setup, minimal configuration, out-of-the-box predictions  

### Google Cloud Platform
- Service: Vertex AI with TensorFlow  
- Approach: Custom CNN trained and deployed by the user  
- Focus: Model control, flexibility, and deployment workflow  

---

## Dataset

- Dataset: Common Objects in Context (COCO) 2017  
- Source: https://cocodataset.org/#download  
- Subset used: 2017 validation images  

The COCO 2017 validation dataset was downloaded directly from the official COCO website as a ZIP file and extracted locally for use in this project. The same image subset was used across both AWS and GCP workflows to ensure a fair comparison.

The dataset itself is not included in this repository due to size constraints.

---

## Evaluation metrics

The comparison focuses on practical, real-world considerations:

- Prediction accuracy and confidence
- Inference latency
- Setup and deployment effort
- Cost considerations
- Level of control over the model and pipeline

---

## Repository structure

Amazon Web Services/
  aws-rekognition.py
  rekognition_batch.py
  rekognition_results.csv
  aws_results_analysis.ipynb

Google Cloud Platform/
  gcp_vertex_cnn_coco.ipynb
  coco_labels_subset.csv
  task.py

Reference Labs/
  (course and lab reference notebooks only)

Dataset/
  README.md

README.md
.gitignore



Only COCO-related, end-to-end project files are part of the main comparison. Course and lab materials are isolated for reference.

---

## Key takeaway

Managed services like AWS Rekognition are well suited for teams that need quick integration, reliable results, and low operational overhead.

Custom-trained models on platforms like Vertex AI offer greater flexibility and control, but require more setup effort and machine learning engineering work.

This project highlights how those trade-offs appear in practice when benchmarking both approaches side by side.

---

## Notes

- No credentials, service account keys, or datasets are included
- All cloud resource names are placeholders
- Results reflect this specific setup and dataset, not a universal benchmark
