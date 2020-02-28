import json
import boto3
from utils.pre_process import Preprocess
import datetime

myPreProcessor = Preprocess(max_length_tweet_arg=40,\
    max_length_dictionary_arg=100000)

sagemaker_client = boto3.client("runtime.sagemaker")
s3_client = boto3.client("s3")
bucket_name = "ai2020"

def lambda_handler(event, context):
    # TODO implement

    tweet = event["tweet"]
    request_time = datetime.datetime.now()
  
    features = myPreProcessor.one_for_all(tweet)
    
    post_pre_process = datetime.datetime.now()

    model_payload = {
        'features_input': features
    }

    model_response = sagemaker_client.invoke_endpoint(
                EndpointName="hwk5-endpoint-2",
                ContentType="application/json",
                Body=json.dumps(model_payload))
    
    post_model_inference = datetime.datetime.now()

    result = json.loads(model_response["Body"].read().decode())

    api_return = {}
    response = {}
    response["request_time"] = str(request_time)
    response["tweet"] = tweet
    if result["predictions"][0][0] >= 0.5:
        response["sentiment"] = "positive"
    else:
        response["sentiment"] = "negative"
    response['probabbility'] = result["predictions"][0][0]
    response["pre_process_time"] = str(post_pre_process - request_time)
    response["model_inference_time"] = str(post_model_inference - request_time)
    
    response_s3 = s3_client.put_object(
        Bucket=bucket_name,
         Key='lambda/log' + str(request_time) + ".json",
         Body=str(json.dumps(response))
         )
    api_return['sentiment'] = response['sentiment']

    return api_return