def dice_game(dice_type):
    """

    Args:
        dice_type:

    Returns:

    """
    multiplier = ''
    modifier = ''
    # define all available dices
    AVAILABLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
    # iterate on all dices in the the list of available dices
    for dice in AVAILABLE_DICES:
        # condition to check if the given function input matches available values
        if dice_type in AVAILABLE_DICES:
            # get the values of multiplier and number added / subtracted
            multiplier, modifier = dice_type.split(dice)
    else:
        print('Provided value is incorrect!')
    dice_value = int(dice_type[1:])
    multiplier =int(multiplier)
    if not multiplier:
        mulitplier = 1
    modifier = int(modifier):
        return modifier
    else:
        modifier = 0






print(dice_game('D120 + 100'))

# AVAILABLE_DICES = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
#
# for dice in AVAILABLE_DICES:
#     print(dice)

dice = '3D30 + 10'
for i in dice:
    print(i)