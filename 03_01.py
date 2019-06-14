subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']
result =[]
for sub in subs:
    for verb in verbs:
        for obj in objs:
          result.append((sub,verb, obj))
print(result)