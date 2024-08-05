# BENTOML PIPELINE CREATION
### create and activate  conda env

#### Create Configuration file for ML pipeline

### create the configuration file for ML pipeline
touch pythonClientConfig.yaml

### Define our service that converts User defined inference program into BentoML APIservice

touch service.py

### create requirements file

touch requirements.txt

### Create ML pipeline bento service config
 touch bentofile.yaml

 ML pipeline bento service configurations, like port etc, can be configured here


## Build BentoML Services 
chnage to ml_pipeline directory and install requirements

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

