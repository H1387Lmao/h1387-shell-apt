def echo(args):
   print(" ".join(args))


basic_shell_commands["echo"] = lambda args: echo(args)
