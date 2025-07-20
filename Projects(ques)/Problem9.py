# Progaram to fill in a letter template given below with name and date 
"""letter = '''
          Dear <|Name|>,
          You are selected!
          <|Date|>
          '''
"""

Name = input("Your name:")
Date = input("Today's date:")

letter = f'''
        Dear, {Name},
        You are selected!
        {Date}
         '''

print(letter)

#OR

letter = '''Dear <|Name|>,
          You are selected!
          <|Date|>'''

new_letter = letter.replace("<|Name|>", Name).replace("<|Date|>", Date)

print(new_letter)