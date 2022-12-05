code = input("Enter code string: ")
cursor = 0
perm = code[:]
from abc import ABC, abstractmethod


def parseExeption(string):
    print("parse error at: " + cursor.toString() + " where is " + code[cursor] + " expecting "+ string)

class AbstractNode(ABC):
    nodes = []
    temp_nodes = []

    def __init__(self):
        self.initial_cursor = cursor

    def set_permanent(self):
        self.nodes = self.temp_nodes
        for i in self.nodes:
            if i is None:
                del self.nodes[i]

    @property
    @abstractmethod
    def name(self):
        pass

    def reset(self):
        self.temp_nodes.clear()
        global cursor
        cursor = self.initial_cursor

    def verify_and_add_token(self, index, node):
        if node.parse():
            self.temp_nodes[index] = node
            return True
        else:
            return False

    def iterate_cursor(self):
        cursor += 1
        return True

    def verify_and_add_non_token_node(self, index, string):
        if code[cursor] is string:
            self.nodes[index] = NonTokenNode(string)
            iterateCursor()
            return True
        else:
            return False


    @abstractmethod
    def parse(self):
        ...
    #for final project:
    #@abstractmethod
    #def evaluate(self)

class BasicNode(AbstractNode):

    basic = {"int", "bool", "char", "double"}

    def name(self):
        return "BASIC"

    def parse(self):
        token = code[cursor]
        if token in self.basic:
            self.nodes[0] = token
            self.nodes[1] =  code[cursor]
            iterateCursor()
            return True
        else:
            return False

class NonTokenNode(AbstractNode):

    def __init__(self, string):
        self.nodes[0] = string

    def name(self):
        return "Non-token"


class BlockNode(AbstractNode):

    def name(self):
        return "Block"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "{")\
            and self.verify_and_add_token(1, DeclsNode())\
            and self.verify_and_add_token(2, StmtsNode()):
                    self.set_permanent()
                    return True
        else:
            return False


class DeclsNode(AbstractNode):

    def name(self):
        return "Decls"

    def parse(self):



class StmtsNode(AbstractNode):




def removeToBookmark():
    global cursor
    i = input.len - 1
    while(input[i] is not (1, "bookmark")):
        if i is 0:
            error(cursor)
        if code[i][0] is not 0:
            del input[i]
    del code[i]
    cursor = i

def error(pos):
    print("Error at: " + pos + " Where this token is" + perm[pos])
    exit(1)

def iterateCursor():
    cursor += 1
    return True #yes, this is to iterate cursor in if statement ;)

def block(start):
    global cursor
    pos = cursor
    if code[cursor] is (0,"{")\
        and iterateCursor()\
        and decls(start+1)\
        and stmts(start+1)\
        and code[cursor] is (0,"{"):
            iterateCursor()     #iterate since token { parsed verified
            code.insert(pos, (1, "block", start))
    else:
        error(cursor)

def decls(start):
    pos = cursor
    code.insert(cursor, (1, "bookmark"))
    if decl(start+1):
        code.insert(pos, (1, "decls", start))
        iterateCursor()
        decls(start + 1)
    else:
        return True

def decl(start):
    code.insert(cursor, (1, "decl", start))
    return myTypeFun(start + 1)

def myTypeFun():
    pos = cursor
    if code

def isBASIC():
    
removeToBookmark()

