
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
val s: List[Int] = List(1)
s.tail
val xs: List[Int] = List(1, 1, 1, 1)
def sum(xs: List[Int]): Int = {
  def loop( acc:Int,xs:List[Int]):Int={
    if(xs.isEmpty)  acc else loop(acc+xs.head,xs.tail)
  }
  loop(0,xs)
}
sum(xs)


 def max(xs: List[Int]): Int = {
  def maxIter(a: Int, xs: List[Int]): Int = {
    if (xs.isEmpty) a
    else  a.max(maxIter(xs.head, xs.tail))
  }
  maxIter(xs.head, xs.tail)
}

max(xs)

