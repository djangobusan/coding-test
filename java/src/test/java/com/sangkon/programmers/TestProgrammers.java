package com.sangkon.programmers;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class TestProgrammers {

	@Test
	void testFindPrime() {
		FindPrime findPrime = new FindPrime();
		assertEquals(findPrime.solution("17"), 3);
		assertEquals(findPrime.solution("011"), 2);
	}

	@Test
	void testTravelRoute() {
		TravelRoute travelRoute1 = new TravelRoute();
		String[][] input1 = new String[][] { { "ICN", "JFK" }, { "HND", "IAD" }, { "JFK", "HND" } };
		String[] output1 = new String[] { "ICN", "JFK", "HND", "IAD" };

		TravelRoute travelRoute2 = new TravelRoute();
		String[][] input2 = new String[][] { { "ICN", "SFO" }, { "ICN", "ATL" }, { "SFO", "ATL" }, { "ATL", "ICN" },
				{ "ATL", "SFO" } };
		String[] output2 = new String[] { "ICN", "ATL", "ICN", "SFO", "ATL", "SFO" };

		assertArrayEquals(travelRoute1.solution(input1), output1);
		assertArrayEquals(travelRoute2.solution(input2), output2);
	}

	@Test
	void testWordConversion() {
		WordConversion wordConversion = new WordConversion();
		String[] input1 = new String[] { "hot", "dot", "dog", "lot", "log", "cog" };
		String[] input2 = new String[] { "hot", "dot", "dog", "lot", "log" };

		assertEquals(wordConversion.solution("hit", "cog", input1), 4);
		assertEquals(wordConversion.solution("hit", "cog", input2), 0);
	}

	@Test
	void testFurthestNode() {
		FurthestNode furthestNode = new FurthestNode();
		assertEquals(furthestNode.solution(6,
				new int[][] { { 3, 6 }, { 4, 3 }, { 3, 2 }, { 1, 3 }, { 1, 2 }, { 2, 4 }, { 5, 2 } }), 3);
	}

	@Test
	void testSheepAndWolves() {
		SheepAndWolves sheepAndWolves = new SheepAndWolves();
		assertEquals(sheepAndWolves.solution(new int[] { 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1 }, new int[][] { { 0, 1 },
				{ 1, 2 }, { 1, 4 }, { 0, 8 }, { 8, 7 }, { 9, 10 }, { 9, 11 }, { 4, 3 }, { 6, 5 }, { 4, 6 }, { 8, 9 } }),
				5);
		assertEquals(sheepAndWolves.solution(new int[] { 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0 }, new int[][] { { 0, 1 },
				{ 0, 2 }, { 1, 3 }, { 1, 4 }, { 2, 5 }, { 2, 6 }, { 3, 7 }, { 4, 8 }, { 6, 9 }, { 9, 10 } }), 5);
	}

}
