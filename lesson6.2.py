number = int(input('Enter a number from 0 to 8640000: '))

if 0 <= number <= 8640000:
    days, rest = divmod(number, (60 * 60 * 24))
    hours, second_rest= divmod(rest, (60 * 60))
    minutes, seconds = divmod(second_rest, 60)

    if 11 <= days % 100 <= 19:
        word_form = 'день'
    elif 2 <= days % 10 <= 4:
        word_form = 'дня'
    elif days % 10 ==1:
        word_form = 'день'
    else:
        word_form = 'днів'

    print(str(days) + ' ' + str(word_form), end= ' ')
    print (str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2), sep= ':')

else:
    print('Error')
