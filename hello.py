class Hello:
  def __str__(self):
    return 'Hello World!'
  def hello(fulano):
    return '\nHello ' + fulano + '!\n'

print( Hello().hello('Matheus') )
