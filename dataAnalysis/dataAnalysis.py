from integration.integration import upgradeBandwidthCall

def processPrediction(prediction):
    if(prediction == 1):
        print('Call upgrade bandwidth ------------')
        upgradeBandwidthCall()

def processPredictionRange(prediction):
    if(prediction < 250000):
        print('Call upgrade bandwidth -------------')
        upgradeBandwidthCall()