#!/usr/bin/python3

ori_pass = "WeHav34PythonM4st3r"
buf = []
s = input("\nPlease enter password: \n")
counter = []
correct = ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']

def pass_check():
    for i in s:
        buf.append(i)
    if len(buf) != len(ori_pass):
        print("\nSorry password length do not match, try harder!")
    else:
        for c in range(19):
            if s[c] == ori_pass[c]:
                counter.append('1')
            else:
                counter.append('0')
        print(counter)
        if counter == correct:

           flag = ['t','r','3','w','P','u','l','f','5','0','y','I','0','n','h','P']
           code =['4','10','0','14','12','13','11','8','4','2','3','2','1','7','5','6']


           for i in code:

           	number = int(i)
           	print (flag[number],end="")



        else:
            print("\nOOPSS, WRONG PASSWORD!")


pass_check()
