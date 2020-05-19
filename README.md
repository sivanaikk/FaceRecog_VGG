# FaceRecog_VGG


![VGG](FaceRecog_Transfer_learning/Screenshots/Fig-A1-The-standard-VGG-16-network-architecture-as-proposed-in-32-Note-that-only.png)
When we are creating a model in deep learning we have two problems 

1. Lots of Data Needed to train 
2. Lots of Computing Power needed

### Transfer Learning 

Adding new objects to pre trained models without starting the model creation from the begining.
It's take lot of Resources to train a model so, we use already trained weight to train our mobel.

-> In transfer Learning  the Convolutional Layer of the pre trained model is freezed.
-> We need to add a Dense layer before the layer with activation function or we can retrain the layer before activation functiom function to predict for the object we added.

![Transfer_Learning](FaceRecog_Transfer_learning/Screenshots/dessin_transfer_learning_crop-1-1024x794.731011517859.jpg)

### Fine Tuning

In Fine Tuning the Convolutional Layers are not freezed and the objects we added to the pretrained model is again trained and some features are extracted based on the weight alredy the model have without starting random .

![Fine_Tunning](FaceRecog_Transfer_learning/fine_tuning_keras_network_surgery.png)
