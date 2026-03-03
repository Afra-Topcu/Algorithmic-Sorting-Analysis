import os


# Custom pseudorandom number generator with a random initial seed
class PRNG:
    def __init__(self, seed=None):
        # Use a truly random seed if no seed is provided
        if seed is None:
            seed = int.from_bytes(os.urandom(4), 'big')  # Generate a random 32-bit integer
        self.state = seed

    def randint(self, low, high):
        # Simple linear congruential generator (LCG)
        self.state = (1103515245 * self.state + 12345) % (2 ** 31)
        return low + (self.state % (high - low + 1))


# Generate logistics dataset
def generate_logistics_dataset(num_warehouses=100, max_packages=1000, seed=None):
    """Generates a logistics dataset with a random or specified seed."""
    prng = PRNG(seed)  # Initialize PRNG with the seed or a random one
    data = []
    for i in range(1, num_warehouses + 1):
        warehouse_id = f"WH-{str(i).zfill(3)}"
        priority_level = prng.randint(1, 5)
        package_count = prng.randint(0, max_packages)
        data.append([warehouse_id, priority_level, package_count])
    return data


# Save dataset to a CSV file
def save_to_csv(data, file_name):
    """Saves the dataset to a CSV file."""
    with open(file_name, "w") as file:
        # Write the header
        file.write("Warehouse_ID,Priority_Level,Package_Count\n")
        # Write each row
        for row in data:
            file.write(",".join(map(str, row)) + "\n")


######### YOUR CODE GOES HERE ---  You shoud define here two_level_sorting and the 3 sorting functions

### Your three sorting functions should have global variable named as counter. So do not return it.
def bubble_sort(array):
    global counter
    counter = 0
    #comparison
    for i in range(len(array)):
        swapped = False
        for j in range(len(array)-i-1):
            counter += 1
            if array[j][1] > array[j + 1][1]:  # if Priority_Level is bigger switch place
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
            # if Priority_Level is equal and Package_Count is bigger switch place
            elif array[j][1] == array[j + 1][1] and array[j][2] > array[j + 1][2]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break #if nothing swap then its over
    return array

def merge_sort(array):
    global counter
    counter=0
    def recursive(array):
        global counter
        if len(array) > 1:  # make this until all arrays has one item
            middle = len(array) // 2  # slice the array into two new array
            left = array[:middle]
            right = array[middle:]
            recursive(left)
            recursive(right)
            i=0 #index of left array
            j=0 #index of right array
            k=0 #index of sorted array
            while i < len(left) and j < len(right):
                counter += 1
                #find the which ones Priority_Level is smaller add that to the array
                if left[i][1] < right[j][1]:
                    array[k]=left[i]
                    i+=1
                elif left[i][1] > right[j][1]:
                    array[k]=right[j]
                    j+=1
                #if Priority_Level are same look for the Package_Count and add the smaller one to the array
                else:
                    if left[i][2] <= right[j][2]:
                        array[k]=left[i]
                        i+=1
                    elif left[i][2] >= right[j][2]:
                        array[k]=right[j]
                        j+=1
                k+=1 #the index of sorted array is incremented one to not to add on top of other array
            #if there is anything left in arrays
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
    recursive(array)
    return array

def quick_sort(array):
    global counter
    counter=0
    #making everything sorted
    def recursive (array):
        if len(array) <1:
            return array
        global counter
        counter += 1
        global quick_sort_pc_counter
        pivot=array[len(array) // 2] #get the middle one as a pivot
        bigger,smaller,equal=[],[],[]
        for number in array:
            #if Priority_Level is smaller than pivots Priority_Level append that to smaller list
            if number[1] < pivot[1]:
                smaller.append(number)
            #if Priority_Level is bigger than pivots Priority_Level append that to bigger list
            elif number[1] > pivot[1]:
                bigger.append(number)
            #if Priority_Level is equal than look their Package_Count
            else:
                #if Package_Count is smaller append to smaller list
                if number[2] < pivot[2]:
                    smaller.append(number)
                #if Package_Count is bigger append to bigger list
                elif number[2] > pivot[2]:
                    bigger.append(number)
                else:
                    equal.append(number)
        return recursive(smaller) + equal + recursive(bigger)

    return recursive(array)

def two_level_sorting(func_sort, array):
    global counter
    counter = 0 #for new sorting make it zero
    array=func_sort(array) #sort for priority levels
    pl_iterations=counter #number of sorting steps based on priority level
    pc_iterations=0
    final_array=[]
    priority_levels=[] #list for priority levels
    for row in array:
        if row[1] not in priority_levels:
            priority_levels.append(row[1])
    #sorting same priority levels base on package count
    for level in priority_levels:
        #extract the group of rows with the same priority level
        group=[row for row in array if row[1] == level]
        counter=0
        #sort the group by their package count
        group=func_sort(group)
        pc_iterations+=counter
        final_array.extend(group)

    return final_array, pl_iterations, pc_iterations


#########

def write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
):
    """Write sorted results and comparisons to the output file."""
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as file:
        file.write("=== Bubble Sorted Results ===\n")
        # file.write(bubble_sorted.to_string() + "\n\n")
        file.write("Warehouse_ID  Priority_Level  Package_Count\n")
        file.write("-" * 40 + "\n")
        for row in bubble_sorted:
            file.write(f"{row[0]:<12}  {row[1]:<14}  {row[2]:<13}\n")
        file.write("\n")
        file.write("=== Comparison Results ===\n")
        if merge_check:
            file.write("Merge and Bubble sorts are identical.\n")
        else:
            file.write("Merge and Bubble sorts differ.\n")

        if quick_check:
            file.write("Quick and Bubble sorts are identical.\n")
        else:
            file.write("Quick and Bubble sorts differ.\n")

        file.write("\n=== Sort Performance Metrics ===\n")
        file.write(f"Bubble priority sort iteration count: {bubble_sort_pl_iterations}\n")
        file.write(f"Merge priority sort n_of right array is smaller than left: {merge_sort_pl_counter}\n")
        file.write(f"Quick priority sort recursive step count: {quick_sort_pl_counter}\n\n")

        file.write(f"Bubble package count sort iteration count: {bubble_sort_pc_iterations}\n")
        file.write(f"Merge package count n_of right array is smaller than left: {merge_sort_pc_counter}\n")
        file.write(f"Quick package count sort recursive step count: {quick_sort_pc_counter}\n")

    print(f"Results written to {OUTPUT_FILE}")


if __name__ == "__main__":
    # File paths and dataset size
    # Specify paths for input and output files
    INPUT_FILE = "/Users/afratopcu/Desktop/b2230356124/hw05_input.csv"  # Path where the generated dataset will be saved
    OUTPUT_FILE = "/Users/afratopcu/Desktop/b2230356124/hw05_output.txt"  # Path where the sorted results and metrics will be saved
    SIZE = 100  # Number of warehouses in the dataset

    # Generate the dataset
    dataset = generate_logistics_dataset(SIZE,
                                         max_packages=100)  # Generate a dataset with SIZE warehouses and max_packages packages

    # Save the generated dataset to the input file
    save_to_csv(dataset, INPUT_FILE)

    ###############################################################################################################
    # Perform sorting and counting operations
    # Sort using Bubble Sort and count iterations for Priority Level (_pl_) and Package Count (_pc_)
    bubble_sorted, bubble_sort_pl_iterations, bubble_sort_pc_iterations = two_level_sorting(bubble_sort, dataset)

    # Sort using Merge Sort and count recursive steps for Priority Level and Package Count
    merge_sorted, merge_sort_pl_counter, merge_sort_pc_counter = two_level_sorting(merge_sort, dataset)

    # Sort using Quick Sort and count recursive steps for Priority Level and Package Count
    quick_sorted, quick_sort_pl_counter, quick_sort_pc_counter = two_level_sorting(quick_sort, dataset)
    ###############################################################################################################

    # Comparisons
    # Check if Merge Sort results match Bubble Sort results
    merge_check = merge_sorted == bubble_sorted

    # Check if Quick Sort results match Bubble Sort results
    quick_check = quick_sorted == bubble_sorted

    # Write results and metrics to the output file
    write_output_file(
        bubble_sorted, merge_sorted, quick_sorted,
        bubble_sort_pl_iterations, merge_sort_pl_counter, quick_sort_pl_counter,
        bubble_sort_pc_iterations, merge_sort_pc_counter, quick_sort_pc_counter,
        merge_check, quick_check
    )




