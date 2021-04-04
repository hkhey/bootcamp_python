phrase = "The right format"
pads=""
n=42-len(phrase)
for i in range(n):
    pads+="-"
phrase=pads+phrase
print(phrase,"\n",len(phrase))
