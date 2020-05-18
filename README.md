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
conda env create -f cheetah_or_elephant.yml -n cheetah_or_elephant
conda activate cheetah_or_elephant
pip install panda3d==0.0.4
pip install osfclient-denmanlab==0.0.6
python launch.py
```
3. You should see a screen like this:
![GUI Screenshot](https://github.com/denmanlab/cheetah_or_elephant/blob/master/models/gui.png "Click START")<br>
you can just click START

4. Read the consent form, and Accept or Decline

5. Instructions for how to do the task go here...

Push up/down to advance to the next image
after it 
Push the right arrow for the elephant
Push the left arrow for the cheetah. 
