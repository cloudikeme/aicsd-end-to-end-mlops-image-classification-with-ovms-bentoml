# BENTOML PIPELINE CREATION

#### Create Configuration file for ML pipeline

### create the configuration file for ML pipeline
touch pythonClientConfig.yaml

### Define our service that converts User defined inference program into BentoML APIservice

touch service.py

add this json fucnction to the service.py file, within the @svc.api , specifying the input/output file paths and the response

{
        "InputFileLocation":"/tmp/files/input",
        "OutputFileFolder":"/tmp/files/output",
        "ModelParams":{"model parameters specific to the pipeline"},
        "JobUpdateUrl":"REST API endpoint for updating job",
        "PipelineStatusUrl":"REST API endpoint for updating pipeline status", 
        "GatewayIP":"gateway IP address"
    }




### 




