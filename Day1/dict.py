nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
'eleven': 11, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100,
'thousand': 1000, 'lakh': 100000, 'crore': 10000000}

numWord = str(input('Enter a number in words: '))
wordList = numWord.split()
if(len(wordList)==1):
    print(nums[numWord])
elif(len(wordList)==2):
    print(nums[(wordList[0])] + nums[(wordList[1])])
else:
    num = 0
    for i in range(len(wordList)):
        if(wordList[i] == 'and'):
            pass
        elif(wordList[i] == 'thousand' or wordList[i] == 'lakh' or wordList[i] == 'crore'):
            if(i>1 and nums[(wordList[i-2])] > 10 and nums[(wordList[i-2])] <= 90):
                num = num + ((nums[(wordList[i-2])] + nums[(wordList[i-1])]) * nums[(wordList[1])])
            else:
                num = num + (nums[(wordList[i-1])] * nums[(wordList[i])])
        elif(wordList[i] == 'hundred'):
            num = num + (nums[(wordList[i-1])] * nums[(wordList[i])])
            if(i+3 == len(wordList)):
                num = num + nums[(wordList[i+2])] + nums[(wordList[i+3])]
            else:
                num = num + nums[(wordList[i+2])]
    print(num)