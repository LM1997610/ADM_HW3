# ADM_HW3

Github repository to submit ADM's **Homework 3** - **[Places of the world](https://github.com/lucamaiano/ADM/tree/master/2022/Homework_3)**.<br>

Work done and compiled by **Group 29** made up of the following members:
- Luca Mazzucco 1997610 
- Maria Vittoria Vestini 1795724

<br>

The main content is in a Jupyter Notebook file named [**main.ipynb**](https://github.com/MaviVestini/ADM_HW3/blob/main/HW3_final.ipynb) which shows our results for the proposed questions.\
The code comments explain the steps and approach to building different versions of the search engine.\
The BONUS question was not answered.

#### Other contents:
- **CommandLine.sh** is a bash shell script file that calls the _places_data_.csv dataset and it contains the answer to the command line question.

- **all_places_data.tsv** document reference dataset

- **vocabulary.pkl**
this file contains a dictionary that maps each word in the corpus of documents to an integer (term_id). Needed to compute Inverted Index.

- **II.pkl** is the Inverted Index used to execute query for the first search engine

- **tfidfII.pkl** is the Inverted Index implemented with *TfIdf* used to execute query for the second search engine

- **RankingList.txt** text file that contains the resuts form the sorting of the **ApplicantsInfo.txt**

- **SingleIDFs.pkl** file that contains a dictionary that contains the IDF of all the documents

- **norms.pkl** file that contains a dictionary that contains the norms, computed with the TF-IDFs, of all the documents

# MAP
GitHub doesn't display the plot, so to view the map from point 4 we saved the file as **fig.html** and it can be seen [here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/MaviVestini/ADM_HW3/main/fig.html) 
