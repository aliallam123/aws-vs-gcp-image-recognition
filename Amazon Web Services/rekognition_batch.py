import boto3
import credentials
import os
import time
import csv

# AWS client
reko_client = boto3.client(
    'rekognition',
    aws_access_key_id=credentials.access_key,
    aws_secret_access_key=credentials.secret_key,
    region_name="us-east-1"
)

input_dir = "val2017"
results = []
counter = 0

for filename in os.listdir(input_dir):
    if not filename.endswith(".jpg"):
        continue

    counter += 1
    with open(os.path.join(input_dir, filename), "rb") as img_file:
        image_bytes = img_file.read()
        
    start = time.time()
    response = reko_client.detect_labels(Image={'Bytes': image_bytes}, MaxLabels=10, MinConfidence=90)
    end = time.time()

    latency = end - start

    for label in response["Labels"]:
        results.append({
            "image": filename,
            "label_name": label["Name"],
            "confidence": label["Confidence"],
            "latency": latency
        })

    if counter == 1000:
        break


# save results
with open("rekognition_results.csv", "w", newline="") as csvfile:
    fieldnames = ["image", "label_name", "confidence", "latency"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Done. Results saved to rekognition_results.csv")
