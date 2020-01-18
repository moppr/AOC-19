import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

public class Intersections{
	
	private ArrayList<String> text;
	private ArrayList<Point> intersections;

	public Intersections(ArrayList<String> text){	
		this.text = text;
		intersections = new ArrayList<Point>();
		generateIntersections();
	}
	
	private void generateIntersections(){		
		ArrayList<HashMap<Point, Integer>> wires = new ArrayList<HashMap<Point, Integer>>();
		
		for (String wire : text){			
			Point curr = new Point(0,0);
			int steps = 0;
			HashMap<Point, Integer> visited = new HashMap<Point, Integer>();
			curr.reset();
			
			for (String move : wire.split(",")){
				char direction = move.charAt(0);
				int dist = Integer.parseInt(move.substring(1));
				
				for (int i = 0; i < dist; i++){
					
					if (direction == 'U') curr.up();
					else if (direction == 'D') curr.down();
					else if (direction == 'L') curr.left();
					else if (direction == 'R') curr.right();
					else System.err.println("Invalid direction " + direction + " specified");
					
					steps++;
					
					boolean exists = false;					
					for (Point seen : visited.keySet()){
						if (curr.equals(seen)){
							exists = true;
							break;
						}
					}
					
					if (!exists) visited.put(curr.copy(), steps);
					
				}
			}
			
			wires.add(visited);
			
		}
		
		Set <Point> wire1 = wires.get(0).keySet();
		Set <Point> wire2 = wires.get(1).keySet();
		for (Point p : wire1){
			if (wire2.contains(p)){
				intersections.add(p);
			}
		}		
		
	}
	
	public int getManhattan(){
		int min = Integer.MAX_VALUE;
		for (Point p : intersections){
			int manh = p.manhattan();
//			System.out.println("Current point: " + p + " with distance " + manh);
			if (manh < min) min = manh;
		}
		
		return min;
	}

}
