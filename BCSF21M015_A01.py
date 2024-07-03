# Time complexity: O(n^2)
# Space complexity: O(n^2)

# Step 01
    # Create preferences matrix for hospitals and residents.

    # Args:
    # - no_hospital (int): Number of hospitals.
    # - no_residents (int): Number of residents.

    # Returns:
    # - List of lists: Hospital preferences matrix.
    # - List of lists: Resident preferences matrix.
        
def create_Matrix_hospital(no_hospital, no_residents):
    hospital_prefered_list = []
    print("\nFill Hospitals preferred list:")
    for i in range(no_hospital):
        row = []
        print(f"Enter H{i + 1} preferred list:")
        for j in range(no_residents):
            value = int(input(f"Preference for Resident R{j + 1}: "))
            row.append(value)
        hospital_prefered_list.append(row)

    return hospital_prefered_list

def create_Matrix_residents(no_hospital, no_residents):
    residents_prefered_list = []
    print("\nFill Residents preferred list:")
    for i in range(no_residents):
        row = []
        print(f"Enter R{i + 1} preferred list:")
        for j in range(no_hospital):
            value = int(input(f"Preference for Hospital H{j + 1}: "))
            row.append(value)
        residents_prefered_list.append(row)

    return residents_prefered_list

# Step 02
    # Perform stable matching algorithm.

    # Args:
    # - n (int): Number of hospitals/residents.
    # - hospital_preferences (list of lists): Hospital preferences matrix.
    # - resident_preferences (list of lists): Resident preferences matrix.

    # Returns:
    # - List: Pairs representing the stable matching.
def stable_matching(n, hospital_preferences, resident_preferences):
    engaged_to = [-1] * n
    free_hospital = [True] * n
    no_engaged = 0
    while no_engaged < n:
        for hospital in range(n):
            if free_hospital[hospital]:
                resident = hospital_preferences[hospital][0]
                if engaged_to[resident] == -1:
                    engaged_to[resident] = hospital
                    no_engaged += 1
                    free_hospital[hospital] = False
                else:
                    current_hospital = engaged_to[resident]
                    # Compare numeric preferences directly
                    if resident_preferences[resident].index(hospital) < resident_preferences[resident].index(
                            current_hospital):
                        engaged_to[resident] = hospital
                        free_hospital[hospital] = False
                        free_hospital[current_hospital] = True
        for i in range(n):
            if free_hospital[i]:
                hospital_preferences[i].pop(0)
    return engaged_to


def main():
    no_hospital_residents = int(input("Enter number of hospitals/residents: "))
    print("---- Preferences should be in numeric form!! (0-..) ")
    print("---- Preferences should be start with 0 ----")
    hospital_preferences = create_Matrix_hospital(no_hospital_residents, no_hospital_residents)
    resident_preferences = create_Matrix_residents(no_hospital_residents, no_hospital_residents)

    print("\n\t\t<<---Hospital preferred list--->>")
    for i, row in enumerate(hospital_preferences, start=1):
        print(f" H{i} -> {row}")

    print("\t\t<<---Residents preferred list--->>")
    for i, row in enumerate(resident_preferences, start=1):
        print(f" R{i} -> {row}")

    pairs = stable_matching(no_hospital_residents, hospital_preferences, resident_preferences)

    print("\nOne possible Stable Matching:-\n ")
    for i, j in enumerate(pairs):
        print(f"Hospital H{i + 1} and Resident R{j + 1}")

    print("\n\t-----The End-----\n")    

if __name__ == "__main__":
    main()
