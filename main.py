import os;
from playsound import playsound;
import vlc;
import pafy;
import keyboard as kb;
import multiprocessing;
import operator;


previous_command = [];
command_summary = [
    'prev - to check previous command entered',
    'clear - to clear the screen',
    'num + num - to add the numbers',
    'num - num - to subtract the numbers',
    'play /path/to/the/song.mp3 - plays the specified song',
    'youtube video-link - opens the youtube video on vlc player',
    'sort(num1,num2,num3) - to sort the numbers',
    'print(statement) - to print a specific statement'
]

signs = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}



def add_to_array(command):
    previous_command.append(command)


def swap(arr,first,second):
    temp = arr[first];
    arr[first] = arr[second];
    arr[second] = temp;

def calculate(input_string,operator):
    arr = [];
    string = ''
    number = 0;
    for i in range(len(input_string[0])):
        if i == len(input_string[0])-1:                    
            string = string+input_string[0][i]
            arr.append(int(string))
            string = '';
        elif input_string[0][i] != operator:
            string = string+input_string[0][i]
        else:
            arr.append(int(string))
            string = '';
    
    for i in arr:
                number = signs[operator](i,number);          
    return number;
while True:
    input_string = input(">").split();
                                 
    if len(input_string)!= 0:
        add_to_array(str(input_string).replace("[","").replace(']',''))    
        if "clear" in input_string:
              if os.name == 'nt':
                   os.system("cls")
              else:
                   os.system("clear")    
        elif "+" in input_string[0]:
            print(calculate(input_string,"+"))
        elif "-" in input_string[0]:
           print(calculate(input_string,"-")*-1)    
        elif "print" in input_string[0]:
            input_string = str(input_string).replace("print(","");
            input_string = str(input_string).replace(")","");
            for i in input_string:
                if i.isalpha():
                    print(i,end="")
            print("\n")        
        elif "sort" in input_string[0]:
            arr = [];
            for i in input_string[0]:
                if i.isdigit():
                    arr.append(int(i));
            for i in range(0,len(arr)-1):
                for j in range(len(arr)-1):
                    if arr[j] > arr[j+1]:
                        swap(arr,j,j+1)
            print(arr);
        
        elif "play" in input_string[0]:
            if ("mp3" or "wav") in input_string[1]:
                    process = multiprocessing.Process(target=playsound,args=(input_string[1],))
                    process.start()
                    while True:
                        response = input("Do You Want to Stop the music > ");
                        if len(response) != 0:
                            if response  == "no":
                                pass;
                            elif response == "yes":
                                process.terminate()
                                break;
                            else:
                                print("invalid response") 
                                pass;      
                        else:
                            pass;  
                
        elif "youtube" in input_string[0]:
            likeCount = []
            if "youtube.com" in input_string[1]:
                video = pafy.new(input_string[1])
                best = video.getbest()
                media = vlc.MediaPlayer(best.url)
                media.play()     
                while True:
                    response = input("Do You want to pause the video > ") 
                    if len(response)!=0:
                        if response == "no":
                            pass;
                        elif response == "yes":
                            media.stop()
                            break;
                    else:
                        pass;    
        elif "prev" in input_string:
            for  i in previous_command:
                print(i);     
        elif "help" in input_string:
                for i in command_summary:
                    print(i);            
    pass;   