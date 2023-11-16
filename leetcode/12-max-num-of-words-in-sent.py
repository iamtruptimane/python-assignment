def mostWordsFound(sentences):
    
        max = 0
      

        for sentence in sentences:
            count = 0
            arr = sentence.split()

            for words in arr:
                count = count + 1

                if max < count :
                    max = count
   
        return max
    
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))    
    
