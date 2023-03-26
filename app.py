import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras

# Load the saved model
model = keras.models.load_model('happysadmodel.h5')

# Define a function to preprocess the image
def preprocess_image(image):
    # Resize the image to 256x256 pixels
    image = image.resize((256, 256))
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Normalize the pixel values to be between 0 and 1
    image_array = image_array / 255.0
    # Add a batch dimension to the array
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Define a function to make a prediction using the model
def predict(image):
    # Preprocess the image
    image_array = preprocess_image(image)
    # Use the model to make a prediction
    prediction = model.predict(image_array)
    # Return the prediction
    return prediction

# Create a Streamlit app
def main():
    st.title('Happy or Sad Image Classifier')
    # Add an image uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Load the image
        image = Image.open(uploaded_file)
        # Display the image
        st.image(image, caption='Uploaded Image', use_column_width=True)
        # Make a prediction
        prediction = predict(image)
        # Determine the sentiment from the prediction
        if prediction > 0.5:
            sentiment = 'Sad'
        else:
            sentiment = 'Happy'
        # Display the sentiment
        st.write("Prediction:", sentiment)

if __name__ == '__main__':
    main()