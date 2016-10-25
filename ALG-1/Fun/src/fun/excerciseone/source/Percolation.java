package fun.excerciseone.source;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

	// main array
	private WeightedQuickUnionUF percolation;
	// fullness array
	private WeightedQuickUnionUF fullness;
	// is boolean array
	private boolean isOpen[];
	// is full array
	
	// top VS
	private int topVirtual;
	// bottom VS
	private int bottomVirtual;

	// size
	private int size;

	// helper methods
	private void validate(int x, int y) {
		if (x < 0 || x > size) {
			throw new IllegalArgumentException("Check co ordinates");
		}
		if (y < 0 || y > size) {
			throw new IllegalArgumentException("Check co ordinates");
		}

	}

	private int getIndexFromCoordinates(int x, int y) {
		validate(x, y);
		int index = ((x-1) * size) + y;
		return index;
	}

	// required methods
	public Percolation(int n) {
		// to be tested with n=1
		if (n < 1) {
			throw new IllegalArgumentException("Size must be greater than one");
		}
		size = n;
		/**
		 * 1.Initializing percolation to the size of required array
		 * setting top and bottom VS
		 */
		int arraySize = (size * size) + 2;
		topVirtual = 0;
		bottomVirtual = (size * size) + 1;
		isOpen = new boolean[arraySize];
		isOpen[topVirtual] = true;
		isOpen[bottomVirtual] = true;
		percolation = new WeightedQuickUnionUF(arraySize);
		fullness = new WeightedQuickUnionUF(arraySize);
		//connecting top and bottom VS to the layers
		for (int j=1 ; j<=size ;j++)
		{
			int i =1;
			int index = getIndexFromCoordinates(i, j);
			percolation.union(topVirtual, index);
			fullness.union(topVirtual, index);
			//isOpen[index] = true;
			
			i=size;
			index = getIndexFromCoordinates(i, j);
			percolation.union(bottomVirtual,index);
			//isOpen[index] = true;
			
			
			
		}
	}
	// call union here?
	public void open(int x, int y) {
	validate(x,y);
	int index = getIndexFromCoordinates(x, y);
	if( !isOpen[index] )
	{
		isOpen[index] = true;
		//check edges
		if(y>1 && isOpen(x, y-1))
		{
			int leftSide = getIndexFromCoordinates(x, y-1);
			percolation.union(index, leftSide);
			fullness.union(index, leftSide);
		}
		if(y<size && isOpen(x, y+1))
		{
			int rightSide = getIndexFromCoordinates(x, y+1);
			percolation.union(index, rightSide);
			fullness.union(index, rightSide);
		}
		//check top/bottom
		if(x>1 && isOpen(x-1,y))
		{
			int above = getIndexFromCoordinates(x-1, y);
			percolation.union(index, above);
			fullness.union(index, above);
		}
		if(x<size && isOpen(x+1,y))
		{
			int below = getIndexFromCoordinates(x+1, y);
			percolation.union(index, below);
			fullness.union(index, below);
		}
		
	}
	
	}

	public boolean isOpen(int row, int col) {
		int index = getIndexFromCoordinates(row, col);
		return isOpen[index];
	}

	public boolean isFull(int row, int col) {
		validate(row,col);
		int index = getIndexFromCoordinates(row, col);
		if(isOpen[index]&&fullness.connected(index, topVirtual))
		{return true;}
		return false;
	}

	public boolean percolates() {
		if(size>1)
		{
			return percolation.connected(topVirtual, bottomVirtual);
		}
		else
		{return isOpen(1,1);}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//Percolation p = new Percolation(4);
		//System.out.println(p.getIndexFromCoordinates(2, 2));
		Percolation percolation = new Percolation(1);
        StdOut.println(percolation.percolates());
        percolation.open(1,1);
        StdOut.println(percolation.percolates());
        Percolation percolation2 = new Percolation(2);
        StdOut.println(percolation2.percolates());
        percolation2.open(1,1);
        StdOut.println(percolation2.percolates());
        percolation2.open(2,1);
        StdOut.println(percolation2.percolates());

	}

}
