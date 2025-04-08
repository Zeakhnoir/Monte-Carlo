import random

def monte_carlo_simulation(sample):
    c = 0  # Initialize counter to 0
    
    for _ in range(sample):
        # Generate two uniform random numbers between 0 and 1
        x1 = random.random()
        x2 = random.random()
        
        if x1 < x2:
            # Define segments for the branch where x1 < x2
            s1 = x1              # First segment length
            s2 = x2 - x1         # Second segment length
            s3 = 1 - x2          # Third segment length
            # Sort segments in ascending order, then assign:
            # smallest (a₃), middle (a₂), and largest (a₁)
            segments = sorted([s1, s2, s3])
            a3, a2, a1 = segments[0], segments[1], segments[2]
            
            # If the sum of the two smallest is greater or equal to the largest, increment counter
            if a2 + a3 >= a1:
                c += 1
        else:
            # Define segments for the branch where x1 > x2
            s1 = x2              # First segment length
            s2 = x1 - x2         # Second segment length
            s3 = 1 - x1          # Third segment length
            # Sort segments in ascending order, then assign:
            segments = sorted([s1, s2, s3])
            a3, a2, a1 = segments[0], segments[1], segments[2]
            
            # If the sum of the two smallest is greater than the largest, increment counter
            if a2 + a3 > a1:
                c += 1
    
    # Return the ratio of successful trials to total trials
    return c / sample

if __name__ == "__main__":
    sample = 1000000   # Number of trials
    probability = monte_carlo_simulation(sample)
    print("Probability:", probability)
