def echo(args):
   new=[]
   for i,v in enumerate(args):
      if i == 0:
         continue
      new.append(v)
   print(" ".join(new))


basic_shell_commands["echo"] = echo
