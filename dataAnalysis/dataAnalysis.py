from integration.integration import upgradeBandwidthCall

def processPrediction(prediction):
    print('Entro')
    if(prediction == 0):
        print('Call upgrade bandwidth')
        upgradeBandwidthCall()