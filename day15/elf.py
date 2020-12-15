def play(start_numbers):
    playing = True
    last_number_spoken = -1
    turn = 1
    spoken = {}
    number = start_numbers.split(',')
    lenstart = len(number)
    while playing:

        if turn <= lenstart:
            last_number_spoken = number[turn - 1]
            spoken[last_number_spoken] = turn
        else:
            print(spoken)
            if last_number_spoken not in spoken:
                spoken[last_number_spoken] = turn
                last_number_spoken = 0
            else:
                previous_before_last_turn = spoken[last_number_spoken]
                last_number_spoken = turn - 1 - previous_before_last_turn
                spoken[last_number_spoken] = turn
        print(f"Turn: {turn}, number spoken: {last_number_spoken}")
        turn += 1
        if turn > 5:
            return last_number_spoken


result = play("0,3,6")
assert result == 436

result = play("1,3,2")
assert result == 1

result = play("2,1,3")
assert result == 10

result = play("1,2,3")
assert result == 27

result = play("2,3,1")
assert result == 78

result = play("3,2,1")
assert result == 438

result = play("3,1,2")
assert result == 1836
