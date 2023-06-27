f=open("paragraph.txt","wt")
List=["The purpose of a paragraph is to express a speakers thoughts on a particular point in a clear way that is unique and specific to that paragraph . In other words  , paragraphs shouldn't be mixing thoughts or idea . When a new idea is introduce , generally , a writer will introduce a new paragraph . Paragraphs provide structure and flow to your text . And random paragraph allow you to move from one thought to another . When you start a new paragraph you are telling your reader that the topic is over and you are moving on . Without this structure , your brilliant ideas and your sound argumentation will be difficult to follow . One of the best way to get started with your paragraph phrasing routine is to get a relevant tool to try your skills on . What else can be good than wordigram itself? Here's a small overview of this amazing platform for sentences , words , nouns , adjectives , hashtags and paragraph generation . "]
f.writelines(List)
f.close()

f1=open("paragraph.txt","rt")      
lines=f1.read()
f1.close()
Allwords=[]
filewords=lines.split()
for x in filewords:
  if x.isalpha():
    Allwords.append(x)    

glossary=[]
for ch in Allwords:
  ch=ch.title()
  if ch.lower() != "a" and ch.lower() != "the" and ch.lower() != "your" and ch.lower() != "for" and ch.lower() != "is" and ch.lower() != "on" and ch.lower() != "in" and ch.lower() != "and" and ch.lower() != "or" and ch.lower() != "be" and ch.lower() != "of" and ch.lower() != "to" and ch.lower() != "at" and ch.lower() != "you" and ch.lower() != "are" and ch.lower() != "were" and ch.lower() != "that" :
      if ch in glossary:
        continue
      else:
        glossary.append(ch)

glossary.sort()       
print(glossary)
print()
print()
print()
print ('\t\t\t\t',"GLOSSARY")
print()
print()

p=0
while p<len(glossary)-1:
  
  print('\t',"%-15s %-15s %-15s %s" %(glossary[p],glossary[p+1],glossary[p+2],glossary[p+3]))
  print()
  p=p+4