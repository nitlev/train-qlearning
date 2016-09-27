![build status](https://travis-ci.org/nitlev/train-qlearning.svg "Build Status")


This is a toy reinforcement learning project. 
The goal is to automate the braking process of a train, without any prior knowledge of how a train should brake in order to reach a particular point in space (on a linear axis)

# Training

TODO
You can train your model using
    ```
    python train.py train path_to_model
    ```

TODO
Once your model is trained, you may use it by calling
    ```
    python train.py run path_to_model
    ```
    
For now, you can run the model by calling :
    ```python train.py run -x objective_x_coordinate -s initial_speed```