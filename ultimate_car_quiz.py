def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('Correct Answer')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('Sorry, wrong answer. Try again ')
            attempt = attempt + 1


    if attempt == 3:
        print('The correct answer is ' + answer)


score = 0
print('Ultimate Car Quiz!')
guess1 = input('What is Toyotas best selling hybrid car? ')
check_guess(guess1, 'Prius')
guess2 = input('What is the 3VZ-E V6 Toyota engine commonly known as? ')
check_guess(guess2, '3.slow')
guess3 = input('Who technically invented the first automobile? ')
check_guess(guess3, 'Karl Benz')
guess4 = input('Which American auto maker makes electric cars with models like the R1T and R1S? ')
check_guess(guess4, 'Rivian')
guess5 = input('The Soul, Sorento, and Sportage are all models made by what Korean auto maker? ')
check_guess(guess5, 'Kia')
guess6 = input('Buick, Cadillac, and Chevrolet are all made by who? ')
check_guess(guess6, 'General Motors')
guess7 = input('What Japanese automaker makes the Miata? ')
check_guess(guess7, 'Mazda')
guess8 = input('Which Toyota made luxury car sold in Japan has a V12 engine? ')
check_guess(guess8, 'Century')
guess9 = input('Is Porsche an American, Korean, German, or Japanese company? ')
check_guess(guess9, 'German')
guess10 = input('In 2025, Chevrolet ceased production of all sedans and coupes except for one. What car is still in production? ')
check_guess(guess10, 'Corvette')



print('Your score is ' + str(score))
