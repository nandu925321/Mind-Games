

def sqrt(x: Double): Double = {

  def abs(x: Double) = if (x < 0) -x else x
  //eliminated x as it is duplicated as in inside the block
  def sqrtIter(guess: Double): Double =
  if (isGoodEnough(guess)) guess
  else sqrtIter(improve(guess))

  //check for difference-divided by x to make x proportional to the epsilon value so that good enough values can be found for very large or very small numbers
  def isGoodEnough(guess: Double) =
  abs((guess * guess - x)) / x < 0.001

  //improve guess
  def improve(guess: Double) =
  (guess + x / guess) / 2

  //sqrt
  sqrtIter(1.0)

}
//call
sqrt(3e-20)