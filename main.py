code = input("Enter code string: ")
cursor = 0
perm = code[:]
array = [][500]
from abc import ABC, abstractmethod

def convert(code):
    array= code.split()
    return array

def parseExeption(string):
    print("parse error at: " + cursor.toString() + " where is " + code[cursor] + " expecting "+ string)


def printNode(node, y):
    for i in node.nodes:
        array[cursor][y] = i.name
        printNode(i, y + 1)
        cursor + +
    for i in range len(array2d):
        for j in range len(array2d[i]):

            print(array2d[i][j], "     ")

        print()

class AbstractNode(ABC):
    nodes = []
    temp_nodes = []
    option = None

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
        return True

    def verify_and_add_token(self, index, node):
        if node.parse() is None:
            self.nodes[index] = None
            return True
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
            self.iterateCursor()
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
            self.iterateCursor()
            return True
        else:
            return False

class NonTokenNode(AbstractNode):

    def __init__(self, string):
        super(self)
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
        if self.verify_and_add_token(0, DeclNode())\
            and self.verify_and_add_token(1, DeclsNode()):
                self.set_permanent()
                return True
        else:
            return None

class DeclNode(AbstractNode):

    def name(self):
        return "Decl"

    def parse(self):
        if self.verify_and_add_token(0, TypeNode())\
            and self.verify_and_add_token(1, IDNode())\
            and self.verify_and_add_non_token_node(2, ";"):
                self.set_permanent()
                return True
        else:
            return False


class TypeNode(AbstractNode):

    def name(self):
        return "Type"

    def parse(self):
        if self.verify_and_add_token(0, BasicNode())\
            and self.verify_and_add_token(1, TypeClNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class TypeClNode(AbstractNode):

    def name(self):
        return "TypeCl"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "[")\
            and self.verify_and_add_token(1, NumNode())\
            and self.verify_and_add_non_token_node(2, "]"):
                    self.set_permanent()
                    return True
        else:
            return None


class StmtsNode(AbstractNode):

    def name(self):
        return "stmts"

    def parse(self):
        #since python uses lazy eval, this shouldnt create an infinite loop
        if self.verify_and_add_token(0, StmtNode())\
            and self.verify_and_add_token(1, StmtsNode()):
            self.set_permanent()
            return True
        else:
            return None


class StmtNode(AbstractNode):

    def name(self):
        return "Stmt"

    def parse(self):
        if self.verify_and_add_token(0, LocNode())\
            and self.verify_and_add_non_token_node(1, "=")\
            and self.verify_and_add_token(2, BoolNode())\
            and self.verify_and_add_non_token_node(3, ";"):
                    self.option = 0
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_non_token_node(0, "if")\
            and self.verify_and_add_non_token_node(1, "(")\
            and self.verify_and_add_token(2, BoolNode())\
            and self.verify_and_add_non_token_node(3, ")")\
            and self.verify_and_add_token(4, StmtNode())\
            and self.verify_and_add_non_token_node(5, "else")\
            and self.verify_and_add_token(6, StmtNode()):
                    self.option = 1
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_non_token_node(0, "while")\
            and self.verify_and_add_non_token_node(1, "(")\
            and self.verify_and_add_token(2, BoolNode())\
            and self.verify_and_add_non_token_node(3, ")")\
            and self.verify_and_add_token(3, StmtNode()):
                    self.option = 2
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_token(0, BlockNode()):
            self.option = 3
            self.set_permanent()
            return True

        else:
            return False


class IDNode(AbstractNode):
    def name(self):
        "ID"

class LocNode(AbstractNode):

    def name(self):
        return "Loc"

    def parse(self):
        if self.verify_and_add_token(0, IDNode)\
            and self.verify_and_add_token(1, LocClNode()):
                    self.set_permanent()
                    return True
        else:
            return None

class LocClNode(AbstractNode):

    def name(self):
        return "LocCl"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "[")\
            and self.verify_and_add_token(1, BoolNode())\
            and self.verify_and_add_non_token_node(2, "]")\
            and self.verify_and_add_token(3, LocClNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class BoolNode(AbstractNode):

    def name(self):
        return "Bool"

    def parse(self):
        if self.verify_and_add_token(0, JoinNode())\
            and self.verify_and_add_non_token_node(1, "||")\
            and self.verify_and_add_token(2, BoolNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class JoinNode(AbstractNode):

    def name(self):
        return "Join"

    def parse(self):
        if self.verify_and_add_token(0, EqualityNode())\
            and self.verify_and_add_non_token_node(1, "&&")\
            and self.verify_and_add_token(2, BoolNode()):
                    self.set_permanent()
                    return True
        elif self.reset()\
            and self.verify_and_add_token(0, EqualityNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class EqualityNode(AbstractNode):

    def name(self):
        return "Equality"

    def parse(self):
        if self.verify_and_add_token(0, RelNode())\
            and self.verify_and_add_token(1, EqualityClNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class EqualityClNode(AbstractNode):

    def name(self):
        return "EqualityCl"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "==")\
            and self.verify_and_add_token(1, EqualityClNode()):
                    self.set_permanent()
                    return True

        elif self.reset()\
                and self.verify_and_add_non_token_node(0, "!=")\
                and self.verify_and_add_token(1, EqualityClNode()):
                        self.set_permanent()
                        return True
        else:
            return None

class RelNode(AbstractNode):

    def name(self):
        return "Rel"

    def parse(self):
        if self.verify_and_add_token(0, ExprNode())\
            and self.verify_and_add_token(1, RelTailNode()):
                self.set_permanent()
                return True
        else:
            return False

class RelTailNode(AbstractNode):

    def name(self):
        return "RelTail"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "<")\
            and self.verify_and_add_token(1, ExprNode()):
                    self.set_permanent()
                    return True
        elif self.verify_and_add_non_token_node(0, ">")\
            and self.verify_and_add_token(1, ExprNode()):
                    self.set_permanent()
                    return True
        else:
            return None

class ExprNode(AbstractNode):

    def name(self):
        return "Expr"

    def parse(self):
        if self.verify_and_add_token(0, TermNode())\
            and self.verify_and_add_token(1, ExprTailNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class ExprTailNode(AbstractNode):

    def name(self):
        return "ExprTail"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "+")\
            and self.verify_and_add_token(1, ExprTailNode()):
                    self.set_permanent()
                    return True
        elif self.reset()\
                and self.verify_and_add_non_token_node(0, "-")\
                and self.verify_and_add_token(1, ExprTailNode()):
                        self.set_permanent()
                        return True
        else:
            return None

class TermNode(AbstractNode):

    def name(self):
        return "Term"

    def parse(self):
        if self.verify_and_add_token(0, UnaryNode())\
            and self.verify_and_add_token(1, TermTailNode):
                    self.set_permanent()
                    return True
        else:
            return False

class TermTailNode(AbstractNode):

    def name(self):
        return "TermTail"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "*")\
            and self.verify_and_add_token(1, TermNode()):
                    self.set_permanent()
                    return True

        elif self.reset()\
                and self.verify_and_add_non_token_node(0, "/") \
                and self.verify_and_add_token(1, TermNode()):
                        self.set_permanent()
                        return True
        else:
            return None

class UnaryNode(AbstractNode):

    def name(self):
        return "Unary"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "!")\
            and self.verify_and_add_token(1, UnaryNode):
                    self.set_permanent()
                    return True


        elif self.reset()\
                and self.verify_and_add_non_token_node(0, "-") \
                and self.verify_and_add_token(1, UnaryNode):
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_token(0, FactorNode()):
                    self.set_permanent()
                    return True
        else:
            return False


class FactorNode(AbstractNode):

    def name(self):
        return "Factor"

    def parse(self):
        if self.verify_and_add_non_token_node(0, "(")\
            and self.verify_and_add_token(1, BoolNode)\
            and self.verify_and_add_non_token_node(2, ")"):
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_token(0, LocNode):
                    self.set_permanent()
                    return True

        elif self.reset()\
            and self.verify_and_add_non_token_node(0, FactorValNode()):
                    self.set_permanent()
                    return True
        else:
            return False

class FactorValNode(AbstractNode):

    def name(self):
        return "FactorVal"

    def parse(self):
        val = code[cursor]
