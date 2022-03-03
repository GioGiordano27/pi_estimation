import random
import matplotlib.pyplot as plt
#Take a function that generates a random number between 0 and 1 with uniform distribution
# Calculate Pi

def estimate_pi(n):

    num_point_circle=0
    num_point_total=0

    x_coords=[]
    y_coords=[]

    for i in range (n):
        x=random.uniform(0,1)
        x_coords.append(x)

        y=random.uniform(0,1)
        y_coords.append(y)

        distance=x**2+y**2

        if distance <=1 :
            num_point_circle+=1
        num_point_total +=1

    plt.figure(figsize=(10, 10), dpi=100)
    plt.axis([0, 1, 0, 1])
    plt.scatter(x_coords, y_coords, s=10)
    plt.savefig("random uniform distribution into pi")
    plt.show()
    return 4 * num_point_circle/num_point_total

def main():
    print(estimate_pi(10000))

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
