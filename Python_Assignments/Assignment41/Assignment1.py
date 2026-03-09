import math

def MarvellousKNN():

    border = "-"*50

#----------------------------------------------------------
# Step 1 : Load Dataset
#----------------------------------------------------------

    print(border)
    print("Step 1 : Load dataset")
    print(border)

    dataset = [
        ("A",1,2,"Red"),
        ("B",2,3,"Red"),
        ("C",3,1,"Blue"),
        ("D",6,5,"Blue")
    ]

    for data in dataset:
        print(data)

#----------------------------------------------------------
# Step 2 : Accept Input Point
#----------------------------------------------------------

    print(border)
    print("Step 2 : Accept new point coordinates")
    print(border)

    x = int(input("Enter X coordinate : "))
    y = int(input("Enter Y coordinate : "))

#----------------------------------------------------------
# Step 3 : Calculate Euclidean Distance
#----------------------------------------------------------

    print(border)
    print("Step 3 : Calculate Euclidean Distance")
    print(border)

    distances = []

    for point,px,py,label in dataset:

        distance = math.sqrt((px-x)**2 + (py-y)**2)

        distances.append((point,px,py,label,distance))

        print(f"{point} Distance : {round(distance,2)}")

#----------------------------------------------------------
# Step 4 : Sort Distances
#----------------------------------------------------------

    print(border)
    print("Step 4 : Sort distances")
    print(border)

    distances.sort(key=lambda d: d[4])

#----------------------------------------------------------
# Step 5 : Select K nearest neighbors
#----------------------------------------------------------

    k = 3

    print(border)
    print(f"Step 5 : Select {k} nearest neighbors")
    print(border)

    neighbors = distances[:k]

    red = 0
    blue = 0

    for point,px,py,label,dist in neighbors:

        print(f"{point} - Distance : {round(dist,2)} Label : {label}")

        if label == "Red":
            red += 1
        else:
            blue += 1

#----------------------------------------------------------
# Step 6 : Majority Voting
#----------------------------------------------------------

    print(border)
    print("Step 6 : Majority Voting")
    print(border)

    if red > blue:
        result = "Red"
    else:
        result = "Blue"

    print("Predicted Class :",result)

#----------------------------------------------------------
# Step 7 : Show Prediction for K = 1,3,5
#----------------------------------------------------------

    print(border)
    print("Step 7 : Prediction for different K values")
    print(border)

    for k in [1,3,5]:

        neighbors = distances[:k]

        red = 0
        blue = 0

        for point,px,py,label,dist in neighbors:

            if label == "Red":
                red += 1
            else:
                blue += 1

        if red > blue:
            result = "Red"
        else:
            result = "Blue"

        print(f"K = {k} -> {result}")

#----------------------------------------------------------
# main
#----------------------------------------------------------

def main():

    MarvellousKNN()

if __name__ == "__main__":
    main()