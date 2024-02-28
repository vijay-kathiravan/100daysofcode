def area_to_paint_wall(height:int,width:int)->int:
    """
    This function calculates the number of cans we have to buy to paint a certain size of wall
    :param height: This parameter takes the value of height as input
    :param width: This parameter takes the value of width as input
    :return: This function returns a integer value as output which is nothing but the number of cans required
    """
    coverage_per_can = 5
    area = (height * width)/ coverage_per_can
    area = area.__ceil__()
    return area
cans = area_to_paint_wall(3,9)
print(f"You will need {cans} cans")