import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day01{

	public static void main(String[] args) throws FileNotFoundException{
		File input = new File("01\\01.in");
		Scanner s = new Scanner(input);
		Fuel fuel = new Fuel();
		
		int simpleTotal = 0, thoroughTotal = 0;
		while (s.hasNextInt()){
			fuel.setMass(s.nextInt());
			simpleTotal += fuel.simpleFuel();
			thoroughTotal += fuel.thoroughFuel();
		}
		
		s.close();		
		System.out.println(simpleTotal + ", " + thoroughTotal);

	}
	
}
