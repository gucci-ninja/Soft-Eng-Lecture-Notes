import re

mathSyms = {
    "/F" : "⊥" ,
    "/T" : "⊤" ,
    "/not" : "¬" ,
    "/and" : "∧" ,
    "/or" : "∨" ,
    "/implies" : "⇒" ,
    "/implied" : "⇐" ,
    "/unequal" : "⧧" ,
    "" : "×" ,
    "" : "‘" ,
    "" : "∈" ,
    "" : "∪" ,
    "" : "∩" ,
    "" : "⊇" ,
    "" : "⊆" ,
    "" : "↔" ,
    "" : "⊲" ,
    "" : "⊳" ,
    "" : "〈" ,
    "" : "〉" ,
    "" : "→" ,
    "" : "☐" ,
    "" : "∀" ,
    "" : "∃" ,
    "" : "Σ" ,
    "" : "∏" ,
    "" : "σ" ,
    "" : "ʹ" ,
    "" : "⦂" 
}

change = lambda o,n,span: o[:span[0]] + n + o[span[1]:]
regKeys = re.compile("\/[a-zA-Z]+")

with open("README.md", encoding='utf8', mode="r") as f:
    lines = f.read()

    cs = [(x.span(),mathSyms[x.group(0)]) for x in regKeys.finditer(lines) if x.group(0) in mathSyms][::-1]
    for c in cs:
        lines = change(lines,c[1],c[0])

with open("README.md", encoding='utf8', mode='w') as f:
    f.write(lines)