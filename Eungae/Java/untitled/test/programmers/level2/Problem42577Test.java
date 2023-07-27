package programmers.level2;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Problem42577Test {
    @Test
    void solution() {
        Problem42577 temp = new Problem42577();
        boolean result = temp.solution(new String[]{"123", "456", "789"});
        assertEquals(true, result);
    }
}
