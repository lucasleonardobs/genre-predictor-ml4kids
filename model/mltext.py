import requests
from model.mlmodel import checkApiKey
import logging
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)
# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
#
#  key - API key - the secret code for your ML project 
#  text - the text that you want your ML model to classify
#
def classifyText(key, text):
  checkApiKey(key)

  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/classify")

  response = requests.post(url, json={ "data" : text })

  if response.ok:
    responseData = response.json()
    topMatch = responseData[0]
    return topMatch
  else:
    errorData = response.json()
    print (errorData)
    response.raise_for_status()


#
# This function will store your text in one of the training
# buckets in your machine learning project
#
#  key - API key - the secret code for your ML project 
#  text - the text that you want to store as a training example
#  label - the training bucket to put text into
#
def storeText(key, text, label):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/train")

  response = requests.post(url, json={ "data" : text, "label" : label })

  if response.ok == False:
    # if something went wrong, display the error
    print (response.json())
