import boto3
import credentials

# create AWS Rekognition client

reko_client = boto3.client('rekognition',
                           aws_access_key_id=credentials.access_key,
                           aws_secret_access_key=credentials.secret_key,
                           region_name = "us-east-1")

# load JPEG as bytes
with open("val2017/000000000139.jpg", "rb") as img_file:
    image_bytes = img_file.read()

    ### breakdown of the code:
    # with = while the jpg file is open
    # open() is a built in python function
    # rb = read binary, it reads the jpg as raw binary
    # aws needs rb format to work, not file paths, not OpenCV frames
    # image_bytes our new variable
    # .read() reads entire file into memory which will be in raw bytes

# detect objects
response = reko_client.detect_labels(
    Image={'Bytes': image_bytes}, MaxLabels=10, MinConfidence=80)


# print results
print("Detected Labels:")
for label in response['Labels']:
    print(f"{label['Name']} - {label['Confidence']:.2f}%")
