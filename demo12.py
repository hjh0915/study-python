ingredients = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
for i in range(len(ingredients)):
    print i + 1, ingredients[i]

dir(enumerate(ingredients))
for i, x in enumerate(ingredients):
    print '%s %s' % (i+1, x)
    
