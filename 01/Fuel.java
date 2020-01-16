public class Fuel{
	
	int mass;
	
	public void setMass(int mass){
		this.mass = mass;
	}

	public int simpleFuel(){
		return Math.floorDiv(mass, 3) - 2;
	}
	
	public int thoroughFuel(){
		int total = 0;
		while (mass > 0){
			mass = simpleFuel();
			total += Math.max(0, mass);
		}
		return total;
	}

}
