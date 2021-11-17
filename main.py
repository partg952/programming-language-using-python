import os;
from playsound import playsound;
import vlc;
import pafy;
import keyboard as kb;
import multiprocessing;

previous_command = [];

def add_to_array(command):
    previous_command.append(command)


def swap(arr,first,second):
    temp = arr[first];
    arr[first] = arr[second];
    arr[second] = temp;

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
            number = 0;
            for i in input_string[0]:
                if i!="+":
                    i = int(i);
                    number = number+i;
            print(number);
        elif "-" in input_string[0]:
            number = 0;
            for i in input_string[0]:
                if i!="-":
                    i = int(i);
                    number = i-number;
            print(number*-1 ); 
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
                try:
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
                except:
                    print("something went wrong");
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
    pass;   