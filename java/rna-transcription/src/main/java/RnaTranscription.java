public class RnaTranscription {
	public java.util.Map<String, String> makeDict() {
	    java.util.Map<String, String> changes = new java.util.HashMap<>();
	    changes.put("G", "C");
	    changes.put("C", "G");
	    changes.put("T", "A");
	    changes.put("A", "U");
	    return changes;
	}
    
	public String transcribe(String dnaStrand) {
		String rnaStrand = "";
		java.util.Map<String, String> changes = makeDict();
		for(int i = 0; i < dnaStrand.length(); i++) {
			rnaStrand += changes.get(dnaStrand.substring(i, i+1));
			}
		return rnaStrand;
	}
}
