def dice_game(dice_type):
    """

    Args:
        dice_type:

    Returns:

    """
    available_dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    for dice in dice_type:
        if dice in available_dices:
            multiplier, modifier = dice_type.split(dice)
        else:
            print('Provided value is incorrect!')