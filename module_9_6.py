def all_variants(text):
    i=0
    j=1
    while j!=len(text)+1:
        yield text[i:i+j]
        i+=1
        if i==len(text) or i+j>len(text):
            i=0
            j+=1


a = all_variants("abc")
for i in a:
    print(i)
