def number_scrabble_game():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player1_numbers = []
    player2_numbers = []
    i=1
    while i <= 9:
        print("Nums to pick:", nums)

        # Player1's turn
        player1_num = int(input("Welcome, player1! please, Pick a number from the showed list: "))
        while player1_num not in nums:
            player1_num = int(input("Please, Pick another number: "))
        nums.remove(player1_num)
        player1_numbers.append(player1_num)
        i=i+1
        if i<= 9:
        # Player 2's turn
                print("Nums left:", nums)
                player2_num = int(input("Welcome, player2! please, Pick a number from the showed list: "))
                while player2_num not in nums:
                     player2_num = int(input("Please, Pick another number: "))
                nums.remove(player2_num)
                player2_numbers.append(player2_num)
                i=i+1
        # Checking winning cases
        if check_win(player1_numbers):
            print("Congrats! Player1 is the winner!")
            end = input ("enter e to exit")
            return
        elif check_win(player2_numbers):
            print("Congrats! Player2 is the winner!")
            end = input ("enter e to exit")
            return
    print("it's a draw")
    end = input("enter e to exit")






def check_win(nums):
    if len(nums) < 3:
        return False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 15:
                    return True
    return False


number_scrabble_game()