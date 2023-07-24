from django import template
register=template.Library()




def swap(data):
    return data.swapcase()

register.filter('swap',swap)

@register.filter()
def remove(data,arg):
    return data.replace(arg,' ')

@register.filter()
def change(data):
    s=data.split()
    l=[]
    for i in range(len(s)):
        if i==0 or i==len(s)-1:
            l.append(s[i])
        else:
            l.append(s[i].lower())
    return ' '.join(l)


@register.filter()
def count(s,sub):
    c=0
    for i in range(len(s)):
        if s[i:i+len(sub):]==sub:
            c+=1
    return c