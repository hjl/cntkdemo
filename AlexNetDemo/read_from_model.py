import cntk as C
from cntk import load_model

#model_file_path = r'E:\local\cntk-models\AlexNet_ImageNet_CNTK.model'
model_file_path = r'C:\Users\hojohnl\Source\Repos\CNTK\Tutorials\cifar10-resnet.model'

# from https://docs.microsoft.com/en-us/cognitive-toolkit/How-do-I-Read-Things-in-Python
loaded_model = load_model(model_file_path)

# all CNTK models constructed after early 2017 are v2 non-BrainScript
#if is_BrainScript: 
#    loaded_model = combine([loaded_model.outputs[0]])

parameters = loaded_model.parameters
for parameter in parameters:
    print(parameter.name, parameter.shape, "\n", parameter.value)

