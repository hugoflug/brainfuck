#! /usr/bin/env python
import sys

def roof(x, roof):
    if x < roof:
        return x
    else:
        return roof

# returns a visual pointer to a point in the code
def code_ptr(code, index):
    return code[index-5:index+4] + '\n' + ' '*roof((index-1), 5) + '^'

def load_code(filename):
    try:    
        f = open(sys.argv[1], 'r')
    except IOError:
        print("Couldn't read file.")
        quit()
    return f.read()

#returns an error message, or an empty string if no errors were found
def syntax_check(code):
    left_brackets = 0
    right_brackets = 0

    cpos = 0

    while cpos < len(code):
        if code[cpos] == '[':
            right_brackets += 1
        elif code[cpos] == ']':
            left_brackets += 1
        if right_brackets < left_brackets:
            return code_ptr(code, cpos) + '\n' + "Syntax error! Unmatched right bracket."
        cpos += 1

    if right_brackets != left_brackets:
        #print_code_ptr
        return "Syntax error! Unmatched left bracket."

#executes the code, returns error if there is one, otherwise an empty string
def execute(code):
    data = [0]
    dpos = 0
    cpos = 0

    while cpos < len(code):
        if code[cpos] == '>':
            dpos += 1
            if dpos >= len(data):
                data.append(0)
        elif code[cpos] == '<':
            dpos -= 1
        elif code[cpos] == '+':
            data[dpos] += 1
        elif code[cpos] == '-':
            data[dpos] -= 1
            if data[dpos] < 0:
                return code_ptr(code, cpos) + '\n' + 'Error: Negative data value (' + str(data[dpos]) + ') at memory cell ' + str(dpos) 
        elif code[cpos] == '.':
            sys.stdout.write(chr(data[dpos]))
        elif code[cpos] == ',':
            data[dpos] = ord(raw_input()[0])
        elif code[cpos] == '[' and data[dpos] == 0:
            loops = 1
            while loops != 0:
                cpos -= 1
                if code[cpos] == '[':
                    loops += 1
                elif code[cpos] == ']':
                    loops -= 1
        elif code[cpos] == ']' and data[dpos] != 0:
            loops = 1
            while loops != 0:
                cpos -= 1
                if code[cpos] == ']':
                    loops += 1
                elif code[cpos] == '[':
                    loops -= 1
        cpos += 1



if len(sys.argv) == 1:
    print("FUCKBRAIN v0.1")
    print("usage: brainfuck [-c cmd | file]")
    quit()
elif len(sys.argv) > 1:
       if sys.argv[1] == '-c':
            code = sys.argv[2]
       else:
            code = load_code(sys.argv[1])

syntax_errors = syntax_check(code)
if syntax_errors:
    print(syntax_errors)
    quit()

runtime_errors = execute(code)
if runtime_errors:
    print(runtime_errors)
    quit()

