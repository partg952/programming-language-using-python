import os;
from playsound import playsound;
import vlc;
import pafy;
import keyboard as kb;
import multiprocessing;
import operator;
var_array = {};
class Variable:
    name = '';
   
    def __init__(self,name,value):
        self.name = name;
        self.value = value;



    def assign_variable(self):
        name = self.name;
        self.name = self.value;
        print("assigned",self.value,"to",name);
        var_array[name] = self.value;
        print(var_array);


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

def calculate(input_string,operator,number):
    arr = [];
    string = ''
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
    input_string = input("reset > ").split();
                                 
    if len(input_string)!= 0:
        add_to_array(str(input_string).replace("[","").replace(']',''))    
        if "clear" in input_string:
              if os.name == 'nt':
                   os.system("cls")
              else:
                   os.system("clear")    
        elif "+" in input_string[0]:
            print(calculate(input_string,"+",0))
        elif "-" in input_string[0]:
           print(calculate(input_string,"-",0)*-1)   
        elif "*" in input_string[0]:
            print(calculate(input_string,"*",1))
        elif "/" in input_string[0]:
            input_string[0] = input_string[0][::-1]
            print(calculate(input_string,"/",1))        
        elif "print" in input_string[0]:
            is_present = False;
            if '"' in  input_string[0]:
                is_present = True;
            input_string[0] = str(input_string[0]).replace('print(',"").replace('"','')
  
            input_string[len(input_string)-1] = str(input_string[len(input_string)-1]).replace(')',"").replace('"','')
            for i in input_string:
                if i in var_array.keys() and is_present == False:
                    if i == input_string[-1]:
                        print(var_array[i],end="\n")
                    else:
                        print(var_array[i],end=" ")
                else:
                    if i == input_string[-1]:
                        print(i,end="\n")
                    else:
                        print(i,end=" ")
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
        elif "=" in input_string[0]:
            arr = [];
            string = ''
            number = 0;
            for i in range(len(input_string[0])):
                if i == len(input_string[0])-1:                    
                    string = string+input_string[0][i]
                    arr.append(string)
                    string = '';
                elif input_string[0][i] != "=":
                    string = string+input_string[0][i]
                else:
                    arr.append(string)
                    string = '';

            var = Variable(arr[0],arr[1]);
            var.assign_variable();

    pass;   