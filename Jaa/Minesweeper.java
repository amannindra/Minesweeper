public class Minesweeper
{

  private boolean[][] minedSquares;
  private boolean[][] clickedSquares;
  private boolean[][] flaggedSquares;
  private int[][] nearbyMines;
  private boolean game;
  private boolean mineClicked;
  private boolean playerWon;
  private int mineCount;
  private int flagCount;
  private double probability;
  private int clickxx;
  private int clickyy;

  public Minesweeper (int rows, int cols, double probabilit, int clickx, int clicky)
  {
    probability = probabilit;
    minedSquares = new boolean[rows][cols];
    clickedSquares = new boolean[rows][cols];
    flaggedSquares = new boolean[rows][cols];
    nearbyMines = new int[rows][cols];
    clickxx = clickx;
    clickyy = clicky;
    
    

  }
  public void printboolean()
  {
    System.out.println ();
    for (int i = 0; i < minedSquares.length; i++)
      {
	    for (int j = 0; j < minedSquares[0].length; j++)
	    {
	        System.out.print(minedSquares[i][j] + " ");
	    }
	  System.out.println ();
      }
  }
  public void setminedSquares()
  {
    for(int i = 0; i < minedSquares.length;i++)
    {
        for(int j = 0;j < minedSquares[0].length; j++)
        {
            if(Math.random() < probability)
                minedSquares[i][j] = true;
            if(minedSquares[i][j] == true)
                System.out.print("M ");
            else
                System.out.print("0 ");
        }
        System.out.println();
    }
  }
  public boolean[][] setClickSquare()
  {
      System.out.println();
      for (int i = 0; i < clickSquares.length; i++)
      {
	      for (int j = 0; j < clickSquares[0].length; j++)
	      {
	          clickSquares[i][j] = false;
	      }
      }  
  }
  public void setclickSqaures()
  {
    for(int i = 0; i < clickSquares.length;i++)
    {
        for(int j = 0;j < clickSquares[0].length; j++)
        {
            if(clickSquares[i][j] == clickSquares[clickxx][clickyy])
                clickSquares[i][j] = true;
            if(clickSquares[i][j] == true)
                System.out.print("C");
        }
        System.out.println();
    }
  }
}
