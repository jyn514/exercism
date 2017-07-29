public class PangramChecker {
    public boolean isPangram(String input) {
    	if (input.length() < 26) return false;
    	input = input.toLowerCase();
    	String alphabet = "abcdefghijklmnopqrstuvwxyz";
    	for (int i = 1; i < 26; i++) {
    		if (!input.contains(alphabet.substring(i, i+1))) return false;
    	}
    	return true;
    }
}
