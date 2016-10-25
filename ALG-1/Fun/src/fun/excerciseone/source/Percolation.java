package fun.excerciseone.source;

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {

	// main array
	private WeightedQuickUnionUF percolation;
	// fullness array
	private WeightedQuickUnionUF fullness;
	// is boolean array
	private boolean isOpen[];
	// is full array
	private boolean isFull[];
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
		int index = ((y-1) * size) + x;
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
		
		
	}
	
	}

	public boolean isOpen(int row, int col) {
		int index = getIndexFromCoordinates(row, col);
		return isOpen[index];
	}

	public boolean isFull(int row, int col) {
		return false;
	}

	public boolean percolates() {
		return false;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Percolation p = new Percolation(4);
		//System.out.println(p.isOpen[5]);

	}

}
