import re
import urllib.request

class navic:
    def python():
        page=urllib.request.urlopen('https://www.python.org/doc/versions/')
        l=page.read()
        c=l.decode('ASCII')
        file=open("x.txt","w")
        file.write(c)
        file.close()
        s=open("x.txt","r")
        for line in s:
            
            if('<li><a class="reference external" href="http://docs.python.org/release' in line):
               s=open("x.txt","w")
               s.write(line)
               result=re.search('Python (.*)</a>',line)
               b = result.group(1)
               return(b)
               
    def ruby():
        page=urllib.request.urlopen('https://www.ruby-lang.org/en/downloads/')
        c=page.read()
        #\c=urllib.parse.unquote(page)
        
        
        file=open("x.txt","w")
        file.write(str(c))
        file.close()
        q=str(c)
        s=open("x.txt","r")
        
        result=re.search('The current stable version is (.*)Please be sure',q)
        b = result.group(1)
        return(b[:-3])
        
    def android_studio():
        page=urllib.request.urlopen('https://developer.android.com/studio/releases/')
        c=page.read()
        #\c=urllib.parse.unquote(page)
        
        
    file=open("x.txt","w")
    file.write(str(c))
    file.close()
    q=str(c)
    file.close()
    s=open("x.txt","r")
    for line in s:
        
        
           s=open("x.txt","w")
           #s.write(line)
           result=re.search('<p><b>(.*)</b></p>',line)
           b = result.group(1)
           a=b.split()
           return(a[0])
           

               


            


