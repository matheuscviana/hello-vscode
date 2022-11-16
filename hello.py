class Hello:
  def __str__(self):
    return 'Hello World!'
  def hello(who=''):
    return '\nHello %s!\n' % who

print( Hello().hello('Matheus') )
