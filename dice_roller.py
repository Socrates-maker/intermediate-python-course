def main():

    import random
    dice_roll=2
    dice_sum=0
    for i in range(0,dice_roll):
        roll=random.randint(1,6)    
        dice_sum+=roll
        if roll==1:
            print(f'you rolled a {roll} !critical fail')
        elif roll==6:
            print(f'you rolled a {roll} !critical succes')
        else:
            print(f'you rolled {roll}')
    
    print(f'you have rolled a total of {dice_sum}')


if __name__== "__main__":
                   main()
