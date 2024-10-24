# PersonalizedMusicRecommender

## DataFiles
The final dataset utilized for music retrieval is a dataset of 1.2 Million Spotify song URIs obtained from: https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs
Note that we did not pull any of the additional columns the dataset provides only the Song URIs and Song Titles.
The original Dataset was split utilizing Split.py to generate the final 12 output files.

##PythonMusicDownloaders
The deprecated files were a result from us beginning with the 1 Million playlist challenge dataset from AICrowd. Downloader.py calls the spotdl install to download all 1.2 million songs into a music folder included in the same repository. This folder is not included on the GitHub code submission.
