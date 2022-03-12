'''
Unit tests for Akira's functions.
'''
import time
from commands import *
import traceback
from termcolor import colored # Color terminal text (makes tests look cool and easier to read)


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
            desc:string: Description of the test case 
            expected_output:___: Expected output for the function. parameter type varies case-to-case
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


############### WINDOWS TESTS ###############

def run_tests():
    print('Running tests...\n')

    # Mute tests for master volume
    case1 = TestCase([True, None], toggle_mute, 'Mute All', 'Mute Master Volume (mutes everything)')
    case2 = TestCase([False, None], toggle_mute, 'Unmute All', 'Unmute Master Volume (unmutes everything)')

    # Mute tests for specific applications
    case3 = TestCase([True, 'chrome'], toggle_mute, 'Mute Google Chrome', 'Mute Google Chrome Volume')
    case4 = TestCase([False, 'chrome'], toggle_mute, 'Unmute Google Chrome', 'Unmute Google Chrome Volume')
    case5 = TestCase([True, 'chrome.exe'], toggle_mute, 'Errenous Mute call', 'Try to mute chrome with errenous call (will generate the app name "chrome.exe.exe")')
    case6 = TestCase([False, 'chrome.exe'], toggle_mute, 'Errenous Unmute call', 'Try to Unmute chrome with errenous call (will generate app name "chrome.exe.exe"')

    # Mute apps that don't exist
    case7 = TestCase([True, 'jvodsvjds jjen q'], toggle_mute, 'Mute non-existent', 'Try to mute nonexistent application')
    case8 = TestCase([False, 'jvodsvjds jjen q'], toggle_mute, 'Unmute non-existent', 'Try to Unmute nonexistent application')


    # Run tests
    case1.run() 
    case2.run()
    case3.run()
    case4.run()
    case5.run()
    case6.run()


if __name__ == "__main__":
    run_tests()