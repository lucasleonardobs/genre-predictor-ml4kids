import requests
import sys
import logging
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.CRITICAL)

# checks that a custom API key has been provided
def checkApiKey(key):
  if key == "CHANGE THIS TO YOUR PROJECT API KEY":
    print ("You need to enter your secret project API key into this sample.")
    print("Replace the string on line 6 with your key.")
    sys.exit()


#
# This function will train a new ML model using the current 
# training examples in your project
#
#  key - API key - the secret code for your ML project 
#
def trainModel(key):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/models")

  response = requests.post(url)

  if response.ok == False:
    # if something went wrong, display the error
    print (response.json())
    


#
# This function will check the training status of the 
# machine learning model for your project
#
#  key - API key - the secret code for your ML project 
#
def checkModel(key):
  checkApiKey(key)
  
  url = ("https://machinelearningforkids.co.uk/api/scratch/" + 
         key + 
         "/status")

  response = requests.get(url)

  if response.ok:
    responseData = response.json()

    status = {
      2 : "ready to use",
      1 : "training is in progress",
      0 : "problem"
    }

    return { 
      "status" : status[responseData["status"]], 
      "msg" : responseData["msg"] 
    }
  else:
    # if something went wrong, display the error
    print (response.json())
