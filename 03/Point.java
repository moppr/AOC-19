public class Point{
	
	private int x, y;

	public Point(int x, int y){
		this.x = x;
		this.y = y;
	}

	@Override
	public String toString(){
		return "(" + x + ", " + y + ")";
	}
	
	public int manhattan(){
		return Math.abs(x) + Math.abs(y);
	}
	
	public void up(){
		y++;
	}
	
	public void down(){
		y--;
	}
	
	public void left(){
		x--;
	}
	
	public void right(){
		x++;
	}
	
	/***
	 * this method might not be necessary - try removing reset call from intersections
	 * and seeing if outcome changes after optimizing
	 */
	public void reset(){
		x = 0;
		y = 0;
	}
	
	public Point copy(){
		return new Point(x, y);
	}

	@Override
	public int hashCode(){
		final int prime = 31;
		int result = 1;
		result = prime * result + x;
		result = prime * result + y;
		return result;
	}

	@Override
	public boolean equals(Object obj){
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Point other = (Point) obj;
		if (x != other.x)
			return false;
		if (y != other.y)
			return false;
		return true;
	}

}
