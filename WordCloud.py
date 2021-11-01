file = """
The big library was of platinum-and-teakwood. There were two occupants,
a monstrous man who wore expensive vitrilex, and a wisp of a girl in a
wheel chair. One entire wall space was taken up by a chart of the solar
system. Below the chart was the label: _Marshall Space Lines, 1990 to
2055, First In Astral Commerce_.

Spaceports, marked by red pins, dotted the entire chart. The large man
was humming as he thrust other scarlet pins into Ceres, Pallas and Juno
with such a savagery as one might use in thrusting swords.

"Feel better, dad?" The wisp of a girl was speaking. Misty locks of
sheeny hair lay on the back of the invalid chair like starclouds on a
summer night. A beautiful frame for a picture of lifeless, transparent
features.

"I ought to! It took fifty years to scalp the Thallin Starways!"
gloated Keith Randolph Marshall, looking proudly at the carmine
clusters that marked new interspace commerce lanes. "You bet! Fifty
years to skin old Rufus Thallin's hide! Why, every ship he owns is mine
now.
"""

from operator import itemgetter

def calculate_frequencies(file_content):    #file_content is a parameter, not variable
    punctuations = '''!()[]{};:'"\,<>./?@#$%^&*_~'''    #removed "-"
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",\
    "in", "there", "on", "for", "into", "like", "other", "ought", "feel", "took"]

    frequencies = {}    #dictionary, main star this function is returning

    file_content = file_content.strip("\n").replace("\n", " ")
    nopunct_file = ""       #this a still a very long string
    for char in file_content:
        if char not in punctuations:
            nopunct_file += char
    #return nopunct_file.lower() #use this to check the output of the cleaned text

    #time to make nopunct_file into a list of words
    nopunct_wordlist = nopunct_file.split()
    #print(nopunct_wordlist)    #prints a list of words from the file_content

    #time to iterate thru all words, check if alpha, check if in boring list, if yes skip, if no check if already in dict, if no dict[word] = 0, if yes dict[word] +=1
    for word in nopunct_wordlist:
        word = word.lower()
        if word.isalpha() == True:   #time to lowercase the words here
            if word not in uninteresting_words:
                if word not in frequencies.keys():
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1

    return frequencies

    #this prints an ordered list of word:frequencies
    #sorted_values= sorted(frequencies.values())
    #sorted_frequencieslist = sorted(frequencies.items(), key=itemgetter(1)) #need to toggle itemgetter module
    #print(sorted_frequencieslist)

print(calculate_frequencies(file))
===

# Here are all the installs and imports you will need for your word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


def calculate_frequencies(file_contents): #file_contents is the text file uploadde
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",\
    "in", "there", "on", "for", "into", "like", "other", "ought", "feel", "took","would", "not", "over", "away",\
    "out", "only", "through", "up", "now", "came", "about", "could", "would", "said", "back", "man", "then", "than",\
    "get", "give", "so", "one"
    ]

    # LEARNER CODE START HERE
    frequencies = {}    #dictionary, main star this function is returning

    file_contents = file_contents.strip("\n").replace("\n", " ")
    nopunct_file = ""       #this a still a very long string
    for char in file_contents:
        if char not in punctuations:
            nopunct_file += char
    #return nopunct_file.lower() #use this to check the output of the cleaned text

    #time to make nopunct_file into a list of words
    nopunct_wordlist = nopunct_file.split()
    #print(nopunct_wordlist)    #prints a list of words from the file_content

    #time to iterate thru all words, check if alpha, check if in boring list, if yes skip, if no check if already in dict, if no dict[word] = 0, if yes dict[word] +=1
    for word in nopunct_wordlist:
        word = word.lower()
        if word.isalpha() == True:   #time to lowercase the words here
            if word not in uninteresting_words:
                if word not in frequencies.keys():
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
    #return frequencies

    #this prints an ordered list of word:frequencies
    #sorted_values= sorted(frequencies.values())
    #sorted_frequencieslist = sorted(frequencies.items(), key=itemgetter(1)) #need to toggle itemgetter module
    #print(sorted_frequencieslist)

    wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
