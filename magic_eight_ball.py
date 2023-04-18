import random

name = 'Ira'
question = 'Will it rain?'
answer = ''
random_number = random.randint(1,11)
# print(random_number)

if random_number == 1:
  answer = 'Yes - definitely.'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
elif random_number == 10:
  answer = 'Maybe. Maybe not.'
elif random_number == 11:
  answer = 'All will be revealed in time.'
else:
  answer = 'Error'

if question == '':
  print('Please ask a question.')
elif name == '':
  print('Question: {}'.format(question))
  print('Magic 8-Ball\'s answer: {}'.format(answer))
else:
  print('{} asks: {}'.format(name, question))
  print('Magic 8-Ball\'s answer: {}'.format(answer))

# or it could be: print(name + ' asks: ' + question) and print('Magic 8'Ball\'s answer: ' + answer)