from flask import Flask, request,redirect,url_for, jsonify,render_template,session
from flask_mysqldb import MySQL


import numpy as np
import pickle
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


def removeHTMLTags(sentences):
    soup = BeautifulSoup(sentences, 'lxml')
    return soup.get_text()

def removeApostrophe(sentences):
    phrase = re.sub(r"won't", "will not", sentences)
    phrase = re.sub(r"can\'t", "can not", sentences)
    phrase = re.sub(r"n\'t", " not", sentences)
    phrase = re.sub(r"\'re", " are", sentences)
    phrase = re.sub(r"\'s", " is", sentences)
    phrase = re.sub(r"\'d", " would", sentences)
    phrase = re.sub(r"\'ll", " will", sentences)
    phrase = re.sub(r"\'t", " not", sentences)
    phrase = re.sub(r"\'ve", " have", sentences)
    phrase = re.sub(r"\'m", " am", sentences)
    return phrase

def removeAlphaNumericWords(sentences):
     return re.sub("\S*\d\S*", "", sentences).strip()

def removeSpecialChars(sentences):
     return re.sub('[^a-zA-Z]', ' ', sentences)

def doTextCleaning(sentences):
    sentences = removeHTMLTags(sentences)
    sentences = removeApostrophe(sentences)
    sentences = removeAlphaNumericWords(sentences)
    sentences = removeSpecialChars(sentences) 
    # Lower casing
    sentences = sentences.lower()  
    #Tokenization
    sentences = sentences.split()
    #Removing Stopwords and Lemmatization
    lmtzr = WordNetLemmatizer()
    sentences = [lmtzr.lemmatize(word, 'v') for word in sentences if not word in set(stopwords.words('english'))]
    sentences = " ".join(sentences)    
    return sentences

app = Flask(__name__)
app.secret_key = "kalai"  

#DB connection:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nlp'

mysql = MySQL(app)


model = pickle.load(open('GNmodel.pkl','rb'))
vectorizer = pickle.load(open('supervectorizer.pkl','rb'))

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM comments")
    data=cur.fetchall()
    cur.execute("SELECT count(*) FROM comments WHERE type=1")
    t1=cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM comments WHERE type=0")
    t0=cur.fetchone()[0]
    cur.close()
    return render_template('index.html',data=data,text=[t0,t1])


@app.route('/predict',methods=['POST'])
def predict():
    sentence=request.form['textData']
    normaltext=request.form['textData']
    #print(sentence)
    sentence = doTextCleaning(sentence)
    sentence = vectorizer.transform([sentence]).toarray() 
    prediction = model.predict(sentence)
    output = prediction[0]
    session['output']=str(output)
    
    #insert into comments table.
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO comments(comment,type) VALUES (%s, %s)", (normaltext, str(output)))
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)
