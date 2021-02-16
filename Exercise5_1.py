def dice_game(dice_type):
    """

    Args:
        dice_type:

    Returns:

    """
    AVAILABLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    dice_value = ''
    # multiplier = ''
    # modifier = ''
    for dice in AVAILABLE_DICES:
        if dice_type in AVAILABLE_DICES:
            multiplier, modifier = dice_type.split(dice)
        dice_value = int(dice_type[1:])
    else:
        print('Provided value is incorrect!')
    return multiplier, modifier


print(dice_game('D120 + 100'))

# AVAILABLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
#
# for dice in AVAILABLE_DICES:
#     print(dice)
