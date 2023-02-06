# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:07:38 2023

@author: Nic
"""
tsla = ['tesla', 'tsla', '$tsla','$tesla']
tslaLen = len(tsla)

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(tslaLen):
                if (tsla[i]) in line:
                    print (line)
 