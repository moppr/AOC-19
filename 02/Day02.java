import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Day02{

	public static void main(String[] args) throws FileNotFoundException{
		File input = new File("02\\02.in");
		Scanner s = new Scanner(input);
		
		Intcode intcode = new Intcode(s.next());
		s.close();
		
		System.out.println(intcode.run(12, 2));
		
		for (int noun = 0; noun < 100; noun++){
			for (int verb = 0; verb < 100; verb++){
				if (intcode.run(noun, verb) == 19690720)
					System.out.println(100*noun + verb);
			}
		}

	}

}
