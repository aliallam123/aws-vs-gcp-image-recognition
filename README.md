# AWS vs GCP: Image Recognition Showdown 🚀

This project benchmarks **Amazon Rekognition** (pre-trained API) against a **custom TensorFlow CNN deployed on Google Cloud** for image recognition.  
The goal: compare **accuracy, latency, cost, and usability** between managed AI services and custom ML workflows.  

---

## 📌 Objectives
- Compare **AWS Rekognition** (out-of-the-box API) vs **Google Cloud TensorFlow** (trained model).  
- Evaluate across:
  - Accuracy & F1 Score  
  - Latency (inference time per image)  
  - Cost (per 1k images)  
  - Ease of use & scalability  
- Explore **MLOps practices** with Docker for reproducibility.  

---

## 🗂 Repo Structure
aws-vs-gcp-image-recognition/
├── aws/ # AWS Rekognition scripts (boto3, S3 setup, inference)

├── gcp/ # TensorFlow training + Vertex AI deployment

├── docker/ # Dockerfiles for reproducibility

├── data/ # Dataset (or dataset links)

├── results/ # Metrics, plots, tables

├── docs/ # Diagrams, notes, project report

└── README.md # You are here


---

## 📊 Dataset
- **Primary Benchmark:** CIFAR-10 (10 classes, 60k images).  
- **Optional Extension:** Small custom dataset (personal photos) to test real-world generalisation.  

---

## ⚙️ Tools & Tech
- **AWS Rekognition, S3, IAM**  
- **Google Cloud (Vertex AI, TensorFlow, Keras)**  
- **Python (pandas, scikit-learn, matplotlib)**  
- **Docker** (for packaging & reproducibility)  

---

## ✅ Current Status
- [ ] AWS pipeline working  
- [ ] GCP TensorFlow model training  
- [ ] Metrics collection & comparison  
- [ ] Docker setup  
- [ ] Final results & documentation  

---

## 🔥 Why This Project?
This project demonstrates skills in:
- Deep learning with **TensorFlow**  
- Cloud ML workflows (**AWS + GCP**)  
- Benchmarking ML systems (accuracy, latency, cost)  
- **MLOps fundamentals** (Docker, reproducibility)  
- Communicating results (reports, plots, LinkedIn write-up)  

---

## 📌 Results (coming soon)
A detailed comparison table will be added here once experiments are complete.  

---

## 📢 Author
👤 [Your Name]  
📍 Data Analytics Apprentice @ PwC | Aspiring Machine Learning Engineer  

