package Easy;

public class CanPlaceFlowers {
	public static void main(String[] args){
		
	}
	
	public boolean canPlaceFlowers(int[] flowerbed, int n){
		int emptySpots = 1;
		int flowersCanBePlaced = 0;
		for (int i = 0; i < flowerbed.length; i++){
			if (flowerbed[i] == 1){
				flowersCanBePlaced += (emptySpots - 1 )/2;
				emptySpots = 0;
			} else {
				emptySpots++;
			}
		}
		if (emptySpots >= 2) flowersCanBePlaced += emptySpots/2;
		
		return flowersCanBePlaced >= n;
	}

}
