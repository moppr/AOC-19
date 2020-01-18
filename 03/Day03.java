import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Day03{

	public static void main(String[] args) throws FileNotFoundException{
		File input = new File("03\\03.in");
		Scanner s = new Scanner(input);
		
		ArrayList<String> text = new ArrayList<String>();
		while (s.hasNext()){
			text.add(s.nextLine());
		}
		
		Intersections intersections = new Intersections(text);
		s.close();
		
		System.out.println(intersections.getManhattan());

	}

}
