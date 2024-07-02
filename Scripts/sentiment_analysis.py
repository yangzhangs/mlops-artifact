import csv
import os
import subprocess

import pymysql
from bs4 import BeautifulSoup
import re


def removeOneTag(text, tag):
    while (True):
        if text.find("<"+tag+">")==-1:
            break
        text = text[:text.find("<"+tag+">")] + text[text.find("</"+tag+">")+7:]
        #print(temp)
    return text

def preprocess_text(text):
    text = removeOneTag(text, "code")

    text = text.replace('<p>','').replace('/p','').replace(',',' ').replace('\'','').replace('\"','').replace('<>','')

    text = " ".join([line for line in text.splitlines() if line.strip()])

    soup = BeautifulSoup(text,features="lxml").get_text()

    text1 = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', soup, flags=re.MULTILINE)

    return text1


def create_csv(input_texts, input_file_path):
    with open(input_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        #csv_writer.writerow(['ID;text'])
        # Write text entries
        for text in input_texts:
            csv_writer.writerow([text.strip()])

def run_senti4sd(input_file_path, output_file_path):
    # Path to Senti4SD jar file
    senti4sd_jar_path = 'E:/senti4D/pySenti4SD/java/Senti4SD.jar'
    wordspace = 'E:/senti4D/pySenti4SD/java/dsm.bin'

    # Run Senti4SD
    cmd = [
        'java', '-jar', senti4sd_jar_path,
        '-F', 'A',
        '-i', input_file_path,
        '-W', wordspace,
        '-oc', output_file_path,
        '-vd', '600'
    ]
    #print(cmd)
    subprocess.run(cmd, check=False)

def read_csv(output_file_path):
    results = []
    with open(output_file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        # Skip header
        next(csv_reader, None)
        # Read rows
        for row in csv_reader:
            results.append(row)
    return results


if __name__ == '__main__':
    # Example usage
    conn = pymysql.connect(host='localhost', user='root', password='1234', database='mlops', charset='utf8')
    cur = conn.cursor()
    conn_i = pymysql.connect(host='localhost', user='root', password='1234', database='mlops', charset='utf8')
    cur_i = conn_i.cursor()
    input_texts = []
    try:
        query = "select Id, concat(title,body)as text from issues where sentiment is NULL order by Id"
        cur.execute(query)
        data = cur.fetchall()
        for row in data:
            print(row[0])
            preprocessed_text = preprocess_text(row[1])
            input_texts.append(preprocessed_text)
            # time.sleep(1)
    except pymysql.Error as e:
        print(e)
    conn.close()

    input_file_path = 'E:/senti4D/pySenti4SD/java/input_issue.csv'
    output_file_path = 'E:/senti4D/pySenti4SD/java/output_issue.csv'
    prediction_file_path = 'E:/senti4D/pySenti4SD/java/predictions_issue.csv'

    create_csv(input_texts, input_file_path)
    run_senti4sd(input_file_path, output_file_path)
    #subprocess.run(["bash", "cd E:/senti4D/pySenti4SD/java/"])
    #subprocess.run(["bash", 'Rscript E:/senti4D/pySenti4SD/java/classification.R E:/senti4D/pySenti4SD/java/output.csv E:/senti4D/pySenti4SD/java/predictions.csv'], check=False)

    sentiment_results = read_csv(prediction_file_path)

    print("Sentiment Analysis Results:")
    print(len(sentiment_results))
    for i in range(0,len(sentiment_results)):
        print(i)
        #print(sentiment_results[i][1])
        cur_i.execute("update issues set sentiment=\"%s\" where Id=%s"%(sentiment_results[i][1],i+1))

    conn_i.close()
