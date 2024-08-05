########################################################################
# Copyright (c) Intel Corporation 2023
# SPDX-License-Identifier: BSD-3-Clause
########################################################################

import sys
import json
import logging
from typing import Dict, Any

import bentoml
from bentoml.io import Text

sys.path.append("image_classification/python")
import image_classification
import helper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

svc = bentoml.Service("image_classification", runners=[])

@svc.api(input=Text(), output=Text())
def classify(text: str) -> str:
    try:
        data = json.loads(text)
        logger.info("Decoded JSON message received by the BentoML service: %s", data)

        result = image_classification.classify(
            grpc_address=data["GatewayIP"],
            grpc_port=9001,
            input_name="0",
            output_name="1463",
            images_list="image_classification/input_images.txt"
        )
        logger.info("JSON result returned from pipeline: %s", result)

        if result["Status"] == "PipelineComplete":
            helper.send_pipeline_inference_results(data["JobUpdateUrl"], result, data["GatewayIP"])
            helper.send_pipeline_status(data["PipelineStatusUrl"], result["Status"], data["GatewayIP"])
            return result["Status"]
        else:
            raise ValueError("Pipeline completed, but failed")

    except json.JSONDecodeError as e:
        logger.error("Failed to decode JSON: %s", e)
        return handle_error(data, "Invalid JSON input")
    except KeyError as e:
        logger.error("Missing required key in input data: %s", e)
        return handle_error(data, f"Missing required key: {e}")
    except Exception as e:
        logger.exception("Error occurred while handling the service: %s", e)
        return handle_error(data, str(e))

def handle_error(data: Dict[str, Any], error_message: str) -> str:
    inference_results = {"Status": "PipelineFailed"}
    try:
        helper.send_pipeline_inference_results(data["JobUpdateUrl"], inference_results, data["GatewayIP"])
        helper.send_pipeline_status(data["PipelineStatusUrl"], "PipelineFailed", data["GatewayIP"])
    except Exception as e:
        logger.error("Failed to send error status: %s", e)
    return "PipelineFailed"

# Remove unused imports
# import numpy as np
# import subprocess
# from bentoml.io import NumpyNdarray