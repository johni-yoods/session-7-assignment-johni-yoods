import os,inspect,re,random
import session7
import pytest

README_CONTENT_CHECK_FOR = [
    'gen_next_number',
    'min_count',
    'doc_string',
    'fibonacci',
    'count',
    'dictionary',
]
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 200, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



def test_docstring_check():
    # check the doc string has more than 50 characters
    ret = session7.docstring_check(session7.fib)
    assert ret() == True,'Error, expected atleast 50 characters of doc string'

def test_no_docstring():
    # check it returns False for no doc string
    ret = session7.docstring_check(test_readme_exists)
    assert ret() == False,'Error, expected atleast 50 characters of doc string'

def test_doc_string():
    ret = session7.docstring_check(test_function_name_had_cap_letter)
    assert ret() == False,'just do a character by character count.'

def test_fibonacci():
    fib_list = [1,2,3,5,8,13]
    ret = session7.fib()
    for i in fib_list:
        assert i ==ret(),'It is not fabonacci series'

def test_counter():
    ret = session7.counter(session7.add)
    for i in range(1,11):
        assert ret(random.randint(1,100),random.randint(1,100)) == i ," not counting properly"

def test_div():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(1,100)
        assert(session7.div(number1,number2)==number1/number2),'Error' 
        number2 = random.randint(-100,-1)
        assert(session7.div(number1,number2)==number1/number2),'Error' 
    
def test_add():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(-100,100)
        assert(session7.add(number1,number2)==number1+number2),'you learned addition in 1st?? or you skipped it..' 


def test_mul():
    for _ in range(10):
        number1 = random.randint(-100,100)
        number2 = random.randint(-100,100)
        assert(session7.mul(number1,number2)==number1*number2),'you learned multiplication in 1st?? or you skipped it..' 

def test_count_with_global_dict():
    dict_val = {'add':4,'mul':3,'div':2}
    fn = session7.add
    func = session7.count_with_global_dict(fn)
    for i in range(4):
        func(random.randint(1,50),random.randint(1,50))
    fn = session7.mul
    func = session7.count_with_global_dict(fn)
    for i in range(3):
        func(random.randint(1,50),random.randint(1,50))
    fn = session7.div
    func = session7.count_with_global_dict(fn)
    for i in range(2):
        func(random.randint(1,50),random.randint(1,50))
    assert session7.count_dict == dict_val,'Not counting properly..'

def test_count_with_user_dict():
    dict_val = {'add':4,'mul':3,'div':2}
    count_dict= {'add':0,'mul':0,'div':0}
    fn = session7.add
    func = session7.count_with_user_dict(fn,count_dict)
    for i in range(4):
        func(random.randint(1,50),random.randint(1,50))
    fn = session7.mul
    func = session7.count_with_user_dict(fn,count_dict)
    for i in range(3):
        func(random.randint(1,50),random.randint(1,50))
    fn = session7.div
    func = session7.count_with_user_dict(fn,count_dict)
    for i in range(2):
        func(random.randint(1,50),random.randint(1,50))
    assert count_dict == dict_val,'just count how many times each funtion is called..'


def test_check_docs():

    assert bool(session7.docstring_check.__doc__)==True,"Docstring missing"
    assert bool(session7.fib.__doc__)==True,"Docstring missing"
    assert bool(session7.add.__doc__)==True,"Docstring missing"
    assert bool(session7.mul.__doc__)==True,"Docstring missing"
    assert bool(session7.div.__doc__)==True,"Docstring missing"
    assert bool(session7.counter.__doc__)==True,"Docstring missing"
    assert bool(session7.count_with_global_dict.__doc__)==True,"Docstring missing"
    assert bool(session7.count_with_user_dict.__doc__)==True,"Docstring missing"

def test_check_closure():
    func = session7.docstring_check(session7.fib)
    assert bool(func.__closure__ ) ==True, "Error"
    func = session7.fib()
    assert bool(func.__closure__ ) ==True, "Error"
    func = session7.counter(session7.add)
    assert bool(func.__closure__ ) ==True, "Error"
    fn = session7.add
    func = session7.count_with_global_dict(fn)
    assert bool(func.__closure__ ) ==True, "Error"
    count_dict= {'add':0,'mul':0,'div':0,}
    fn = session7.add
    func = session7.count_with_user_dict(fn,count_dict)
    assert bool(func.__closure__ ) ==True, "Error"
