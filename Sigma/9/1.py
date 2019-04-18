with open("te5st.txt","w") as file_text:
    file_text.write("First line\nSecond Line\nThird line")
    print("jfgukfy")
with open("te5st.txt","r") as file_text:
    all_lines = file_text.readlines()
    print(all_lines[0])
    file_text.seek(0,0)
    for line in file_text:   
        print(line, end="")