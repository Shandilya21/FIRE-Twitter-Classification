# FIRE-Twitter-Classification
Forum for Information Retrieval (FIRE): Implementation of simple machine learning model for analyses of emergency-related tweets for Classification Task.


<p align="center">
  <img src="https://github.com/Shandilya21/FIRE-Twitter-Classification/blob/master/Tweet_classification.jpg" alt="Tweet_Classification"/>
</p>


## Description 
Social media has evolved itself as a significant tool used by people for information spread during emergencies like natural or man-made disasters. Real-time analysis of this huge collected data can play a vital role in crisis assessment, response and relief activities. We present a system which analyses the emergency-related tweets to classify them as need and available tweets. The system will further give a ranked list of tweets, along with a relevance score for each tweet with respect to the topic. Finally, for each need tweet identified its corresponding mapped availability tweets are reported.

### Code Description:
As the code is very easy to follow, the main_src file is in main folder stated **Twitter_final.py**, run this script which is the main script. Save the result inn **result/** folder for named **Need_tweets.txt** and **available_tweets.txt** for further ranking. place the path in main script for data and run the below script.

```
python main/Twitter_final.py
python Rank/rank.py
```
##### Pre-Processing
All the pre-processing has been done in main Twitter_final.py, for other preprocessing scripts please check the main/ folder for pre-processing task in details. We seperately attached the script for TF-IDF Vectorizer for Rank purpose. 


#### DATA
Data of this project is downloded from [Data_Link](https://drive.google.com/open?id=1rLfHSwg18eY9gcWLN5m_5KMlVT46rKcf) and place it under the **data/** folder for processing.

```
Please feel free to contribute and raise issue
```
