def mad_lib():
    """
    Start the mad lib game
    """
    print("""
The Mad Lib Game

Enter an adjective:
          
""")

    adjective = input()

    print("""
Enter a color:
          
""")

    color = input()

    print("""
Enter a noun:
          
""")
    noun = input()

    print("""
Enter a verb:
          
""")
    verb = input()
    print("""
Enter an adverb:
          
""")
    adverb = input()
    print(f"""
    story:
        Once upon a time, 
        in a land filled with vibrant colors, 
        there was a very special and unique individual. 
          This individual was a/an {adjective} {noun}.
         This {adjective} {noun} loved to wear bright and bold {color} clothes. 
         
         
         One day, while {verb}ing in the park, 
         they {verb}ed a {noun} that caught their eye. 
         The {adjective} {noun} quickly ran over to get a closer look. As they reached for the {noun}, they discovered that it was a {adjective} gemstone. 
         The {adjective} {noun} was overjoyed and quickly added the gemstone to their collection. 

         As they {adverb} walked home, 
         they couldn't stop thinking about their new acquisition. 
         The {adjective} {noun} couldn't wait to show off their new treasure to their friends and family.
        #  
""")

mad_lib()