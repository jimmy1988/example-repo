#Maximum stars we are going to
max_stars = 5

#starting number to start the increment or decrement
stars = 1

#The stepping value for the range
direction = 1

#loop around displaying the stars
# _ is a throwaway value, we will be controlling the stars variable manually
for _ in range(2 * max_stars - 1):

    # print the amoy=unt of stars times the number of stars
    print("*" * stars)

    #When reach the max stars, change the direction
    if stars == max_stars:
        direction = - 1

    #Increment or decrement the stars by 1, depending on the direction
    stars += direction