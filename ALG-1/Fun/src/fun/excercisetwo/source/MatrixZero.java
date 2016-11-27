/**
 * 
 */
package fun.excercisetwo.source;

import java.util.Scanner;

/**
 * @author sourabh
 *
 */
public class MatrixZero {

	/**
	 * @param args
	 */
	private void putZeros(int arr [][],int M, int N)
	{
		boolean [] flag = new boolean [M];
		for (int i=0; i<=M ;i++)
		{
			for(int j=0; j<=N; j++)
			{
				if(!flag[i])
				{}
			}
		}
	}
	
	public static void main(String[] args) {
		//Take in a int matrix and feed it to zeros array
		System.out.println("Enter the matrix size M*N");
		Scanner sc  = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		int [][] arr = new int [M][N];
		System.out.println("Enter the matrix");
		for(int i=0;i<M;i++)
		{
			for(int j=0;j<N;j++)
			{
				arr[i][j] = sc.nextInt();
			}
		}
		sc.close();
		
		for(int i=0;i<M;i++)
		{
			for(int j=0;j<N;j++)
			{
				System.out.print(arr[i][j]+"\t");
			}
			System.out.println();
		}
	}

}
