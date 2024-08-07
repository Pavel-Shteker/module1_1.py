example = 'Любишь Слаанеш - люби и BURN IN PURGING FLAME'

ostatok=len(example)%2
polovina=len(example)//2
correct=ostatok+polovina-1 #ручная коррекция из за нулевого символа

print ('1) ', example[0])
print ('2) ', example[-1])
print ('3) ', example[correct::])
print ('4) ', example[::-1])
print ('5) ', example[0::2])
