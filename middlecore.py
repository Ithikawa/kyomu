import argparse
import codecs
import core
import json
import re

def set_argments(input_str,pointer,target_args,raw_text):
    if re.match("^[0-9]+$",input_str):
        target_args[int(pointer)] = raw_text[int(input_str)]
    else:
        target_args[int(pointer)] = input_str
    return target_args

def main(detect_file, out_file,comic_list):
    print("throw GCP API")
    core.render_doc_text(detect_file, out_file)
    print("sucsess!!")

    with open(out_file,encoding="utf-8") as f:
        temp_str = f.read()

    re_text = re.compile(".*}\ntext:",re.MULTILINE | re.DOTALL)
    raw_text = re.sub(re_text,"",temp_str)
    splited_text = raw_text.replace("\"","").split("\n")

    add_text = ["","","",""]
    temp = 0
    print("""
0. set title
1. set illustrator
2. set circle
3. set date
4. print raw text
5. print add text
9. exit
        """)
    for i,temp_str in enumerate(splited_text):
        print(str(i) + ":" + temp_str + ", " ,end="" )
    print("")
    while temp != 9:
        del temp
        temp = input(">> ")
        if temp == "0":
            print("set title :" + add_text[0], end = "" )
            illustrator = input(" >> ")
            add_text = set_argments(illustrator,0,add_text,splited_text)
        elif temp == "1":
            print("set illustrator :" + add_text[1], end = "" )
            circle = input(" >> ")
            add_text = set_argments(circle,1,add_text,splited_text)
        elif temp == "2":
            print("set circle :" + add_text[2], end = "" )
            title = input(" >> ")
            add_text = set_argments(title,2,add_text,splited_text)
        elif temp == "3":
            print("set date :" + add_text[3], end = "" )
            year = input(" >> ")
            add_text = set_argments(year,3,add_text,splited_text)
        elif temp == "4":
            print(splited_text)
        elif temp == "5":
            print(add_text)
        elif temp == "9":
            print("NEXT")
            break
        else:
            print("choise content")

    f = codecs.open( comic_list, "a","utf-8")
    for temp_line in add_text:
        f.write( temp_line + "," )
    f.write( "\n" )
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    out_file = "rest.txt"
    comic_list = "comic_list.txt"
    args = parser.parse_args()

    parser = argparse.ArgumentParser()
    main(args.detect_file,out_file,comic_list)