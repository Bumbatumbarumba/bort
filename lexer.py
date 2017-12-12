"""
Created by Bartosz Kosakowski
12/08/2017
Lexical analyzer for the bort programming language.
bort is a language of my own invention, in case you
were wondering.
"""
#regex lib
import re;

typeList = ["int", "float", "char", "string", "boolean"];

def removeWhiteSpace(text):
	splitText = text.split(" ");
	splitText = [i for i in splitText if i is not ""];
	return splitText;

#start of checking expr for var declaration
def varDec(varDec):
	splitDec = removeWhiteSpace(varDec);
	if splitDec[0] in typeList:
		type = splitDec[0];
		if name(splitDec[1]):
			if splitDec[2] is "=":
				if checkAsgnType(splitDec[3], type):
					return true;
				else:
					print("Error: type mismatch")
			else:
				print("Error: assignment operator is =");
		else:
			print("Error: invalid variable name");
	else:
		print("Error: type not declared");
	#end of varDec

#check that name matches the regex
def name(name):
	pattern = re.compile("^([A-Z]|[a-z]|_)+([A-Z]|[a-z][0-9]|_)*$");
	if re.match(pattern, name) is not None:
		return True;
	else:
		return False;
	#end of name

def checkAsgnType(rVal, varType):
	if varType in typeList:
		if varType is "string" or varType is "char":
			return char(rVal, varType);
		elif varType is "int" or varType is "float":
			return digits(rVal, varType);
		else:
			return bool(rVal);
	else:
		return false;
	#end of checkAsgnType

def char(rVal, varType):
	#if varType is char, check that length of chars is 1 and encapsulated by ""
	if varType is "char":
		if len(rVal) == 3:
			if rVal[0] is "\"" and rVal[2] is "\"":
				return True;
			else:
				return False;
		else:
			return False;
	#if varType is string, check that chars is encapsulated by ""
	if varType is "string":
		return True;
	else:
		return False;
	#end of char

def bool(rVal):
	if rVal is "true" or rVal is "false":
		return True;
	else:
		return False;

def digits(rVal, varType):
	#check if rVal is an int
	if varType is "int":
		return True;
	#check if rVal is a float
	elif varType is "float":
		return True;
	#end of digit

userin = input("enter an expr:\n");
varDec(userin);