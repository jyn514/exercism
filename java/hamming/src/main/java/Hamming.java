public class Hamming {
	public String leftStrand, rightStrand;
	static final String DNA = "GCTA";
	
    Hamming(String initialLeftStrand, String initialRightStrand) {
    	leftStrand = initialLeftStrand;
    	rightStrand = initialRightStrand;
    	if (leftStrand.length() != rightStrand.length()) {
    		throw new IllegalArgumentException(
    			"leftStrand and rightStrand must be of equal length.");
    	}
    	for (int i=0; i < leftStrand.length(); i++) {
    		if (! DNA.contains(leftStrand.substring(i, i+1)) 
    				&& DNA.contains(rightStrand.substring(i, i+1))) {
    			throw new IllegalArgumentException(
    				"strands must have only the characters 'GCTA'");
    		}
    	}
    }

    int getHammingDistance() {
    	int count = 0;
    	for (int i=0; i < leftStrand.length(); i++) {
    		if (leftStrand.charAt(i) != rightStrand.charAt(i)) 
    			count += 1;
    	}
    	return count;
    }

}
