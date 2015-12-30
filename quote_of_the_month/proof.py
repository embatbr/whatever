str2number = lambda letter: ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter.upper()) + 1)
word2sum = lambda word: sum(map(str2number, word))

print('knowledge = %d%%' % word2sum('KNOWLEDGE'))
print('hardwork = %d%%' % word2sum('HARDWORK'))
print('attitude = %d%%' % word2sum('ATTITUDE'))