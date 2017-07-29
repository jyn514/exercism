import java.util.Map;

class Scrabble {
	public String word;
	Map<String, Integer> scores;
	
    Scrabble(String initialWord) {
    	word = initialWord;
    	scores = createScoreMap();
    }

    int getScore() {
    	int score = 0;
    	for (int i = 0; i < word.length(); i++) {
    		score += scores.get(word.substring(i, i+1).toUpperCase());
    	}
    	return score;
    }

    Map<String, Integer> createScoreMap() {
    	Map<String, Integer> scores = new java.util.HashMap<>();
    	// organized by score; chars in letters[0] are worth 1 point
    	String[] letters = { "AEIOULNRST", "DG", "BCMP",
    		"FHVWY", "K", "", "", "JX", "", "QZ" };
    	for (int i = 0; i < 10; i++) {
    		for (int j = 0; j < letters[i].length(); j++) {
    			scores.put(letters[i].substring(j, j+1), i+1);
    		}
    	}
    	return scores;
    }
    
}