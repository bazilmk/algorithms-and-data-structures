'''
Created By: Bazil Muzaffar Kotriwala
Student ID: 27012336
'''

import Task_3
from Task_3 import ArrayOperations
from Task_4 import file_list

class TextEditor:

    def __init__(self):
        self.array = ArrayOperations()

    def insert_num(self, num, line):
        '''
        This function inserts a line of text in the list at the position inputted by the user, and raises an exception if no position is entered by the user
        :param: number position inputted by the user and the line of text inputted by the user
        :precondition: A list must already exist
        :postcondition: The list is updated as a line is inserted into it or an error is raised depending on the user's input
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        try:
            num = int(num)                                                 # if the string cannot be converted to integer, returns False resulting in '?' to be printed
            self.array.insert(num, line)
        except ValueError:
            return False
        except IndexError:
            return False
        return True


    def read_filename(self, filename):
        '''
        This function takes a filename as an input by the user and reads the contents of the file into a list, storing each line as a single item in the list
        :param: filename of the file to be read
        :precondition: A file must exist from which the contents of the file can be read
        :postcondition: A list is created with each line in the file stored as a single item in the list
        :complexity: Best Case = Worst Case = O(n), where n is the length of the contents in the file, even if the contents are empty or filled the loop will run n times
        '''

        try:
            self.array = file_list(filename)
        except FileNotFoundError:
            return False
        return True

    def write_filename(self, filename):
        '''
        This function creates a new file or opens an existing file and writes every item in the list into the file and then closes the file.
        :param: filename of the file to be written to
        :precondition: There must be an existing list from which it copies the items into the file
        :postcondition: An existing file is overwritten with the contents of the list copied into it or a new file is created with the contents of the list copied into it
        :complexity: Best Case = Worst Case = O(n), where n is the length of the list, the loop will run n times
        '''

        infile = open(filename, 'w')
        for i in range(1, len(self.array) + 1):
            infile.writelines(self.array[i] + str('\n'))
        infile.close()

    def print_num(self, num):
        '''
        This function prints the line from the file at the position inputted by the user, however, if no position is inputted by the user it prints all the lines of the file
        :param: number position inputted by the user
        :precondition: The file must exist already to be accessed
        :postcondition: The particular line or all the lines of the file are printed for the user
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        if num == '':                                                       # if no input for position is given, all the lines are printed
            print(self.array)
        else:
            try:
                num = int(num)                                              # if the string cannot be converted to integer, returns False resulting in '?' to be printed
                print(self.array[num])
            except ValueError:
                return False
            except IndexError:
                return False
        return True

    def delete_num(self, num):
        '''
        This function deletes the line from the file at the position inputted by the user, however, if no position is inputted by the user it deletes all the lines of the file
        :param: number position inputted by the user
        :precondition: The file must have some existing lines to be deleted i.e. the file cannot be empty.
        :postcondition: The file is updated after the deletion has taken place depending on the user input
        :complexity: Best Case = Worst Case = O(1), constant time complexity.
        '''

        try:
            if num == '':
                for i in range(len(self.array), 0, -1):
                    self.array.delete(i)                                    # if no input for position is given, all the lines are deleted from the list
            else:
                num = int(num)                                              # if the string cannot be converted to integer, returns False resulting in '?' to be printed
                self.array.delete(num)
        except IndexError:
            return False
        except ValueError:
            return False
        return True

def help():
    print('\nInstructions:')
    print('$ - command')
    print('> - input line')
    print("'?' - incorrect input")
    print('1. insert/print/delete - Type the one of these commands followed by the line number to apply the command to that line.')
    print('2. print/delete - If you type the command without any line number following it, that command will be applied to all the lines in the list. ')
    print('3. read/write - Type either of the commands followed by the name of the file to which you want to apply the command. ')
    print('4. quit - Type the command to end program.\n')


if __name__ == '__main__':

    array = TextEditor()
    print("Welcome to Bazil's Text editor!\n")

    print('[insert] Insert Num ')
    print('[read] Read filename ')
    print('[write] Write Filename ')
    print('[print] Print Num ')
    print('[delete] Delete Num ')
    print('[quit] Quit Program')
    print('[help] Need help?\n')


    command_prompt = True
    while command_prompt:

        command = input('$ ')

        if command[:6] == 'insert':
            line = input('> ')
            if not array.insert_num(command[7:], line):
                print('?')

        elif command[:4] == 'read':
            if not array.read_filename(command[5:]):
                print('?')

        elif command[:5] == 'write':
            array.write_filename(command[6:])

        elif command[:5] == 'print':
            if not array.print_num(command[6:]):
                print('?')

        elif command[:6] == 'delete':
            if not array.delete_num(command[7:]):
                print('?')

        elif command[:4] == 'help':
            help()

        elif command[:4] == 'quit':
            print('\nThe program has been terminated. ')
            break

        else:
            print('?')
            continue