#! /usr/bin/env python
#TODO choosing size of memory
#TODO optimizations

import sys

out_filename = ""

if len(sys.argv) == 1:
    print("bftoc")
    print("usage: bftoc [file] [output filename]")
    quit()
elif len(sys.argv) > 1:
    filename = sys.argv[1]
if len(sys.argv) > 2:
    out_filename = sys.argv[2] 

try:    
    f = open(filename, "r")
except IOError:
    print("Couldn't read file.")
    quit()
bf_code = f.read()
f.close()

c_code = "int main() { \n\
                char m[1000] = {0}; \n\
                char* p = m;"

for c in bf_code:
    if c == ">":
        c_code += "p++;"
    elif c == "<":
        c_code += 'p--;'
    elif c == "+":
        c_code += "(*p)++;"
    elif c == "-":
        c_code += "(*p)--;"
    elif c == ".":
        c_code += "putchar(*p);"
    elif c == ",":
        c_code += "*p = getchar();"
    elif c == "[":
        c_code += "while (*p) {"
    elif c == "]":
        c_code += '}'

c_code += '}'

if out_filename == "":           
    out_filename = filename.replace(".bf","") + ".c"
f = open(out_filename, 'w')
f.write(c_code)
f.close()
