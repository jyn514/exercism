import java.time.LocalDate;
import java.time.LocalDateTime;

class Gigasecond {
	LocalDateTime ldt;
	static final long billion = 1000000000;
	
    Gigasecond(LocalDate birthDate) {ldt = birthDate.atStartOfDay();}
    Gigasecond(LocalDateTime birthDateTime) {ldt = birthDateTime;	}
    LocalDateTime getDate() {return ldt.plusSeconds(billion); 		}
}
