# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:07:38 2023

@author: Nic
"""

TslaPostsFile = open("TSLAPosts.txt", "a", encoding='utf-8') #encoding because people use emojis
MetaPostsFile = open("METAPosts.txt", "a", encoding='utf-8') #encoding because people use emojis
SPYpostsFile = open("SPYPosts.txt", "a", encoding='utf-8') #encoding because people use emojis
GooglePostsFile = open("GOOGLEPosts.txt", "a", encoding='utf-8') #encoding because people use emojis
ApplePostsFile = open("APPLEPosts.txt", "a", encoding='utf-8') #encoding because people use emojis



#sort based on Tesla mentions
tsla = ['tesla', 'tsla', '$tsla','$tesla', 'TESLA' , '$TSLA', 'TSLA']
tslaLen = len(tsla)
tslaPosts = []

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(tslaLen):
                if (tsla[i]) in line:
                    TslaPostsFile.write(line)
TslaPostsFile.close()


#sort based on META mentions
meta = ['META', 'meta', '$META','$meta', 'Facebook,' 'facebook', '$fb', '$FB', 'FaceBook']
metaLen = len(meta)
metaPosts = []

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(metaLen):
                if (meta[i]) in line:
                     MetaPostsFile.write(line)
MetaPostsFile.close()

#sort based on Apple mentions
apple = ['APPLE', 'apple' , '$aapl', '$AAPL']
appleLen = len(apple)
applePosts = []

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(appleLen):
                if (apple[i]) in line:
                    ApplePostsFile.write(line)
ApplePostsFile.close()

#sort based on SPY mentions
spy = ['SPY', 'spy', '$SPY', '$spy']
spyLen = len(spy)
spyPosts = []

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(spyLen):
                if (spy[i]) in line:          
                    SPYpostsFile.write(line)
SPYpostsFile.close()

#sort based on Google mentions
google = ['Google', 'google', '$googl', '$GOOGL', 'alphabet', 'ALPHABET']
googleLen = len(google)
googlePosts = []

with open('RedditPosts.txt', 'r', encoding='UTF-8') as posts:
        for line in posts:
            for i in range(googleLen):
                if (google[i]) in line:
                    GooglePostsFile.write(line)
GooglePostsFile.close()
      
