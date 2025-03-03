# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) #padma_pednekar changed int. to int( ; changed the single quote (') to double quote(") ; changed the "==" to "="

if year < 1900: #padma_pednekar added colon (:) at the end of the if statement, <= changed to <
    print ('Woah, that\'s the past!')  #padma_pednekar changed "that's" to "that\'s", i.e. used escape sequence.
elif year >= 1900 and year <= 2020: #padma_pednekar changed && to and; > changed to >= ; changed < to <=
    print ("That's totally the present!")
else: #padma_pednekar changed the elif to else
    print ("Far out, that's the future!!")
