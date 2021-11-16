import os;
while True:
    input_string = input(">").split();
    if len(input_string)!= 0:
        if "clear" in input_string:
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
            print(number); 
        elif "print" in input_string[0]:
            input_string = str(input_string).replace("print(","");
            input_string = str(input_string).replace(")","");
            for i in input_string:
                if i.isalpha():
                    if input_string.index(i) == len(input_string)-3:
                        print(i);
                    else:
                        print(i,end="")
                    
    pass;