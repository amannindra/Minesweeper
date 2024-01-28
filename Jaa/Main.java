import java.util.Scanner; 
import java.util.*; 

public class Main
{
	public static void main(String[] args) {
	    Scanner User = new Scanner(System.in);
	    
	    System.out.println("How many rows due to want?");
	    String UserRowsobject = User.nextLine();
	    
	    System.out.println("How many colums due to want?");
	    String UserColsobject = User.nextLine();
	    
	    System.out.println("Probability of Mines?(In Percentage, no 25 only 0.25)");
	    String probability = User.nextLine();
	    double a = Double.parseDouble(probability);
	    System.out.println("Click a Squares(x)");
	    String clickSquarex = User.nextLine();
	    System.out.println("Click a Squares(y)");
	    String clickSquarey = User.nextLine();
	    
	    
	    Minesweeper ms = new Minesweeper(Integer.parseInt(UserRowsobject),Integer.parseInt(UserColsobject), a, Integer.parseInt(clickSquarex), Integer.parseInt(clickSquarey));
	    ms.setminedSquares();
	    
	}
}


