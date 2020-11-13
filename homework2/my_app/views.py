from django.shortcuts import render
from django.http import HttpResponse
import json
import os
import random


def main_html(request):
    return render(request, 'my_app/file.html')

def json_read(request):
    a = os.getcwd()
    with open(f'{a}\\my_app\\file.json','r') as file:
        text = json.load(file)

    html = '''
    <head>
        <title>Json</title> 
    <head>       
    <body>
        <header><img src="https://lh3.googleusercontent.com/proxy/yyQeiq0MLAXFZKhbetxK1s_h_urvG6341tvXwzwQezucSMsL5J6AevzCAMl04tINYuuWxXxZ6WXeTg9Zyw8CID3oK42cgXsMzE_tD4XfC08" width=100% height=40%></header>
        <center><h1 style="color:white; background-color:black">In this page we read json files</h1></center><br><br><br>
        <div style="color:0A108E;font-size:28px">
        <p>our dict{}</p><p>{}</p> <p>{}</p> </div>
        <a href= "http://127.0.0.1:8000/" style="color:#0B0B3B">Main page</a>
    <body>
    '''.format(text,text.keys(),text.values())
    return HttpResponse(html)



    
def task(request):
    list_1 = ["a","b","c","d"]
    list_2 = ["a","b","e","f"]
    dict_1 = {}
    dict_2 = {}
    counter = {}
    for i in list_1:
        dict_1[i] = random.randint(0,7)*100 
    for i in list_2:
        dict_2[i] = random.randint(0,7)*100 
    
    for i in dict_1:
        if i in dict_2:
            counter[i] = dict_1[i]+ dict_2[i]
        else:
            counter[i] = dict_1[i]

    for i in dict_2:
        if i not in dict_1:
            counter[i] = dict_2[i]                           




    output = '''
    <title>Great</title>
    <header style="background-color:#0C0032; color:#83C6E7"><h1>TASKS SOLUTION<h1></header>
    <body style="background-color:#190061">
        <h1><div style="background-color:#240090"><p>first dictionary {}
        </p><p>second dictionary {}</p><p>counter dictionary {}</p></div></h1><br>
        <img src="https://media4.giphy.com/media/MU4yzBETZ2tVDiCDRn/giphy.gif"width=30%>
        <h2><p>You can see <a href= "http://127.0.0.1:8000/task" style="color:#AFD275">another example</a></p>
        <p>Or go to the <a href= "http://127.0.0.1:8000/" style="color:#AFD275">Main page</a></p><h2>
    <body>
    '''.format(dict_1, dict_2, counter)

    return HttpResponse(output)


def index(request):
    return render(request, 'my_app/file.json')

