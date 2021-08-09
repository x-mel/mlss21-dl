#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 5 06:59:04 2021

@author: mel
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


from time import sleep
import sys
import os
import re

def start_chrome():

    user_agent='user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    options = webdriver.ChromeOptions()

    options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument('window-size=800x600')
    options.add_argument('headless')
    options.add_argument(user_agent)

    driver = webdriver.Chrome(options=options)
    print("Started headless chrome", flush=True)
    return(driver)


def get_download_link(url):
    
    email_field='//*[@id="enrollment-form"]/div[1]/input'
    name_field='//*[@id="enrollment-form"]/div[2]/input'
    submit_button='//*[@id="enrollment-form"]/input'
    video_xpath='//*[@id="player_1"]/div[2]/div[4]/video'
    
    cred_email='blank'
    cred_name = 'blank'
    
    # We start the driver
    driver = start_chrome()
    wait = WebDriverWait(driver, 30)
    
    driver.get(url)
    
    wait.until(EC.presence_of_element_located((By.XPATH, email_field)))
    
    email= driver.find_element_by_xpath(email_field)
    name = driver.find_element_by_xpath(name_field)
    submit= driver.find_element_by_xpath(submit_button)
    
    email.send_keys(cred_email)
    name.send_keys(cred_name)
    
    submit.click()
    wait.until(EC.presence_of_element_located((By.XPATH, video_xpath)))
    
    sleep(10)
    video = driver.find_element_by_xpath(video_xpath)
    download_link = video.get_attribute("src")
    
    driver.quit()
    return download_link

lectures= {'0802': [
    
                        {
                            'speaker': 'Yuh-Jye Lee',
                            'title': 'Opening',
                            'link': 'https://webinar.tapmeetinglive.com/events/Opening',
                        }, 
    
    
                        {
                            'speaker': 'Csaba Szepesvari',
                            'title': 'Large scale learning and planning in reinforcement learning',
                            'link': 'https://webinar.tapmeetinglive.com/events/Csaba_Szepesvari',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0802-Csaba-Szepesvari_v2.pdf'
                        }, 
                     {
                        'speaker': 'Jason Ma',
                        'title': 'Google Efforts on AI Research and Talent Development',
                        'link': 'https://webinar.tapmeetinglive.com/events/Industry0802',

                    },   
                        {
                            'speaker': 'Hsuan-Tien Lin',
                            'title': 'Large scale learning and planning in reinforcement learning',
                            'link': 'https://webinar.tapmeetinglive.com/events/Hsuan_Tien_Lin',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0802-Hsuan-Tien-Lin.pdf'

                        }],
    
            '0803': [{
                            'speaker': 'Jason Lee',
                            'title': 'Theory of deep learning',
                            'link': 'https://webinar.tapmeetinglive.com/events/Jason_Lee',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0803-Jason-Lee.pdf'
                        },
                        {
                            'speaker': 'Shou-De Lin',
                            'title': 'Machine Learning as a Services Challenges and Opportunities',
                            'link': 'https://webinar.tapmeetinglive.com/events/Industry0803',
                        },     
                        {
                            'speaker': 'Arthur Gretton',
                            'title': 'Probability Divergences and Generative Models',
                            'link': 'https://webinar.tapmeetinglive.com/events/Arthur_Gretton',
                        },   
                
                ],
       
            '0804': [{
                            'speaker': 'Henry Kautz',
                            'title': 'Neuro-symbolic systems and the history of AI',
                            'link': 'https://webinar.tapmeetinglive.com/events/Henry_Kautz',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0804-Henry-Kautz.pdf'
                        }, 
    
                        {
                            'speaker': 'Chun-Yi Lee',
                            'title': 'Fundamentals and Applications of Deep Reinforcement Learning',
                            'link': 'https://webinar.tapmeetinglive.com/events/Chun_Yi_Lee',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/20210804_MLSS_Presentation.pdf'
                        },
                        {
                                                
                            'speaker': 'Johnny Tseng',
                            'title': 'Transform the Beauty Industry through AI AR Perfect Corp Innovative Vision into the Digital Era',
                            'link': 'https://webinar.tapmeetinglive.com/events/Industry0804',
                        },   
                        {
                                                
                            'speaker': 'Marco Cuturi',
                            'title': 'Optimal transport',
                            'link': 'https://webinar.tapmeetinglive.com/events/Marco_Cuturi',
                        },                   
                                                
                        ]
            ,             
            '0805': [{
                            'speaker': 'Kai-Wei Chang',
                            'title': 'Bias and Fairness in NLP',
                            'link': 'https://webinar.tapmeetinglive.com/events/Kai_Wei_Chang',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0805-Kai-Wei-Chang_compressed.pdf'
                        }, 
                        {
                                                
                            'speaker': 'David Lee',
                            'title': 'Developing a World-Class AI Facial Recognition Solution - CyberLink FaceMe',
                            'link': 'https://webinar.tapmeetinglive.com/events/Industry0805',
                        },        
                        {
                            'speaker': 'Cho-Jui Hsieh',
                            'title': 'Neural Architecture Search and AutoML',
                            'link': 'https://webinar.tapmeetinglive.com/events/Cho_Jui_Hsieh',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0805-Cho-Jui-Hsieh_v2.pdf'
                        }], 
            '0806': [{
                            'speaker': 'Pin-Yu Chen',
                            'title': 'Holistic Adversarial Robustness for Deep Learning',
                            'link': 'https://webinar.tapmeetinglive.com/events/Pin_Yu_Chen',
                            'handout': 'http://ai.ntu.edu.tw/mlss2021/wp-content/uploads/2021/08/0806-Pin-Yu-Chen.pdf'
                        },
                        {
                                                
                            'speaker': 'Industry Talks',
                            'title': 'Advantech - Compal Electronics - Taiwwan Shin Kong Security - Vizuro Taiwan',
                            'link': 'https://webinar.tapmeetinglive.com/events/Industry0806',
                        },  
                ]
    }


for day in lectures.keys():
    for session in lectures[day]:
        video_url = get_download_link(session['link'])
        file_name = '{}-{}_{}.mp4'.format(day, session['speaker'], session['title'])
        print('********'*9, flush=True)
        
        if 'handout' in session:
            print("Downloading Handout")
            os.system('curl -C - -L -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36" -H "Cookie: allow-download=1" -O "%s" '  %(session['handout']))

        print("Downloading Video:", file_name, flush=True)
        
        print('********'*9, flush=True)
        os.system('curl "%s" -C - -L -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.25 Safari/537.36" -H "Cookie: allow-download=1" -o "%s"' %(video_url, file_name))
        print('---------'*9, flush=True)

