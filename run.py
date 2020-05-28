#! /usr/bin/env python3
import os
import requests

dir = r"/home/student-02-e4328ec36fb1/data/feedback"
post_url = "http://35.226.35.86/feedback/"

def processFiles(dir, post_url):
    """iterate over all text files in directory"""
    for file in os.listdir(dir):  # iterate over the dir
        f, e = os.path.splitext(file)  # find out the file extension
        if e == ".txt":  # if it's a text file
            dict = convertToDict(file)  # convert the file to the dict
            response = requests.post(post_url, json=dict)  # make a POST request
            if response.status_code == "status_code_201":
                print("Successfully posted {}".format(file))
            else:
                print("Failed {}".format(response.status_code))

def convertToDict(file):
    """convert text file to a dictionary"""
    dict = {}
    with open(dir+"/"+file, 'r') as f:
        dict['title'] = f.readline()
        dict['name'] = f.readline()
        dict['date'] = f.readline()
        dict['feedback'] = f.readline()
    return dict

processFiles(dir, post_url)