class Hello:
  def __str__(self):
    return 'Hello World!'
  def hello(who):
    return '\nHello ' + who + '!\n'

print( Hello().hello('Matheus') )
