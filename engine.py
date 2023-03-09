
import re
import string
import numpy as np
import pandas as pd
from tqdm import tqdm

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class module:

    def preprocess(long_string : string ):
        
        long_string = re.sub(r'[^\w\s]','', long_string)
        final_string = long_string.translate(str.maketrans('', '', string.punctuation))
        
        tokens = final_string.replace("\n", " ").replace("\t", " ").replace('\x0c', "" ).split(" ")
        tokens = [x.lower() for x in tokens if x != '']
        
        stop = set(stopwords.words('english'))
        filtered_tokens = [w for w in tokens if not w.lower() in stop]
        
        ps = PorterStemmer()
        filtered_tokens = [ps.stem(w) for w in filtered_tokens]
        t = [item for item in filtered_tokens if item.isalpha()]

        return t
    

    def query_vectorizer( query, N: int, word_dict, IDFs):
        qqq = np.zeros(N)
        l = []

        for i in range(len(query)):
            
           idf = IDFs[word_dict[query[i]]]
           tf = query.count(query[i])/len(query) 
           l.append(tf*idf)
       
        for i in range(len(query)):
            for elem in range(len(qqq)):
                if word_dict[query[i]] == elem:
                    qqq[word_dict[query[i]]-1] = l[i]

        pos = [(x[0],round(x[1],4)) for x in enumerate(qqq) if x[1] != 0]

        return qqq, pos


    def boolean_search(query_str : str, inverted_idx : dict, word_dict : dict , data,  show = None):
            
        q = re.split(" +(AND NOT|AND|OR) +", query_str)
        queryquery = module.preprocess(query_str)
        
        if len(queryquery) != 2:
            print("Error : two term queries only")
            return
            
        operation = [q[i] for i in range(len(q)) if q[i] in  ['AND','OR', "AND NOT"]][0]
        
        try:
            result = [set(inverted_idx[item]) for item in [word_dict[word] for word in queryquery]]
            
            if operation == "AND":
                result = set.intersection(*map(set,result))

            elif operation == "OR":
                result = set.union(*map(set,result)) 

            elif operation == "AND NOT":
                result = set.difference(*map(set,result)) 

            print("\nquery : '{}'".format(query_str))
            print("\n results = {} matching documents\n".format(len(result)))
            
            if show == True:

                output = data.loc[list(result)][["placeName","placeLocation" ,"placeDesc", "placeUrl"]]

                print(" df.shape", output.shape)
                display(output.head())
                
                return output

        except KeyError: 
            print("Error: query term not in Vocabulary")
            
    
    def Search_Engine(query, II, word_dict):
        docs = []
        for word in query:
            indice = word_dict[word]
            values = dict([(key, value) for key, value in II[indice]])
            docs.append(values)
        keys_list = [list(x[0].keys()) for x in zip(docs)]
        merged_keys = set(sum(keys_list, []))
        return list(merged_keys)
    

    def retrive_matrix(indice : dict, n_docs, n_terms):

        matrice = np.zeros((n_docs, n_terms))
        print("matrice.shape :", matrice.shape)

        for i in tqdm(range(0, n_docs)):
            for term_id, postings in indice.items():
                if i in [x[0] for x in postings]:
                     new_value = [x[1] for x in postings if x[0] == i][0]
                else:
                    new_value = 0
                colonna = int(term_id-1)
                matrice[i, colonna] = new_value

        return matrice
  

    def show(dataset, ranking):
        lista = [(x[0], dataset["placeName"][x[0]], dataset["placeLocation"][x[0]], 
                        dataset["placeUrl"][x[0]], dataset["placeDesc"][x[0]],x[1]) for x in ranking[:10]]
        df = pd.DataFrame(lista)
        df.columns = ["placeIndex", "placeName", "placeLocation", "placeUrl", "placeDesc", "Score"]
        return df
    


        