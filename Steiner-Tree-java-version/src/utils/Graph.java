https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
package utils;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Graph {
	public long n, e, t;
	public Set<Pair> p_edges = new HashSet<>();
	public List<Long> terminals = new ArrayList<>();
	public List<DoublePair> edges = new ArrayList<>();
	public List<List<Long>> adj_marix = new ArrayList<>();
	public List<List<Long>> dist = new ArrayList<>();;
	public List<List<Long>> next = new ArrayList<>();;
	public List<List<List<Long>>> path = new ArrayList<>();
	
	public Graph(String filename) {
		
	}
	
	public void graph_add_edge(long u, long v, long w) {
		this.edges.add(new DoublePair(u, v, w));
	}
	
	public void generate_adj_matrix() {
		for(int i = 0; i < n; i ++) {
			List<Long> t = new ArrayList<Long>(n > Integer.MAX_VALUE ? Integer.MAX_VALUE : (int) n);
			for(long j = 0l; j < n; j ++) {
				t.add(Long.MAX_VALUE);
			}
			this.adj_marix.add(t);
			this.adj_marix.get(i).set(i, 0L);
		}
	}
	
	public void All_Pairs_Shortest_Path() {
		
	}
	
	public void Find_path(long u,long v) {
		
	}
	
	public void ST_path() {
		
	}
	
	public void printPath(long u,long v) {
		
	}
}
