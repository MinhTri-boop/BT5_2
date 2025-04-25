#Tạo 1 danh sách (list) ngẫu nhiên N phần tử (N nhập từ bàn phím) có giá trị từ 1 đến 100 sau đó tạo 1 menu cho phép thực hiện các công việc sau:
#In ra danh sách vừa tạo.
#In đảo ngược danh sách.
#Sắp xếp danh sách và in ra danh sách vừa sắp xếp (dùng sorted).
#tim phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
#đếm số lượng các phần tử bằng giá trị X nhập từ bàn phím. In ra các vị trí xuất hiện.
#In ra vị trí các phần tử là số nguyên tố.
#tìm các số duy nhất (không trùng lặp) trong danh sách.
#liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.
#In ra các đoạn con trong danh sách giảm liên tiếp.

def Print_Da_List(da_list):
    print(da_list)
def Print_Da_List_reverse(da_list):
    print(da_list[::-1])
def Sort_Da_List(da_list):
    da_list.sort()
    print(da_list)
def Largest_Da_List(da_list):
    index_out = 0
    max = 0
    for index in reversed(range(0,len(da_list))):
        if max <= da_list[index]:
            max = da_list[index]
            index_out = index
    print(max,index_out)
    return max
def Count_X_And_Its_Index(x, list_input):
    list_of_index = []
    number_of_appearance = 0
    for index in range(0, len(list_input)):
        if list_input[index] == x:
            number_of_appearance += 1
            list_of_index.append(index)
    print(number_of_appearance)
    print(list_of_index)
def Check_If_Prime(list_input):
    max_number_da_list = Largest_Da_List(list_input)
    list_of_basic_prime = []
    list_of_index_test = [1] * (max_number_da_list + 1)
    for number in range(2, (max_number_da_list + 1) // 2):
        index = number+number
        if list_of_index_test[number] == 1:
            list_of_basic_prime.append(number)
            while index <= max_number_da_list:
                list_of_index_test[index] = 0
                index = index + number
    list_to_store_index = []
    print(len(list_of_index_test))
    for number_index in range(2, len(list_of_index_test)):
        if list_of_index_test[number_index] == 1:
            for index in range(0, len(list_input)):
                if number_index == list_input[index]:
                    list_to_store_index.append(index)
    print(list_to_store_index)
    print(list_input)
def Return_Da_Num_If_Appeared_Only_Once(list_input):
    list_output = []
    for number in list_input:
        if list_input.count(number) == 1:
            list_output.append(number)
    print(list_output)
def Return_Number_Inlist_And_Their_Count(list_input):
    dict_output = {}
    for number in list_input:
        if number not in dict_output:
            dict_output[number] = list_input.count(number)
    print(dict_output)
def print_subset_if_it_decreased(list_input):
    list_output_not_clear = []
    list_input.append(1000000000)
    check_the_left = 0
    for index in range(0, len(list_input)-1):
        if list_input[index] >= list_input[index+1]:
            list_output_not_clear.append(list_input[index])
            check_the_left = 1
        elif list_input[index] < list_input[index+1]:
            if check_the_left == 1:
                list_output_not_clear.append(list_input[index])
                check_the_left = 0
            list_output_not_clear.append('end of subset')
    print(list_output_not_clear)
import random as rd
if __name__ == '__main__':

    n = int(input(" Enter the Length of List : "))
    random_list = [rd.randint(1, 100) for _ in range(n)]
    while True:
        print("Pick the number from 1 to 10 to choose a function: ")
        print("1. Print Da List")
        print("2. Print Da List But Reverse")
        print("3. Sort Da List And Print Da List")
        print("4. Da Biggest In Da List And Its Index")
        print("5. Find X And Its Index")
        print("6. Print Da Prime's Index")
        print("7. Print Da Once Appearance Number")
        print("8. Print Number Inlist And Its Appearance")
        print("9. Print Decreased Subset")
        print("10. Exit")
        input_number = int(input())
        if input_number == 1:
            Print_Da_List(random_list)
        elif input_number == 2:
            Print_Da_List_reverse(random_list)
        elif input_number == 3:
            Sort_Da_List(random_list)
        elif input_number == 4:
            Largest_Da_List(random_list)
        elif input_number == 5:
            x = int(input("Enter the number to check: "))
            Count_X_And_Its_Index(x,random_list)
        elif input_number == 6:
            Check_If_Prime(random_list)
        elif input_number == 7:
            Return_Da_Num_If_Appeared_Only_Once(random_list)
        elif input_number == 8:
            Return_Number_Inlist_And_Their_Count(random_list)
        elif input_number == 9:
            print_subset_if_it_decreased(random_list)
        elif input_number == 10:
            break
