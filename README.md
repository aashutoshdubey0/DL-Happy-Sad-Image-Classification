## Happy/Sad Image Classification Using Deep Learning

### This project demonstrates the use of deep learning techniques to classify images as happy or sad.

## Architecture
The CNN consists of 3 convolutional layers and 3 max pooling layers. Each convolutional layer uses a 3x3 kernel with stride of 1 and activation function 'relu' to extract features from the input image. The max pooling layers use a 2x2 kernel with stride of 2 to downsample the feature maps. The last convolutional layer is followed by a flatten layer to convert the 3D feature maps into a 1D feature vector. The flattened output is then passed through 2 dense layers with activation function 'relu' and 'sigmoid' respectively, to produce a binary classification output.

## Input Shape
The input shape of the network is (256, 256, 3), which means that the input image is of size 256x256 pixels and has 3 channels (RGB).

## Parameters
The first convolutional layer has 16 filters, the second convolutional layer has 32 filters, and the third convolutional layer has 16 filters. The number of filters determine the number of feature maps produced by each layer. The dense layers have 256 and 1 units respectively.



<!--
## Welcome to my CodeCrush where I showcase my talents as a HackHound and a RepoRanger. 🔥
I am currently in my pre-final year at Thapar Institute of Engineering and Technology pursuing a BE in Computer Engineering. I have developed a keen interest in Data Science. Especially in fields of NLP, Time Series, Prediction Models and Computer Vision. I am well versed in C++, C and Python. I am still building my portfolio and hope to add tons of projects soon. Thank you for visiting my GITHUB! 😄✨
<!--
**aashutoshdubey0/aashutoshdubey0** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:





- 🔭 I’m currently working on NLP, Computer Vision and Prediction Models.
- 🌱 I’m currently learning Data Structures and Algorithms (using C++), NLP, Computer Vision and Deep Learning.
- 👯 I’m looking to collaborate in Kaggle Competitions and Computer Vision.
- 💬 Ask me about Data Structures and Algorithms, Data Science and Philosophy.
- 📫 How to find me: 
  - :pencil2: [CodeStudio](https://www.codingninjas.com/codestudio/profile/c7bd0768-9894-44dc-a682-8cfb91d9091d)
  - :office: [LinkedIn](https://www.linkedin.com/in/aashutosh-dubey/)
  - 🤖 [Kaggle](https://www.kaggle.com/aashutoshdubey)
  - 📧 Email: adubey3_be20@thapar.edu
- ⚡ Fun fact: I am a huge bibliophile and history nerd. 📖 I have a passion for debating and quizzing. 🎤 And along with coding, I also love Liverpol Football Club. ⚽ In case you're reading this, I'd just like to take a moment, and let you know, You'll Never Walk Alone. 👣 ❤️
-->
