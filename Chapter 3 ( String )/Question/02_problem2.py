letter = '''Dear <|Name|>,
            You are selected! 
            <|Date|>'''

# .replace is string function so it used for replacing world

print(letter.replace("<|Name|>","Suraj").replace("<|Date|>","20 oct 2026"))