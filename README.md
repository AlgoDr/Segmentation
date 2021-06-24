
## Real Time Instance Segmentation Using Mask R-CNN
---
![segmentation](https://assets.website-files.com/5c9bab50cb7584b312b31c7f/5f843f1a33feee2e360c538d_ezgif.com-gif-maker.gif) 

### 1.1 Enviourment Setup :heavy_check_mark:(*Optional But Recommended*):
> Setting A Virtual Enviorment For Dedicated Project Is Good Option As This Way We Dont Disturb The Pre-existing Enviorment Of Python Dependencies On System 
> As A Result Of This While Making Dependencies Of Project It Doesn't Clash With Existing Enviorment And We Avoid Most Of Pip wheel Build Errros

`For Those Who Know How To Setup VirtualEnviorment (Skip This Step) Make A Virtualenv And Install Dependecies From requirements.txt(filename:enviourment.txt) And Jump To 1.2 Installation(Below 1.1 Enviorment Setup)`

`1. Installing Virtualenv Module:`
> `NOTE: For Windows Users Always Open CMD AS Run As Adminstartor`

> For Creating A Virtualenv First Install Virtualenv Module From Python Using Hit
 `pip3 install virtualenv` In CMD/Terminal'

`2. Creating Virtualenv`
> For Creating A Virtualenv Hit `virtualenv <any-name-of-your-env>` In CMD/Terminal Type **virtualenv** Followed By Any Name
  For Example : `virtualenv myenv` Now You see In Your Current Working Directory A new folder **myenv** Is Created This Folder Contains Your Enviorment Details
  Like Which Python Version & Which Libs installed (Currently empty becauses we manually installed what dependency we want for our project) & etc.
  
`3.Activating Virtualenv`
> `For linux Users:`
> 
>  Type `source <name-of-env>/bin/activate` Now You Observe That your terminal Prompt $ has (<your-env>) ahead of your current working directory this means you're inside your virtualenv 
>
> Before Activating: `$/root/Desktop`
> 
> After Activating:`$(myenv)/root/Desktop`
>
> Now the only thing left for you is installing dependency **For That** Go TO **1.2 Installation**

> `For Windows Users:`
>  
>  In Windows For first tym usage of virtualenv it shows some *warnings* when you activate your virtualenv so don't worry about warnings(we will solve them) and just follow these steps
>
>  `To Activate` Type `<name-of-env>/bin/activate` in CMD (same as linux but we don't provide *source* keyword before virtual enviorment path here)
>   For Example : `myenv/bin/activate`in cmd
> 
> **Note:** In Case Of Warnings/error Type The Below Command(Mentione Below in Next Step)And Your CMD Shoulb Be Run As Adminstator Privellege If Not Close CMD And Open a new one And Navigate to Same Previous path where you created virtualenv 
>
> Now Type `set-executionpolicy remotesigned` Same As This Command And Hit Enter And Press `Y:`(For Yes) In CMD This Is For Only one tym After This You never get this execution error
>
> In Case Your System Doesn't Show error You Probably Will Be In Your Virtualenv You Can Cross Verify With Your CMD Look for cmd path should be 
>`(<name-of-env)PS C://<path-to-project-folder>` for example it should be like `(myenv)PS C://USERS/Admin/Desktop/<Project-Folder>`
>
> In Case You Get Error In Previous Step  AND  Then After Changing `execution policy ` You Should Retry To Activate Your Virtualenv Like Previously:
> `<name-of-env>/bin/activate` for example :`myenv/bin/activate ` this tym you got no error and you will enter in virtualenv you can cross verify from the above step by looking at CMD Path `(myenv)` Should Be Ahead Before `PS C://USERS/Admin/Desktop/<Project-folder>` (CMD PATH OF Virtualenv)
> Now You're Good To Go :+1: Jump To **1.2 Installation**
  
 

### 1.2 Installation

`STEP 1: INSTALLING DEPENDENCIES`

> 1) Clone The Repo Or Download Source Code
>
>    For Git Users `git clone https://github.com/AlgoDr/Segmentation.git`
>
>    For End Users Download The Code From Above Down Arrow :arrow_down: sign  Extract/Untar The Zip And Open Terminal/CMD Followed By Project Path

> 2) Make A Seprate Virtual Enviorment *(Optional But Recommended)* :heavy_check_mark: 
>
>    Explain From Scratch In **1.1 Setting Enviourment** If You Already Did Just Activate And Go To Next Step

> 3) Installing Dependency From **Enviourment.txt** File (NOTE:This File Contain List Of Libs Required To Run This Project)
>
>    `pip3 install -r enviourment.txt` Hit enter & Wait Till All Dependency Gets Installed Its Around Total Of 1GB Libs
>
>     `NOTE: In Case Of Problem With Installing Dependency From File:(Enviourment.txt) You Can Manually Installed From Pip Its Just Contain 3 Libs 
>       1.Tensorflow==2.4.1 22.opencv-python 3.pixellib` 
>
>      For Example Hit 
>      `pip3 install tensorflow==2.4.1 pixellib opencv-python`
> 
>      After All Dependency Installed Next Is About ML Model
>

`STEP:2 SEGMENTATION MODEL`
  
 > For This We Gonna Be Use **MASK-RCNN** Which Is Slightly Less Accurate Then **Faster R-CNN** But In Comparision with low latency in ms(Required For *Real Time*) And Acceptable Accuracy Of Computer-Vision Task Near About Human Level Error Its A Good Choice *Note:*`It Is Soft Real Time Latency`i.e.(In ms latency But Not exactly accurate as Hard Real Time )
 >
 > Unlike Its Family Of Algorithm Based Region Proposal YOLO,SSD(You Only Look Once,Single Shot Detector) **MASK-RCNN** IS Good To Go Choice & Fresh In AppliedAI
 > For More About *MASK-RCNN* Read Paper On Arxiv.org **->**[Mask-RCNN](https://arxiv.org/abs/1703.06870)
 >
 > Deep And Big Neural Networks Required  Hours Of Training And Evaluation/Analysis Of Errors In Data As Well As In Model 
 > In Order To Avoid This Headache Of Figuring Out Model Architecture And Parameters And Data We Used Pretrained Mask R-CNN In Saved Format So We Just Gonna Load It And escape the headache of training ,evualuation & Erorr Analysis
 >
 > Download Pretraine Model From This Link [MASK-RCNN](https://github.com/matterport/Mask_RCNN/releases/download/v2.0/mask_rcnn_coco.h5) 
 > And Move/Copy This Model To Project Directory  Now We Are Ready For Next Step
 >
 > `KEYPOINT: This pretrained Mask-RCNN Is Trained On Coco Dataset Which Is One Of The Most Popular Data Set For Object Detection Task Like Classsification,Localization,Segmentation etc. This Dataset Contained Millions Of Images Of Thousand Category like Bus,Cars,Human etc. As Comapred To Most Of Stuff We See In Daily Life Plus This Dataset Overall Size Into 28 GB.`
 
`STEP :3 RUNNING INSTANCE`
  
 > Till This Step Your Installation Is Complete Now The Only Thing You Need Is Running `index.py`file by Typing 'python3 index.py' In CMD/Terminal
 > It Will Take Barely 10s And a Window Will Pop Up It Is Running instance Of What Type Of Argument You paased **0 For Your Web Came Video** Orpath to Video in single Quote **'path-to-video.mp4'** in `index.py file In `VideoCapure Function``
  
  
### 1.3 Usage:
> `Index.py`is main file which contain driver code of running segmentation model 
> 
>  You have to just Run index.py as `python3 index.py`
>
> NOTE:that All Data(Pretrained_coco_model.hs,virtualenv_folder & index.py all should be in same directory/folder)
> For Running On Video Download Any OutDoor/InDoor Video From Youtube Or any other platform And Put Downloded video in Same Folder And In`index.py` In`VideoCapture()`Function Put Path To Video In Single Quotes**'path-to-video.mp4'** in place of **0** ;0 Is For Webcame Video Processing And It Should Be placed Without Quotes **VideoCapture(0)**
  


