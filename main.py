def hello(name):
  answer = 'Hello ' + name
  print(answer)
  return answer

def main():
  name = input('What is your name? ')
  hello(name)

if __name__ == '__main__':
  main()
