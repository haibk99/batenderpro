questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
};
ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
};

import random
def printanser(questions,ingredients):
    print(questions['strong'] ,random.choice(ingredients['strong']))
    print(questions['salty'] ,random.choice(ingredients['salty']))
    print(questions['bitter'] ,random.choice(ingredients['bitter']))
    print(questions['sweet'] ,random.choice(ingredients['sweet']))
    print(questions['fruity'] ,random.choice(ingredients['fruity']))
    return;
 #   if questions="strong"
printanser (questions, ingredients)