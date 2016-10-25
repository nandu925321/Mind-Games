/**
 * 
 */
package fun.excerciseone.source;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

/**
 * @author sourabh.parime
 *
 */
public class PercolationStats {

	/**
	 * @param args
	 */
	 
	 //required methods
	 private double threshResults[];
	 private double T;
	 public PercolationStats(int n, int trials)
	 {
		 if(n<1 || trials<1)
		 {throw new IllegalArgumentException("invalid arguments in size or number of trials");}
		 threshResults = new double [trials];
		 this.T = trials;
		 for(int t = 0;t<trials;t++)
		 {
			 int openSites = 0;
			 Percolation percolation = new Percolation(n);
			 while (!percolation.percolates())
			 {
				 int i = StdRandom.uniform(1,n+1);
				 int j = StdRandom.uniform(1,n+1);
				 if (!percolation.isOpen(i,j))
	                {
	                    percolation.open(i,j);
	                    openSites += 1;
	                }
			 }
			 double result = (double)openSites/(double)(n*n);
			 threshResults[t] = result;
			 
		 }
	 }
	   public double mean()
	   {
		return StdStats.mean(threshResults);   
	   }
	   public double stddev()
	   {
		   return StdStats.stddev(threshResults);
	   }
	   public double confidenceLo()
	   {
		   return mean()-(1.96*stddev()/Math.sqrt(T));
	   }
	   public double confidenceHi()
	   {
		   return mean()+(1.96*stddev()/Math.sqrt(T));
	   }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		   //int N = StdIn.readInt();
	       //int T = StdIn.readInt();
		   int N=5000;
		   int T=1000;
	       PercolationStats stats = new PercolationStats(N,T);
	       StdOut.println("mean = "+ stats.mean());
	       StdOut.println("standard deviation = "+ stats.stddev());
	       StdOut.println("95% confidence interval = "+ stats.confidenceLo() + " , " + stats.confidenceHi());

	}

}
