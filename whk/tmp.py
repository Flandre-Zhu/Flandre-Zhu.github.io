import os
sys=os.system
from sys import argv

name="linear_algebra_note"
if(len(argv) >=2):
    name=argv[1]

sys(f"pandoc -s {name}.md -o {name}.html --katex --css pink.css")
sys(f"cat katex.html {name}.html > FUCKTMP && mv FUCKTMP {name}.html")
sys(f"cat l2d.html >> {name}.html")
