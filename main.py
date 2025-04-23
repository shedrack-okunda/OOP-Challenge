from pet import Pet

def main():
    # Create a new pet object
    pet = Pet("Pretty")
    print(f'Creating a new pet object: {pet.name}')
    
    # Test the eat method
    print("Testing the eat method:")
    pet.eat()
    pet.get_status()

    # Test the sleep method
    print('\nTesting the sleep method:')
    pet.sleep()
    pet.get_status()

    # Test the play method
    print('\nTesting the play method:')
    pet.play()
    pet.get_status()
    
    # Test the train method
    print('\nTesting the train method:')
    pet.train('sit')
    pet.train('stay')
    pet.train('in')
    pet.show_tricks()
    
    # Test the play method when energy is low
    print('\nTesting the play method when energy is low:')
    pet.energy = 1
    pet.play()
    pet.get_status()

    # Test the eat method when hunger is low
    print('\nTesting the eat method when hunger is low:')
    pet.hunger = 1
    pet.eat()
    pet.get_status()
    
if __name__ == "__main__":
    main()