#=====importing======#
import main.input_ as input_
import main.process as process
import main.functions as functions
import main.assistant_info as assistant_info

#====variable assigning===#
speak=functions.Function.speak
exit_cmd=["exit","close","quit"]

functions.Function.clear()
speak(functions.Function.wishme())

#====taking Input  & processing output=====#

while True:
    cmd=input_.VoiceInput() 
    if cmd==None:
        continue
    elif any(i in cmd for i in exit_cmd):        
        break    
    output=process.user(cmd)
    print(f"me : {cmd}")
    print(f"{assistant_info.name} : {output}\n")
    speak(output)
    
   



