import java.util.ArrayList;
import java.util.Scanner;

public class Intcode{
	
	private String text;

	public Intcode(String text){	
		this.text = text;
	}
	
	public int run(int noun, int verb){
		ArrayList<Integer> program = new ArrayList<Integer>();
		Scanner s = new Scanner(text);
		s.useDelimiter(",");
		while (s.hasNext()){
			program.add(Integer.parseInt(s.next()));
		}		
		s.close();
		
		program.set(1, noun);
		program.set(2, verb);
		
		int i = 0;
		while (true){
			int opcode = program.get(i);
			int a,b,c;
			
			switch (opcode){
			case 1: //SUM
				a = program.get(i+1);
				b = program.get(i+2);
				c = program.get(i+3);
				program.set(c, program.get(a) + program.get(b));
				i += 4;
				break;
			case 2: //PROD
				a = program.get(i+1);
				b = program.get(i+2);
				c = program.get(i+3);
				program.set(c, program.get(a) * program.get(b));
				i += 4;
				break;
				
			case 99: //HALT
				return program.get(0);
				
			default:
				System.err.println("Invalid opcode " + opcode + " given");
			}
			
		}
		
	}

}
