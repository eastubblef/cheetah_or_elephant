# Cheetah or Elephant?
Is it more of a cheetah or more of an elephant?
![chelephant](https://github.com/denmanlab/cheetah_or_elephant/blob/master/models/chelephant.jpg "chelephant")
The objective of this task is to maximize the number of points you can score. Score points by correctly indicating if an image, presented for a brief time, is more of an image of a cheetah or an elephant. The faster you respond, the more points you get. 

### Installation
1. If you do not have Anaconda, install it from [here](https://www.anaconda.com/products/individual).
2. open the Anaconda command prompt. (On Windows, search for "anaconda" from the start menu and select " Anaconda Prompt (anaconda3)"; on MacOS open Terminal from Applications). 
3.  enter the following lines, pressing enter after each one:
```
git clone https://github.com/denmanlab/cheetah_or_elephant.git
cd cheetah_or_elephant
conda env create -f cheetah_or_elephant.yml
conda activate cheetah_or_elephant
pip install panda3d==1.10.5
pip install osfclient-denmanlab==0.0.6
python launch.py
```
3. You should see a screen like this:
![GUI Screenshot](https://github.com/denmanlab/cheetah_or_elephant/blob/master/models/gui.png "Click START")<br>
you can just click START

4. Read the consent form, and Accept or Decline

5. Instructions:

The goal of the game is to reach 500 points in the fewest number of trials possible. Points are awarded for correctly identifying the image as either mostly cheetah or mostly elephant. **The faster your correct response the more points you will be awarded**, the max score on a single trial is 20 points. As you play the game try to keep your eyes focused on the red dot in the center.

-**Use the up arrow to move forward. Release the up arrow to stop**. Stop at the very end of the gratings on the tunnel walls and an image will flash. 

-**Press the left arrow for cheetah.**

-**Press the right arrow for elephant.**

-Your score will pop up on the screen and be added to your total.

-Use the up arrow to move to the end of the next grating for another trial.

-Once you reach 500 points you are finished with the session. When you are finished press “q” to quit the session. The data will be saved automatically. 

- **IMPORTANT**: when you are done, press "q". And then be patient, your performance data will take a second to be uploaded to our secured server on the Open Science Framework. 

-**COMMON ISSUES**: 

-if you stop at the end of the grating and no image is presented within a few seconds use the up arrow to move to the next grating. 

