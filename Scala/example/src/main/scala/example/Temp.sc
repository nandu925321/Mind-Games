
def abs(x:Double) = if(x<0) -x else x

def sqrtIter(guess:Double , x:Double):Double =
  if(isGoodEnough(guess ,x))guess
  else sqrtIter(improve(guess,x),x)

//check for difference-divided by x to make x proportional to the epsilon value so that good enough values can be found for very large or very small numbers
def isGoodEnough(guess:Double, x:Double) =
  abs( (guess*guess-x))/x<0.001

//improve guess
def improve(guess:Double,x:Double)=
  (guess + x /guess)/2

//sqrt
def sqrt(x:Double):Double = sqrtIter(1.0,x)

//call
sqrt(3e-20)