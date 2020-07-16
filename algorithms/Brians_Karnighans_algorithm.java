
// this algorithm counts number of set bits in a integer
// Time complexsity : O(logn)
// space Complexsity : O(1)

public class Brians_karnighans_algorithm{

	public int getSetBitsCount(int num)
    {
        // Brian's karnighans algorithm
        int count = 0;
        
        while(num > 0)
        {
            num = num & (num-1);
            count++;
        }
        
        return count;
    }

	public static void main(String[] args) {
		System.out.println( getSetBitsCount(5));
	}

}