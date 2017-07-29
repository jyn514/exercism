class Acronym {
	String acronym = "";
	
    Acronym(String phrase) {
    	for (int i = 0; i < phrase.length(); i++) {
    		String letter = phrase.substring(i, i+1);
    		if (i == 0) {
    			acronym += letter;	}
    		else {   			
	    		char previous = phrase.charAt(i - 1); 
	    		if (previous == ' ' || previous == '-') {
	    			acronym += letter.toUpperCase();
	    		}
    		}
    	}
    }

    String get() { return acronym; }

}
