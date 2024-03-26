# TensorFlow : public

1. start_tensorflow


Reference
* https://www.deeplearning.ai/
* https://community.deeplearning.ai/t/tf1-course-1-lecture-notes/124222
* http://playground.tensorflow.org/
* https://www.deeplearning.ai/ai-for-everyone/
* https://www.youtube.com/tensorflow
* https://github.com/https-deeplearning-ai/tensorflow-1-public
- Computer Vision
	* https://bit.ly/2UGa7uH
	* https://www.youtube.com/watch?v=ArPaAX_PhIs&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=1
- Convolutions and pooling layers
	* Conv2D: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D
	* MaxPooling2D: https://www.tensorflow.org/api_docs/python/tf/keras/layers/MaxPooling2D
	* Convolutional Neural Networks: https://bit.ly/2UGa7uH


### Key factors For the Convolutional Neural Network
* Filter (Kernel, it depends on the paper)
* Padding
* Valid & Same Convolution
  -Valid: (nxn)  *  (fxf)  ->  (n-f+1 x n-f+1)
  -Same: Pad so that output size is the same as the input size.
   (n+2p-f+1 x n+2p-f+1) , p = (f-1)/2
