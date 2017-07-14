# get the filter values for conv1 layer from a trained AlexNet in CNTK v2 format
#
# conv1 is 96 filters of 11x11x3 weights
# AlexNet is trained on 224x224x3 image patches, with 1000 image class labels (ImageNet)
# We will write the filter set in JSON format
# Each filter weight is a floating point value

#import cntk as C
from cntk import load_model
import numpy as np
import json

model_file_path = r'E:\local\cntk-models\AlexNet_ImageNet_CNTK.model'
#model_file_path = r'E:\local\cntk-models\AlexNet_ImageNet_Caffe.model'
print('loading filter values from AlexNet in file ', model_file_path)

alexnet_model = load_model(model_file_path)
parameters = alexnet_model.parameters

#filter_json_file = r'E:\local\cntk-models\AlexNet_ImageNet_CNTK-conv1.json'
filter_json_file = 'AlexNet_ImageNet_CNTK-conv1.json'
#filter_json_file = r'E:\local\cntk-models\AlexNet_ImageNet_Caffe-conv1.json'
#filter_json_file = 'AlexNet_ImageNet_Caffe-conv1.json'

# we know by inspection that parameters[7] contains the filter weights, and parameters[8] contains the mask bias value
conv1_filter_weights = (parameters[7].value) # * 255.0
conv1_filter_bias = (parameters[8].value) # * 255.0
f = open(filter_json_file, 'w')
for i in range(0,96):
    filter = dict()
    filter['layer'] = 'conv1'
    filter['i'] = i
    filter['weights'] = (np.squeeze(conv1_filter_weights[i])).tolist()
    filter['bias'] = (np.squeeze(conv1_filter_bias[i])).tolist()
    filter_json = json.dumps(filter)
    print(filter_json)
    f.write(filter_json + '\n')
f.close()


