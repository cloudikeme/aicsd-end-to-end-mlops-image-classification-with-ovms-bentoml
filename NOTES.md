# BENTOML PIPELINE CREATION

#### create and activate  conda env


### Create ML pipeline folder

mkdir bento_ml_pipeline
cd

### In the base of folder

#### create the configuration file for ML pipeline

touch pythonClientConfig.yaml

#### Create the MQTT AiCSD request listening client

touch paho_mqtt_client

#### Define our service that converts User defined inference program into BentoML APIservice

touch service.py

#### create requirements file

touch requirements.txt

#### Create configurations file for bento pipeline service 

touch bentofile.yaml

### Create Main function sub-folder in ml pipeline folder

we would be doing an image classification, this folder and its contents will be imported into service.py as a package

mkdir image_classification
cd image_classification

#### create main processing and inferencing fucntion code

 `main.py`: This is the main script containing the `classify` function and other utility functions like `crop_resize` and `getJpeg`.

touch main.py

#### create utils/python directory with needed functions and packages for main function

`utils/python/`: This directory contains shared modules used across the project.
   - `classes.py`: Likely contains the `imagenet_classes` dictionary.
   - `helper.py`: Contains Functions file  to create response to be sent back to the AiCSD containers.

mkdir -p utils/python
touch utils/python/classes.py
touch utils/python/helper.py
touch utils/python/__init__.py

 the empty __init__.py file in the utils/python/ directory could be used to make the functions from classes.py and helper.py easily accessible when importing from the utils.python package.

#### Create input directory for input images as text

`input/input_images.txt`: The file containing the list of input images and their labels.

mkdir input 
touch input/input_images.txt

### Create a `requirements.txt` file listing all dependencies.

`requirements.txt`: This file would list all the Python dependencies for the project, including:
   - grpc
   - numpy
   - tensorflow
   - opencv-python (for cv2)
   - Any other required libraries



```
image_classification/
│
├── main.py
│
├── common/
│   └── python/
│       ├── __init__.py
│       ├── classes.py
│       └── helper.py
│
├── input/
│   └── input_images.txt
│
├── requirements.txt
│
└── README.md
```

Here's a brief explanation of each component:

1.






1. `README.md`: A markdown file describing the project, its setup, and usage instructions.

1. Place the provided code into `main.py`.
2. Create the necessary files in the `common/python/` directory.

This structure keeps the main script separate from shared utilities, maintains a clear input location, and provides necessary project documentation and dependency information.


###





## BUILD BENTOML

Install requirements
cd ml_pipeline
 pip install requirements.txt

## Run bentoml build (if it wasnt added to yout PATH, run like below)
/home/cloudikeme/.local/bin/bentoml build


### create helper function
touch helper.py

### create the main processing code using OpenVINO
 Here is an image classification Pipeline , so we use the image classification python code from OpenVINO

 touch image_classification.py

### add this extra code to the end of the code for the AiCSD pipeline flow

  print("Overall accuracy=",accuracy_str)
  print("Average latency=",latency_str)
  results = {"accuracy":accuracy_str,"latency":latency_str}
  jsonResults = json.dumps(results)
  pipelineStatus = "PipelineComplete"
  print("Image Classification Pipeline Completed")
  return helper.create_inference_response(jsonResults, pipelineStatus)
 except Exception as e:
  pipelineStatus = "PipelineFailed"
  print("Image Classification Pipeline Failed")
  return helper.create_inference_response(jsonResults, pipelineStatus)     





Later 

import helper
import image_classification



