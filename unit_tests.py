'''
Unit tests for Akira's functions.
'''
import time
from commands import *
import traceback
from termcolor import colored # Color terminal text (makes tests look cool and easier to read)

############### WINDOWS TESTS ###############


class TestCase():
    ''' 
    Generic Test case class. This class can be expanded
    to facilitate more complex test cases.
    '''

    def __init__(self, parameters: list, func, test_name: str, desc: str, expected_output = None):
        '''
        PARAMS:    
            parameters:list: list of function parameters in order
            function:function: function to test
            message:string: Description of the test case 
        RETURNS: None
        Desc: TestCase class initializer.
        '''
        self.parameters = parameters
        self.function = func
        self.test_name = test_name
        self.desc = desc
        self.expected = expected_output # Expected output. None if self.function has no return

    def run(self):
        '''
        PARAMS: None
        RETURNS: result:bool: returns 1 if test is successful; 0 otherwise.
        Desc: Run test case
        '''
        print(f'Executing test: {self.test_name}\nDescription: {self.desc}')
        try:
            result = self.function(*self.parameters) # cool 'splat' operator. 

            # Compare and to expected result and output test results.
            if result == self.expected:
                text = colored(f'Test case passed', 'green')
                print(text)

                # Warning if nonetype result
                if not result:
                    print(colored('(Warning: return value is NoneType)\n', 'cyan'))
                else:
                    print('\n')
                
                return 1

            else:
                text = colored('Test case failed', 'red')
                print(text)
                text = colored(f'Expected return: {self.expected}\nActual return value: {result}\n', 'yellow')
                print(text)
                return 0

        except Exception as e:
            print('!!!ERROR THROWN. Test case failed:\n')
            print(f'Error: {e}')
            traceback.print_exc()
            return 0



def run_tests():
    print('Running tests...\n')

    # Mute tests
    case1 = TestCase([True, None], toggle_mute, 'Mute All Test', 'Mute Master Volume (mutes everything)')
    case2 = TestCase([False, None], toggle_mute, 'Unmute All Test', 'Unmute Master Volume (unmutes everything)')

    case1.run()
    case2.run()


if __name__ == "__main__":
    run_tests()