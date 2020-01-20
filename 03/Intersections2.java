import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

public class Intersections2{
	
	private ArrayList<String> text;
	private ArrayList<Integer[]> intersections;

	public Intersections2(ArrayList<String> text){	
		this.text = text;
		intersections = new ArrayList<Integer[]>();
		generateIntersections();
	}
	
	private void generateIntersections(){		
		ArrayList<HashMap<Integer[], Integer>> wires = new ArrayList<HashMap<Integer[], Integer>>();
		
		for (String wire : text){
			int steps = 0;
			int x = 0;
			int y = 0;
			HashMap<Integer[], Integer> visited = new HashMap<Integer[], Integer>();
			
			for (String move : wire.split(",")){
				char direction = move.charAt(0);
				int dist = Integer.parseInt(move.substring(1));
				
				for (int i = 0; i < dist; i++){
					
					if (direction == 'U') y++;
					else if (direction == 'D') y--;
					else if (direction == 'L') x--;
					else if (direction == 'R') x++;
					else System.err.println("Invalid direction " + direction + " specified");
					
					steps++;
					
					boolean exists = false;					
					for (Integer[] seen : visited.keySet()){
						if (seen[0] == x && seen[1] == y){
							exists = true;
							break;
						}
					}
					
					if (!exists){
						visited.put(new Integer[]{x,y}, steps);
//						System.out.println("Visited " + x + ", " + y);
					}
					
				}
			}
			
			wires.add(visited);
			
		}
		
		Set <Integer[]> wire1 = wires.get(0).keySet();
		Set <Integer[]> wire2 = wires.get(1).keySet();
		for (Integer[] p : wire1){
			if (wire2.contains(p)){
				System.out.println("Added an intersection " + p + "...");
				intersections.add(p);
			}
		}		
		
	}
	
	public int getManhattan(){
		int min = Integer.MAX_VALUE;
		for (Integer[] p : intersections){
			int manh = Math.abs(p[0]) + Math.abs(p[1]);
//			System.out.println("Current point: " + p + " with distance " + manh);
			if (manh < min) min = manh;
		}
		
		return min;
	}

}
