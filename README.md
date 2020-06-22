# LoL-Predictor

Do you want to know if you will win a game before you've played? This project aims to use PyTorch to train a deep learning model that can predict which team in the popular MMO game League of Legends.

**To read the full final report, go to: docs >> Final Report.pdf**

**Set-up**

First, ensure you have Python 3.6.8 or greater installed. Then, ensure you have PyTorch installed by running (If you have a CUDA enabled GPU, ensure to install CUDA support):

`pip install pytorch`

You can verify that PyTorch has been installed correctly by going to the Terminal/PowerShell, then running the following code:
`python`

`import torch`

If no errors appear, then PyTorch has successfully been installed.

If you wish to scrape data from the Riot Games API, you will need your own API key. If you want to use the scraping code included in this repository, then you must also install the RiotWatcher library for Python. In the terminal, type:

`pip install riotwatcher`

Once the library has been installed, clone the repository to your local computer, and open it in your text editor of choice (Note it should be able to open .py and .ipynb files)

The dataset is available here, under "datasets", or it can also be downloaded from Kaggle: https://www.kaggle.com/jamesbting/league-of-legends-ranked-match-data-from-na?rvi=1

**TRAINING**:

To get started with training, simply open the file "Model.ipynb" under the "src" folder in your Jupyter Notebook editor of choice. In the first cell, there are 5 boolean operators that correspond to different settings, each having a brief explanation. Once all your options have been set, you can run all cells to start training. The notebook will automatically detect if you have a CUDA enabled GPU enabled, and the PyTorch to support it, and if you do, it will run all calculations on the GPU.

**ACKNOWLEDGMENTS**:
This project is based on the projects done by Kenneth Hall(https://github.com/minihat/LoL-Match-Prediction), and by Thomas Huang, David Kim, and Gregory Leung (http://thomasythuang.github.io/League-Predictor/).

The RiotWatcher wrapper for the Riot API is provided here: (https://github.com/pseudonym117/Riot-Watcher).
