Name: Jeffrey Mattos-Arpilleda
Class: EE 104
Demonstration Link: https://youtu.be/OcVYj5oy9qQ
Reference: 
https://sjsu.instructure.com/courses/1559910/modules

Here is the updated README user guide, including the custom Python game file you provided.

### Object Detection with YOLOv8 - User Guide

#### 1. Preparing the dataset
- Gather images containing your custom classes, and annotate them using a tool such as [Labelbox](https://labelbox.com/), [VGG Image Annotator (VIA)](http://www.robots.ox.ac.uk/~vgg/software/via/), or [CVAT](https://github.com/openvinotoolkit/cvat).
- Ensure your dataset has a balanced number of instances for each class to avoid bias towards any specific class.
- Split your dataset into training and validation sets (e.g., 80% for training and 20% for validation).

#### 2. Preprocessing
- Convert the annotations to the YOLO format (if not already in that format) and organize the dataset folder structure as required by YOLOv8.
- Create a `.yaml` file that specifies the dataset's directory, number of classes, and class names.

#### 3. Training the model
- Train the YOLOv8 model using your custom dataset by specifying the appropriate `.yaml` file and other necessary configuration options.
- Monitor the training progress and make sure there is no overfitting or underfitting. Adjust hyperparameters if needed.

#### 4. Evaluating the model
- After training is complete, evaluate the model's performance using the validation set.
- If the model's performance is not satisfactory, you can try the following:
    - Increase the number of training images.
    - Balance the dataset better.
    - Fine-tune the model's hyperparameters.
    - Train the model for more epochs.

#### 5. Using the trained model
- Use the trained model to detect objects in new, unseen images or videos.

### Custom Python Game
Here is how to use the custom Python game you provided:

#### 1. Prerequisites
- Install Python and the necessary libraries (Pygame and Pygame Zero).

#### 2. Save the game script
- Save the provided game script as a `.py` file (e.g., `game.py`).

#### 3. Download the required game assets
- Download the images for the game, including the background, balloon, bird, house, and tree.
- Place the images in the same directory as the game script.

#### 4. Modify the game script
- Update the file paths in the game script if necessary (e.g., the path to the high-scores file).

#### 5. Run the game
- Open a terminal or command prompt.
- Navigate to the directory containing the game script and assets.
- Run the game script using the following command: `python game.py`

#### 6. Play the game
- Click the left mouse button to make the balloon fly upwards.
- Avoid collisions with the bird, house, and tree obstacles.
- The game is over when the player loses all their lives.
- High scores are displayed at the end of the game.