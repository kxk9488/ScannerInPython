import sys
global fileReader , charClass , lexeme ,nextChar ,token , nextToken 
charClass="";
lexeme ="";
nextChar="";
token = 0;
nextToken = 0;
LETTER = 0;
DIGIT = 1;
UNKNOWN = 99;
EOF = -1;
INT_LIT = 10;
IDENT = 11;
ASSIGN_OP = 20;
ADD_OP = 21;
SUB_OP = 22;
MULT_OP = 23;
DIV_OP = 24;
LEFT_PAREN = 25;
RIGHT_PAREN = 26;     

# Method to get next character from fileReader
def getChar():
    global nextChar
    nextChar = fileReader.read(1);
    global charClass
    if nextChar.isspace():
        getChar();
    if nextChar != "":
        if nextChar.isalpha():
            charClass = LETTER;
        elif nextChar.isdigit():
            charClass = DIGIT;
        else:
            charClass = UNKNOWN;

# Method to build lexeme
def addChar():
    global lexeme
    lexeme += nextChar;

def lex(): 
    global lexeme,nextToken,charClass
    lexeme = "";
    if charClass == LETTER:
        addChar();
        getChar();
        while (charClass == LETTER) or (charClass == DIGIT):
            if nextChar == "":
                charClass = EOF;
                break;
            addChar();
            getChar();
        nextToken = IDENT;
    elif charClass == DIGIT:
        addChar();
        getChar();
        while charClass == DIGIT:
            addChar();
            getChar();
        nextToken = INT_LIT;
            
    elif charClass == UNKNOWN:
        lookup(nextChar);
        getChar();
            
    elif charClass == EOF:
        nextToken = EOF;
        lexeme = "EOF";
    print "Next Token is : ", nextToken , "Next lexeme is: " , lexeme;
    return nextToken;

def lookup(ch):
    global nextToken,lexeme
    if ch == '(':
        addChar();
        nextToken=LEFT_PAREN;

    elif ch == ')':
        addChar();
        nextToken=RIGHT_PAREN;
        
    elif ch == '+':
        addChar();
        nextToken=ADD_OP;
            
    elif ch =='-':
        addChar();
        nextToken=SUB_OP; 
    elif ch == '*':
        addChar();
        nextToken=MULT_OP;
    elif ch == '/':
        addChar();
        nextToken=DIV_OP;
    else :
        addChar();
        nextToken=EOF;
        lexeme = "EOF";       
    return nextToken;

if __name__ == '__main__':
    parse = 0
    try:
        if len(sys.argv) == 2:
            fileReader = open(sys.argv[1], 'r')
            parse = 1
        elif len(sys.argv) == 1:
            fileReader = open('front.in', 'r')
            parse = 1
        else:
            print 'Usage:\n Python front.in[fileReader-to-parse(optional,default=input.txt)]'
    except IOError:
        print ("fileReader not found" , sys.argv[1])
         
    except:
        print "Unexpected Error"    
    if parse:    #Execute if parse =1 i.e., fileReader opened succesfully
        getChar();
        lex();
        while nextToken != EOF:
            lex();
        fileReader.close()