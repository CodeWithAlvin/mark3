#====imports======#
try:
    from functions import recognizer
except:
    from main.functions import recognizer
    	
    	
def VoiceInput():
    return(recognizer())
    
def TextInput():
    return(input("query : "))
