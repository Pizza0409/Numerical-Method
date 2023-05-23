#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import csv
import flet as ft


# In[2]:


# 讀資料

ticket_df = pd.read_csv('tickets.csv', header=None)
ticket = ticket_df.values
ticket_df


# In[3]:


# 南下的組合

southbound_dict = {}
for i in range(len(ticket[0])):
    for j in range(i+1, len(ticket[0])-1):
        station_1 = str(ticket[0][i+1])
        station_2 = str(ticket[0][j+1])
        southbound_dict[(station_1, station_2)] = (ticket[j+1][i+1], ticket[i+1][j+1])


# In[4]:


# 北上的組合

northbound_dict = {}
for i in range(len(ticket[0])):
    for j in range(i+1, len(ticket[0])-1):
        station_1 = str(ticket[0][-i-1])
        station_2 = str(ticket[0][-j-1])
        northbound_dict[(station_1, station_2)] = (ticket[-i-1][-j-1], ticket[-j-1][-i-1])


# In[5]:


# 站名

station = []
for i in range(1, len(ticket[0])):
    station.append(str(ticket[0][i]))


# In[6]:


# 這個function只是給大家感受一下GUI大概會怎麼被使用的樣子。接收到2個input，然後output票價的結果

def THSR_fare():
    start_station = input('Enter your start station:')
    end_station = input('Enter your end station:')
    if southbound_dict.get((start_station, end_station)) is not None:
        print(f'Southbound from {start_station} to {end_station}')
        print(f'The ticket fare of Standard Car is: {southbound_dict[start_station, end_station][0]}')
        print(f'The ticket fare of Business Car is: {southbound_dict[start_station, end_station][1]}')
    elif northbound_dict.get((start_station, end_station)) is not None:
        print(f'Northbound from {start_station} to {end_station}')
        print(f'The ticket fare of Standard Car is: {northbound_dict[start_station, end_station][0]}')
        print(f'The ticket fare of Business Car is: {northbound_dict[start_station, end_station][1]}')
    else:
        print(f'The destination from {start_station} to {end_station} is not found')


# In[7]:


THSR_fare()
# input 1 is Taipei
# input 2 is Tainan
# output:
# Southbound from Taipei to Tainan
# The ticket fare of Standard Car is: 1,350
# The ticket fare of Business Car is: 2,230


# ## 開始GUI介面實作

# ###### 大家不一定要照著下面的模板實作，只要能夠做出相同功能、相似尺寸的GUI就好

# In[8]:


def main(page: ft.Page):
    global start_station, end_station
    page.scroll = "always"


    # GUI的排版
    page.title = "Taiwan High Speed Rail Fare System"
    page.window_width = 750
    page.window_height = 600
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    button_width = 150
    button_height = 75

    start_station = ""
    end_station = ""

    # 按鈕的function
    def start_station_click(aaa):
        # 使用global變數定義start_station讓其他function也能夠使用到被更新後的同樣參數
        # 可以使用aaa.control.data抓到站名
        global start_station
        start_station = aaa.control.data
        pass
    
    def end_station_click(aaa):
        global end_station
        end_station = aaa.control.data
        pass
    
    def result_click(aaa):
        # 可參考THSR_fare()這個function去實作這邊
        fare = [0, 0]
        if southbound_dict.get((start_station, end_station)) is not None:
            fare[0] = southbound_dict[start_station, end_station][0]
            fare[1] = southbound_dict[start_station, end_station][1]
        elif northbound_dict.get((start_station, end_station)) is not None:
            fare[0] = northbound_dict[start_station, end_station][0]
            fare[1] = northbound_dict[start_station, end_station][1]
        else:
            print(f'The destination from {start_station} to {end_station} is not found')
        result_text = ft.Text(f"From {start_station} to {end_station}\nThe frare is for standard car is {fare[0]}\nThe frare is for business car is {fare[1]}", size = 16)
        page.add(result_text)
        pass

    # ------建立物件------
    start_text = ft.Text("Please select a start station", size=18)
    end_text = ft.Text("Please select a end station", size=18)
    
    # /// for start station view ///
    # 可以一個一個建立出按鈕，但也可以透過for loop 去建立出 4(column)*3(row)的樣子
    # 使用station這個參數可以抓到各個站名
    # 使用這個函數實作，參數可以自己調整，除了width
    # ft.ElevatedButton(text=f"{station[i]}", data=f"{station[i]}", width=150, on_click=start_station_click)
    num_row = 3
    num_col = 4
    
    start_button = []   
    # 創建所有站的buttons
    for i in range(len(station)):
        button_text = station[i]
        start_button.append(ft.ElevatedButton(text = button_text, data = button_text, width = 150, on_click = start_station_click))
    #呈現4 * 3 的排列
    start_grid = ft.GridView(start_button, runs_count = 4, child_aspect_ratio = 4)
    
    
    # /// for end station view ///
    end_button = []
    # 創建所有站的buttons
    for i in range(len(station)):
        button_text = station[i]
        end_button.append(ft.ElevatedButton(text = button_text, data = button_text, width = 150, on_click = end_station_click))
    #呈現4 * 3 的排列
    end_grid = ft.GridView(end_button, runs_count = 4, child_aspect_ratio = 4)           
    

    # /// for result view ///
    # 使用以下函數實作
    # ft.ElevatedButton(text=f"Calculate the fare", width=630, on_click=result_click)
    # ft.Text("")
    result_button = ft.ElevatedButton(text = "Calculates the fare", width = 630, on_click = result_click)
    result_text = ft.Text("", size = 8)


    # ------將物件進行排版------
    page.add(start_text,
             start_grid,
             end_text,
             end_grid,
             result_button,
             result_text
            )
    
ft.app(target=main)


# In[ ]:





# In[ ]:




