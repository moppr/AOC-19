import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day01{
	
	static Fuel fuel = new Fuel();

	public static void main(String[] args) throws FileNotFoundException{
		File input = new File("01\\01.in");
		Scanner s = new Scanner(input);
		int simpleTotal = 0, thoroughTotal = 0;
		while (s.hasNextInt()){
			int mass = s.nextInt();
			simpleTotal += fuel.simpleFuel(mass);
			thoroughTotal += fuel.thoroughFuel(mass);
		}
		
		System.out.println(simpleTotal + ", " + thoroughTotal);

	}

}
