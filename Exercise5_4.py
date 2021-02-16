import random


def dice_game(dice_type):
    """
    This function simulates a dice game with numerous dice types
    Args:
        dice_type: a specific type of dice

    Returns: Sum of points from dice runs

    """
    # define all available dices
    AVAILABLE_DICES = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')
    # iterate on all dices in the the list of available dices
    for dice in AVAILABLE_DICES:
        # condition to check if the given function input matches available values
        if dice in dice_type:
            # get the values of multiplier and number added / subtracted
            multiplier, modifier = dice_type.split(dice)
            dice_value = int(dice[1:])
        else:
            return 'Provided value is incorrect!'
        break
    else:
        return 'Provided value is incorrect!'
    # exception to check if multiplier is convertible to int and value is assigned if multiplier is not provided
    try:
        multiplier = int(multiplier) if multiplier else 1
    except ValueError:
        return 'Provided value is incorrect!'
    # exception to check if multiplier is convertible to int and value is assigned if multiplier is not provided
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return
    # calculating the sum of number from mulpliple tries
    return sum([random.randint(1, dice_value) for _ in range(multiplier)]) + modifier


if __name__ == '__main__':
    print(dice_game("2D10+10"))
    print(dice_game("D6"))
    print(dice_game("2D3"))
    print(dice_game("D12-1"))
    print(dice_game("DD34"))
    print(dice_game("4-3D6"))

#         if not multiplier:
#             multiplier = 1
#         else:
#             multiplier = int(multiplier)
#     except ValueError:
#         return 'Provided value is incorrect!'
#     try:
#         if not modifier:
#             modifier = 0
#         else:
#             modifier = int(modifier)
#     except ValueError:
#         return 'Provided value is incorrect!'
#     dice_numbers = [random.randint(1, dice_value) for _ in range(multiplier)]
#     return sum(dice_numbers + modifier)
#
#
# print(dice_game('D20'))
