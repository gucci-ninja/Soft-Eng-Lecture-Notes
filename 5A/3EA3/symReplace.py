import re

class mathDict(dict):
    def __missing__(self, key):
        print (key)
        return key[1:]

mathSyms = mathDict({
    "/F" : "⊥" ,
    "/T" : "⊤" ,
    "/not" : "¬" ,
    "/and" : "∧" ,
    "/or" : "∨" ,
    "/implies" : "⇒" ,
    "/implied" : "⇐" ,
    "/unequal" : "⧧" ,
    "/times" : "×" ,
    "/inter" : "‘" ,
    "/cent" : "¢",
    "/sPower" : "ϟ",
    "/inf" : "∞",
    "" : "∈" ,
    "" : "∪" ,
    "" : "∩" ,
    "" : "⊇" ,
    "" : "⊆" ,
    "/sLen" : "↔" ,
    "/sModL" : "⊲" ,
    "/sModR" : "⊳" ,
    "/fs" : "〈" ,
    "/fe" : "〉" ,
    "/map" : "→" ,
    "/fDom" : "☐" ,
    "" : "∀" ,
    "" : "∃" ,
    "" : "Σ" ,
    "" : "∏" ,
    "" : "σ" ,
    "" : "ʹ" ,
    "" : "⦂" ,
    "/tab": "&nbsp;&nbsp;&nbsp;&nbsp;"
})

change = lambda o,n,span: o[:span[0]] + n + o[span[1]:]
regKeys = re.compile("(?<![a-zA-Z\<])\/[a-zA-Z]+(?!\>)") # find keys in mathSyms
regScript = re.compile("\/([\_^])<(.*?)\/>") # find subscript/superscript
symC = 1

with open("README.md", encoding='utf8', mode="r") as f:
    lines = f.read()
    while symC:
        # find and replace math symbol shortcut
        csK = [(x.span(),mathSyms[x.group(0)]) for x in regKeys.finditer(lines)][::-1]
        for c in csK:
            lines = change(lines,c[1],c[0])
        symC=len(csK)

        # find and replace superscript/subscript shortcut
        csS = [(x.span(),x.group(1),x.group(2)) for x in regScript.finditer(lines)][::-1]
        for c in csS:
            scriptType = "b" if c[1] == "_" else "p"
            replaceText = "<su{}>{}</su{}>".format(scriptType,c[2],scriptType)
            lines = change(lines,replaceText,c[0])
    

with open("README.md", encoding='utf8', mode='w') as f:
    f.write(lines)