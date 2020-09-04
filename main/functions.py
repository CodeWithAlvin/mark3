#=====imports=====#
import androidhelper
print("Starting jarvis")
import datetime,time
import random
import os
import wolframalpha
try:
	import assistant_info
except:
	import main.assistant_info as assistant_info

dr=androidhelper.Android()	

 #==recognize speech==#
def recognizer():
    while dr.ttsIsSpeaking().result:            
        time.sleep(1)
    return dr.recognizeSpeech("listening").result        
  
#====function class====#	
class Function:
    def clear():
        os.system("clear")
    #==speak==#
    def speak(str):
        return dr.ttsSpeak(str)	   

    def random(lis):
        return random.choice(lis)
        #==func for wish ==#
    def wishme():
        hour= datetime.datetime.now().hour
        Function.speak("WelcomeBack sir! ")
        time.sleep(2)
        if hour>= 0 and hour< 12:
            return("Good morning ")
        elif hour<= 12 and hour> 16:
            return("Good afternoon")
        else:
            return("Good evening")     
            #integer taker
    def int_checker(string):
        lis=string.split()        
        for item in lis[1:len(lis)]:
            if item.isdigit():
                value=int(item)
                return(value)
                                
    #===send mail===#
    def sendEmail():        
        reciver=Function.speak("reciver address")and recognizer()      
        subject=Function.speak('subject please') and recognizer()
        body=Function.speak('body please') and recognizer()
        dr.sendEmail((str(reciver+"@gmail.com")),(str(subject)),(str(body)))
        stopper=input("enter to continue")
        return ("send succesfully")

    #====change Air Mode====#
    def changeAirMode():
        dr.toggleAirplaneMode()
        return("changed succesfully")
        
    #===check air mode===#    
    def checkAirMode():
        airmode=dr.checkAirplaneMode().result
        if airmode==False :
            return('aeroplane mode is off')
        elif airmode==True:
            return('aeroplane mode is onn')
    
    #====send sms====#
    def sendSms():
        reciver= Function.speak('recivers number') and recognizer().result
        body=Function.speak('body please') and recognizer().result
        dr.smsSend((str(reciver)),(str(body)))
    
    #====location====#
    def location_offline():
        locate=dr.getLastKnownLocation().result
        return(locate)
        typ=locate.get("passive")
        latitude=typ.get("latitude")
        longitude=typ.get("longitude")   
        return(latitude,longitude)
    
    #==apk opener==#
    def appLauncher(string) : 
        apk_dict=dr.getLaunchableApplications().result
        alphalower = {k.lower(): v for k, v in apk_dict.items()}             
        app_name=[k for k in alphalower.keys() if k in string]       	
        try:           
            dr.launch(alphalower.get(app_name[0]))
            inp=input("enter to continue\n")
        except:
            None
    
    #==get app names==#
    def launchableApplications():
        apk_dict=dr.getLaunchableApplications().result.keys()
        alphlower = [apk_name.lower() for apk_name in apk_dict]
        return alphlower
     
    #==== capture image====#                
    def captureImage():
        dr.cameraCapturePicture("/storage/emulated/0/"+str(datetime.datetime.now())+".jpg")
        return('captured successfully in internal storage')
   
   #===video recorder===(low quality)#
    def captureVideo():
        dr.recorderStartVideo('/storage/emulated/0/'+str(datetime.datetime.now())+".mp4",0,10000000000)
        return("your vedio will be saved in internal storage")
    
    #==== record audio===#
    def recordAudio():
        dr.recorderStartMicrophone('/storage/emulated/0/'+str(datetime.datetime.now())+".mp3")
        return("your audio will be saved in  internal storage")
    
    #===stop recording===#
    def stopRecording():                    
        try:
            dr.recorderStop()
            return("recording stoped")
        except:
            return("you doesnt start recording")        
    
    #===search===#
    def search(x):
        dr.search(x)
        stopper=input("enter to continue")
        
    #===set volume===#
    def setVolume(x):
        dr.setRingerVolume(x)
        dr.setMediaVolume(x)
    
    #===battery status===#
    def Battery():
        dr.batteryStartMonitoring()
        data=dr.readBatteryData().result             
        temp=int(data.get("temperature"))
        temp=temp/10
        level=data.get("level")
        return(f"Battery level is {level} percent and temperature is {temp} °Celcius")
        dr.batteryStopMonitoring()
   
    def wolfram(cmd):
        key="T7JEE3-8VXU93896P" 
        client=wolframalpha.Client(key)
        res=client.query(cmd)
        answer=next(res.results).text
        return(answer)
        
try:
	Function.Battery()
except:
	None
			
print("==============================")
print("Here we Go")										
									
											