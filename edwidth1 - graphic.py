Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f():
	x=10
	y=100
	return x, y

>>> print(f())
(10, 100)
>>> (a, b) = f()
>>> print(a + "ff" +b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a + "ff" +b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(a + b )
110
>>> print(a b)
SyntaxError: invalid syntax
>>> print(a, b)
10 100
>>> print((a,b))
(10, 100)
>>> def input(text):
	return text
name = input("hello")
SyntaxError: invalid syntax
>>> name = input("hello")
hello
>>> name = input("what is your name?")
what is your name?Hyerim
>>> print(name)
Hyerim
>>> raw_n = input("how many number?")
how many number?20
>>> print(raw_n)
20
>>> type(raw_n)
<class 'str'>
>>> n = int(raw_n)
>>> type(n)
<class 'int'>
>>> print(n)
20
>>> def foo(id, name):
	id = name
	name = id
	return (id, name)

>>> id = 3
>>> name = "kim"
>>> id, name = foo(id, name)
>>> print(id, name)
kim kim
>>> number = input("fff")
fff12.3
>>> type(number)
<class 'str'>
>>> import math
>>> import sys
>>> import urllib
>>> import cs1robots
>>> import cs1pgraphics
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    import cs1pgraphics
ModuleNotFoundError: No module named 'cs1pgraphics'
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help("math")
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> help("cs1robot")
No Python documentation found for 'cs1robot'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help("cs1robots")
Help on module cs1robots:

NAME
    cs1robots

DESCRIPTION
    # cs1robots.py
    #
    # Environment for steering a robot through a grid world
    # for learning to program in Python
    #
    # Inspired by and using code from RUR-PLE by Andre Roberge
    #
    # 2010/01/14 Otfried Cheong
    # 2010/02/23: Changed to refresh only once after every move
    # 2010/02/24: Fixed refresh in world editing.
    # 2010/08/12: Improved handling of beepers to speed up.
    # 2015/10/23 Jungkook Park
    # 2015/10/23: Add Py3k compatibility and use Pillow instead of PIL
    #
    # On Linux, need packages python-tk, python-imaging-tk
    #

CLASSES
    builtins.Exception(builtins.BaseException)
        RobotError
    builtins.object
        Robot
    
    class Robot(builtins.object)
     |  Robot(color='gray', orientation='E', beepers=0, avenue=1, street=1)
     |  
     |  Methods defined here:
     |  
     |  __del__(self)
     |  
     |  __init__(self, color='gray', orientation='E', beepers=0, avenue=1, street=1)
     |      Create a new robot.
     |  
     |  carries_beepers(self)
     |      Returns True if some beepers are left in Robot's bag.
     |  
     |  drop_beeper(self)
     |      Robot drops one beeper down at current location.
     |  
     |  facing_north(self)
     |      Returns True if Robot is facing north.
     |  
     |  front_is_clear(self)
     |      Returns True if no wall or border in front of robot.
     |  
     |  get_pos(self)
     |      Returns current robot position.
     |  
     |  left_is_clear(self)
     |      Returns True if no walls or borders are to the immediate left
     |      of the robot.
     |  
     |  move(self)
     |      Move one street/avenue in direction where robot is facing.
     |  
     |  on_beeper(self)
     |      Returns True if beepers are present at current robot position.
     |  
     |  pick_beeper(self)
     |      Robot picks one beeper up at current location.
     |  
     |  right_is_clear(self)
     |      Returns True if no walls or borders are to the immediate right
     |      of the robot.
     |  
     |  set_pause(self, delay=0)
     |      Set a pause to be made after each move.
     |  
     |  set_trace(self, color=None)
     |      Without color argument, turn off tracing.
     |      With color argument, start a new trace in that color.
     |  
     |  turn_left(self)
     |      Rotate left by 90 degrees.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class RobotError(builtins.Exception)
     |  RobotError(str)
     |  
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      RobotError
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, str)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args

FUNCTIONS
    create_world(avenues=10, streets=10)
        Create an empty robot world.
    
    edit_world()
        Edit the current robot world.
        You can add and remove walls by clicking at the wall position.
        Add a beeper by clicking with the left button at an intersection.
        Remove a beeper with the right mouse button.
    
    load_world(filename=None)
        Loads a robot world from filename.
        Opens file-chooser if no filename is given.
    
    pause(delay=1.0)
        Pause for delay seconds.
    
    save_world(filename=None)
        Save a robot world to filename.
        Opens file-chooser if no filename is given.

FILE
    c:\users\cnrrn\appdata\local\programs\python\python37\lib\cs1robots.py


>>> from cs1robots import *
>>> from cs1graphics import *
>>> canvas = Canvas(400, 300)
>>> canvas.setBackgroundColor("light blue")
>>> canvas.setTitle("CS101 Drawing 그림ㅋ")
>>> canvas.Circle(30)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    canvas.Circle(30)
AttributeError: 'Canvas' object has no attribute 'Circle'
>>> canvas.Text("fff", 24)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    canvas.Text("fff", 24)
AttributeError: 'Canvas' object has no attribute 'Text'
>>> sq = Square(100)
>>> canvas.add(sq)
>>> sq.setFillColor("red")
>>> sq.setFillColor("blue")
>>> sq.setBorderColor("red")
>>> sq.setBorderWidth(5)
>>> sq.moveTo(200, 200)
>>> for i in range(100):
	sq.move(1,0)
	time.sleep(0,1)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 3, in <module>
    time.sleep(0,1)
NameError: name 'time' is not defined
>>> import time
>>>  for i in range(100):
	sq.move(1,0)
	time.sleep(0,1)

SyntaxError: unexpected indent
>>>  for i in range(100):
	sq.move(1,0)
	time.sleep(0.1)
	
SyntaxError: unexpected indent
>>> for i in range(100):
	sq.move(1,0)
	time.sleep(0.1)

	
>>> r = Rectangle(150, 75)
>>> canvas.add(r)
>>> r.setFillColor("yellow")
>>> r.moveTo(280, 150)
>>> sq.setDepth(10)
>>> r.setDepth(20)
>>> sq.rotate(45)
>>> sq.scale(1.5)
>>> sq.scale(0.5)
>>> r.scale(0.7)
>>> for i in range(80):
	r.scale(1.2)

	
>>> r.scale(0.1)
>>> for i in range(50):
	r.scale(0.2)

	
>>> car = Layer()
>>> tirel = Circle(10, Point(-20, -10))
>>> tirel.setFillColor("black")
>>> car add(tirel)
SyntaxError: invalid syntax
>>> car.add(tirel)
>>> tire2 = Circl(10, Point(20,-10))
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    tire2 = Circl(10, Point(20,-10))
NameError: name 'Circl' is not defined
>>> tire2 = Circle(10, Point(20,-10))
>>> tire2.setFillColor("black")
>>> car.add(tire2)
>>> body = Rectangle(70, 30, Point(0,-25))
>>> body.setFillColor("blue")
>>> body.setDepth(60)
>>> car.add(body)
>>> canvas.add(car)
>>> car.moveto(100, 100)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    car.moveto(100, 100)
AttributeError: 'Layer' object has no attribute 'moveto'
>>> car.moveTo(100, 100)
>>> for i range(100):
	
SyntaxError: invalid syntax
>>> for i in range(100):
	car.move(2,0)

	
>>> 
