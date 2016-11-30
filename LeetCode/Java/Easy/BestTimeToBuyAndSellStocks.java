package Easy;

public class BestTimeToBuyAndSellStocks {

	public static void main(String[] args) {
		int[] test = {7, 1, 5, 3, 6, 4};
		System.out.println(maxProfit(test));
	}
	
	
	public static int maxProfit(int[] prices){
		if (prices.length < 2){
			return 0;
		}
		int min = 0;
		int ptr = 1;
		int max = prices[ptr] - prices[min];
		
		while (ptr < prices.length){
			if (prices[ptr] < prices[min]){
				min = ptr;
			}
			if (prices[ptr] - prices[min] > max){
				max = prices[ptr] - prices[min];
			}
			ptr++;
			
		}
		return max;
	}

}
