try:
    from functions import * 
except:
    from main.functions import *
try:
    from options import *
except:
    from main.options import *
#==== variablr assigning===#
speak=Function.speak
random=Function.random
apk_list=Function.launchableApplications()
print(apk_list)
def user(string):
    cmd=string
    #======= if else ladder=======#
    if "how are you" in cmd:
        return(random(hay))
    elif "hey" in cmd:
        return(random(hey))
    elif "what are you doing" in cmd:
        return(random(wayd))
    elif "battery"in cmd:
        return(Function.Battery())
    elif "the time" in cmd:
        return("The time is "+time.strftime("%I %M %p"))
    elif "the date" in cmd or "date please" in cmd:
        return("sir!"+"today's date is "+time.strftime("%A %e")+" on "+time.strftime("%B,%Y"))
    elif "stop" in cmd and"recording" in cmd:
        return(Function.stopRecording())    
    elif any(i in cmd for i in photo_lst) :
        return(Function.captureImage())
    elif any(i in cmd for i in start_audio):        
        return(Function.recordAudio())
    elif any(i in  cmd for i in start_video):
        return(Function.captureVideo())
    elif "stop" in cmd and"recording" in cmd:
        return(Function.stopRecording())
    elif "search" in cmd:
    	x=cmd.replace("search ","")	
    	Function.search(x)
    	
    elif all(i in cmd for i in["send","mail"]):
    	return(Function.sendEmail())
    	
    elif any(i in cmd for i in ["check airplane mode","check aeroplane mode"]):
    	return Function.checkAirMode()
    	
    elif any(i in cmd for i in ["airplane mode","aeroplane mode"]):
    	return Function.changeAirMode()
    
    elif any(i in cmd for i in ["change the volume","set the volume"]):    	
    	x=Function.int_checker(cmd)
    	return Function.setVolume(x)
     
    elif  any(apk_name in cmd for apk_name in apk_list):
    	Function.appLauncher(cmd)
    	  
    else:
        try:
            return(Function.wolfram(cmd))
        except:
            None

