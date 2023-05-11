from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

csv_path = os.path.join(os.path.dirname(__file__), "database2.csv")
df = pd.read_csv(csv_path)

@app.route("/", methods=["GET","POST"])
def index2():
    if request.method=="POST":
        return render_template("index2.html", pred = prediction)
    else:
        return render_template("index2.html")

@app.route('/company_info', methods=['GET', 'POST'])
def company_info():
    categories = df['Category'].unique()  
    companies = df['Company'].unique()  

    if request.method == 'POST':
        #category = request.form['category']
        company_name1 = request.form['company_name1']
        company_data1 = df[(df['Company'] == company_name1)]
        descricao1 = company_data1['Description'].values[0]
        nota1 = company_data1['Rating'].values[0]
        categoria1 = company_data1['Category'].values[0]
        response_rate1 = company_data1['Response Rate'].values[0]
        avg_response_rate1 = company_data1['Average Response Rate'].values[0]
        solution_rate1 = company_data1['Solution Rate'].values[0]
        avg_evaluation1 = company_data1['Average Avaluation'].values[0]
        customer_retention1 = company_data1['Customer Retention'].values[0]
        
        company_name2 = request.form['company_name2']
        company_data2 = df[(df['Company'] == company_name2)]
        descricao2 = company_data2['Description'].values[0]
        nota2 = company_data2['Rating'].values[0]
        categoria2 = company_data2['Category'].values[0]
        response_rate2 = company_data2['Response Rate'].values[0]
        avg_response_rate2 = company_data2['Average Response Rate'].values[0]
        solution_rate2 = company_data2['Solution Rate'].values[0]
        avg_evaluation2 = company_data2['Average Avaluation'].values[0]
        customer_retention2 = company_data2['Customer Retention'].values[0]
        
        return render_template('company_info.html', 
                               categories=categories,
                               companies=companies,
                               company_name1=company_name1, 
                               descricao1=descricao1, nota1=nota1, categoria1=categoria1, 
                               response_rate1=response_rate1, avg_response_rate1=avg_response_rate1, 
                               solution_rate1=solution_rate1, avg_evaluation1=avg_evaluation1, 
                               customer_retention1=customer_retention1,
                               company_name2=company_name2, 
                               descricao2=descricao2, nota2=nota2, categoria2=categoria2,
                               response_rate2=response_rate2, avg_response_rate2=avg_response_rate2, 
                               solution_rate2=solution_rate2, avg_evaluation2=avg_evaluation2, 
                               customer_retention2=customer_retention2)
    
    return render_template('company_info.html', categories=categories, companies=companies)

def get_unique_categories():
    return df['Category'].unique()

def get_unique_companies(category):
    return df[df['Category'] == category]['Company'].unique()

@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'POST':
        selected_category = request.form['category']
        unique_companies = get_unique_companies(selected_category)
    else:
        selected_category = None
        unique_companies = []

    unique_categories = get_unique_categories()

    return render_template('categories.html',
                           categories=unique_categories,
                           selected_category=selected_category,
                           companies=unique_companies)

@app.route("/contacts", methods=["GET","POST"])
def contacts():
    if request.method=="POST":
        return render_template("contacts.html", pred = prediction)
    else:
        return render_template("contacts.html")

if __name__ == "__main__":
    app.run(port = 8000, debug=True)