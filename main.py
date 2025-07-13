import fitz  # needed for reading pdf
import re  # nedded for regex functions

#The path to the pdf

path = "C:\\Users\\PC\\Downloads\\Data .pdf"
 
pattern = "Introduction"  #The string to search

#open the pdf
#saving all text to pages ( all pages)
#Create a list to store every page number of letters.
# The len of this list will give us the number of pages

page_list = []

pages = ""

with fitz.open(path) as doc:
    for page in doc:
        text = page.get_text()
        pages += text
        page_list.append(len(text))

# now open compile the pattern for regex

regexp = re.compile(pattern, re.I)

#Get the match 

match = regexp.finditer(pages)

#create a mtch list list with list of all start index in the match list

match_list = [x.start() for x in match]

#now match the first index with their respective pages in every index in the list

'''
Goes like this: 
- Iterate through range 0 to the total number of page list
- Since page_list contain a list with total number of each page,  
- add each item of the page list to variable count untill when the variable c ount is same as each item in match_list, the list containing each start index of the matched pattern letter where they are in the pdf.
- Also the count2, used as a index of the match_list and changes upon each page found, should be less than the length of match list to avoid match_list index out of range error
 
'''


count = 0
count2 = 0

for x in range(len(page_list)):
    count += page_list[x]

    if count2 > (len(match_list)-1): break

    if count > match_list[count2]:
        print(pattern, "::: Found at page:: ", x + 1)
        count2 += 1
        continue
	
