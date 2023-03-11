# ADM : HomeWork 3

Github repository to submit [**ADM**](http://aris.me/index.php/data-mining-ds-2022)'s **HomeWork 3** - **[Places of the world](https://github.com/lucamaiano/ADM/tree/master/2022/Homework_3)**.<br>

Work done and compiled by **Group 29** made up of the following members:
- Luca Mazzucco : 1997610 
- Maria Vittoria Vestini : 1795724

The main content is a Jupyter Notebook file named [**HW_3.ipynb**](https://nbviewer.org/github/LM1997610/ADM_HW3/blob/main/HW_3.ipynb) which shows our results for the proposed questions.\
The code comments explain the steps and approach to develop three different types of **Search Engines**:

- **Boolean Search Engine** : The first included is a basic search engine that allows users to perform boolean queries. It relies on simple text matching to identify relevant results
 
- **TF-IDF Search Engine** : The second uses the tf-idf algorithm to rank the relevance of search results.\
It takes into account both the frequency of the search term in the document and the inverse document frequency,\
&emsp; which is a measure of how common the search term is across the entire corpus of documents.

- **Location-Based Search Engine** : The third search engine is designed to integrate boolean queries with the user's location to provide location-based results.

The BONUS question was not answered.

### Other contents:

- **engine.py** →  **Heart** of the search engine:\
&ensp; It contains a `class` that includes needed functions for **text preprocessing** and\
&ensp;  and **results retrieving** from **inverted indexes**.

- **AlgorithmicQ_CommandLine.ipynb** → shows results for Algorithmic Question and Command Line

- **CommandLine.sh** → is the bash shell script file for the **CommandLine Question**.

## **NOTE :**
GitHub doesn't display interactive **maps** for task number 4, suggested to have a look [here](https://nbviewer.org/github/LM1997610/ADM_HW3/blob/main/HW_3.ipynb) instead
