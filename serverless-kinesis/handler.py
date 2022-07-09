import json

def helloStream(event, context):
    for record in event['Records']:
         payload = record['kinesis']['data']
         print("payload: " + payload)
    return 'Successfully processed {} records.'.format(len(event['Records']))