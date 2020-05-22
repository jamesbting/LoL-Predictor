# LoL-Predictor
This project aims to use PyTorch to train a deep learning model that can predict which team in the popular MMO game League of Legends.

*To read the full final report, go to: docs >> Final Report.pdf*

*RESULTS*
The model is able to predict with approximately 60 - 65% accuracy by only including pre-match data such as Champion mastery, and summoner spells. This is better than the 50% you would be able to achieve by choosing Blue Team every time, but it is not reliable enough to say, place a bet.

However, when including post-match data, the validation accuracy jumps to approximately >= 95%. This shouldn't be a surprise however, as teams that perform better tend to win more games.

*ACKNOWLEDGMENTS:*
This project is based on the projects done by Ken Hall(https://github.com/minihat/LoL-Match-Prediction), and by Thomas Huang, David Kim, and Gregory Leung (http://thomasythuang.github.io/League-Predictor/).

The RiotWatcher wrapper for the Riot API is provided here: (https://github.com/pseudonym117/Riot-Watcher).

