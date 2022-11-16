'''
This program is designed to calculate the 
needed scale factor to inlay a negative and 
positive piece of acrylic.
'''

def calc_scale_factor(theo_length: float, calc_length: float) -> float:
    # The error length divided by 2
    error_length_d2 = (theo_length - calc_length) / 2
    
    # The scaled length needed for Theoretical to equal Measured
    scaled_length = theo_length + (2*error_length_d2)
    
    # Return scale factor
    return (scaled_length/theo_length)
    
def main() -> None:
    # Get inputs
    print('Theoretical length of one side: ')
    theo_length = float(input())
    print('Measrued length of one side after cut: ')
    calc_length = float(input())
    
    # Calculate the scale factor
    scale_factor = calc_scale_factor(theo_length, calc_length)
    print(f'\nThe scale_factor needed is: {scale_factor}')
    
    # Print new length for CAD
    print(f'New theoretical length = {scale_factor*theo_length}')
    
if __name__ == '__main__':
    main()