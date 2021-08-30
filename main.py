# credits: https://github.com/inboxpraveen/recommendation-system, Kishan Lal/Krish Naik, Hybrid Recommender guy in Kaggle
import flask
import difflib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import OrderedDict 
app = flask.Flask(__name__, template_folder='templates')

df2 = pd.read_csv('./smd.csv')

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])
all_titles = set()
for i in range(len(df2['title'])): 
    all_titles.add(df2['title'][i])

def FirstKelements(arr):
    minHeap = []
    for i in range(12):
        minHeap.append(arr[i])
     
    # Loop For each element in array
    # after the kth element
    size = len(arr)
    for i in range(12, size):
        minHeap.sort(key=lambda x: x[1])
        if (minHeap[0][1] > arr[i][1]):
            continue
        else:
            minHeap.pop(0)
            minHeap.append(arr[i])
    return minHeap
    

def get_recommendations(title):
    #cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[title]
    try:
        idx = idx[-1]
    except: 
        idx = idx
    sim_scores = list(enumerate(cosine_sim2[idx]))
    ## print(sim_scores[5]) = (5, 0.025334729596907)
    ## print(sim_scores[1]) = (1, 0.06917144638660747)
    #sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    #print(sim_scores)
    #print(indices[title])
    #print(title)
    sim_scores = FirstKelements(sim_scores)
    sim_scores.reverse()
    sim_scores = sim_scores[1:]
    movie_indices = [i[0] for i in sim_scores]
    ##print(len(od))
    tit = df2['title'].iloc[movie_indices]
    dat = df2['release_date'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title','Year'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return return_df

# Set up the main route
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name']
        #m_name = m_name.title()
        #check = difflib.get_close_matches(m_name,all_titles,cutout=0.50,n=1) # all_titles ko dictionary banao 
        if m_name not in all_titles:
            return(flask.render_template('negative.html',name=m_name))
        else:
            result_final = get_recommendations(m_name)
            names = []
            dates = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                dates.append(result_final.iloc[i][1])

            return flask.render_template('positive.html',movie_names=names,movie_date=dates,search_name=m_name)

if __name__ == '__main__':
    app.run()