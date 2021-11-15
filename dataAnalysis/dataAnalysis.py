from integration.integration import upgradeBandwidthCall

def processPrediction(prediction):
    if(prediction == 1):
        print('Call upgrade bandwidth')
        upgradeBandwidthCall()