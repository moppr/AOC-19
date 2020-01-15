public class Fuel{
	
	int simpleFuel(int mass){
		return Math.floorDiv(mass, 3) - 2;
	}
	
	int thoroughFuel(int mass){
		int total = 0;
		while (mass > 0){
			mass = simpleFuel(mass);
			total += Math.max(0, mass);
		}
		return total;
	}

}
