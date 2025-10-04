# Topics & Techniques

A field guide to the algorithmic topics that show up across the problems in this
repo: the theory behind each, how to *recognize* when it applies, and the usual
techniques and ways of thinking that solve it. Representative problems are named
inline — find them (with links) in [INDEX.md](INDEX.md).

The grouping follows the categories the source platforms already use
(HackerRank tracks, Codility lessons) plus the classic interview topics that the
LeetCode set spans.

---

## 0. Complexity & the problem-solving mindset

Before reaching for a technique, frame the problem.

**Big-O in one breath.** Time/space complexity describes how work grows with
input size `n`, keeping only the dominant term: `O(1)` (constant), `O(log n)`
(halving), `O(n)` (one pass), `O(n log n)` (sort / divide-and-conquer),
`O(n²)` (nested pass), `O(2ⁿ)` / `O(n!)` (subsets / permutations). You discard
constants and lower-order terms because they stop mattering as `n` grows.

**Read the constraints — they leak the intended complexity.** `n ≤ 20` invites
exponential (subsets/backtracking); `n ≤ 2000` allows `O(n²)`; `n ≤ 10⁵`–`10⁶`
demands `O(n)` or `O(n log n)`; "huge `n`, tiny answer" hints `O(log n)` or
math. (This is exactly Codility's *Time Complexity* lesson — see *FrogJmp*,
*TapeEquilibrium*.)

**The standard escalation.** (1) State the brute force and its cost. (2) Find the
*bottleneck* — the repeated work. (3) Remove it with the right tool: precompute
(prefix sums), remember (hashing / DP), maintain an invariant (two pointers /
sliding window / monotonic stack), or exploit structure (sortedness → binary
search, overlap → intervals). (4) Re-check space; an `O(n)` table can sometimes
collapse to `O(1)` rolling state.

**Space–time trade-off** is the recurring lever: a hash map or DP table spends
memory to buy speed (e.g. *Two Sum* `0001`, *Subarray Sum Equals K* `0560`).

---

## 1. Arrays & two pointers

**Idea.** Contiguous, index-addressable storage with `O(1)` random access. Most
"scan and combine" problems are array problems. The signature optimization is
the **two-pointer** method: replace a nested `O(n²)` scan with two indices that
each move monotonically, giving `O(n)`.

**Recognize it when:** the array is sorted (or you can sort it), you're looking
for a pair/triple meeting a sum/difference condition, or you must partition /
compact in place.

**Techniques & ways of thinking.**
- *Opposite ends:* start `lo=0`, `hi=n-1`, move inward based on a comparison —
  *Two Sum II* `0167`, *Container With Most Water* `0011`, *Valid Palindrome*
  `0125`, *Squares of a Sorted Array* `0977`, *3Sum* `0015` (fix one, two-point
  the rest).
- *Fast/slow (read/write) pointers:* one writes the kept prefix while the other
  scans — in-place removal/compaction: *Remove Element* `0027`, *Move Zeroes*
  `0283`, *Remove Duplicates from Sorted Array* `0026`, *Sort Colors* `0075`
  (Dutch-flag three-way partition).
- *Merging two sorted runs* from the back to avoid overwrites — *Merge Sorted
  Array* `0088`.

**Cost.** Usually `O(n)` time after an optional `O(n log n)` sort, `O(1)` extra.

---

## 2. Prefix sums (and difference arrays)

**Idea.** Precompute cumulative totals so any range sum is an `O(1)` subtraction:
`sum(i..j) = prefix[j] - prefix[i-1]`. This is Codility's *Prefix Sums* lesson.

**Recognize it when:** you need many range-sum/range-count queries, or a subarray
whose sum/average hits a target.

**Techniques.**
- Running totals — *Running Sum of 1d Array* `1480`, *Product of Array Except
  Self* `0238` (prefix × suffix products, no division).
- **Prefix sum + hash map** is the killer combination: store seen prefix sums to
  find a subarray with a given sum in one pass — *Subarray Sum Equals K* `0560`,
  *Contiguous Array* `0525` (map 0→−1), *Subarray With Positive Product* `1567`.
- Count divisibles / passing pairs by prefix counting — Codility *CountDiv*,
  *PassingCars*.

**Cost.** `O(n)` build, `O(1)` per query.

---

## 3. Sliding window

**Idea.** A special two-pointer pattern over a *contiguous* window `[l, r]` that
expands `r` and contracts `l` while maintaining a running aggregate, so each
element enters and leaves at most once — `O(n)` instead of `O(n·k)`.

**Recognize it when:** "longest/shortest/at-most-k contiguous substring/subarray
satisfying a constraint", or fixed-size window stats.

**Techniques.**
- *Variable window:* grow until the constraint breaks, then shrink — *Longest
  Substring Without Repeating Characters* `0003`, *Minimum Size Subarray Sum*
  `0209`, *Subarray Product Less Than K* `0713`.
- *Fixed window + frequency map:* anagram/permutation matching — *Find All
  Anagrams* `0438`, *Permutation in String* `0567`, *Repeated DNA Sequences*
  `0187`.
- *Window + monotonic deque* for window max/min — *Sliding Window Maximum*
  `0239`.

**Cost.** `O(n)`; the window state is `O(k)` or `O(alphabet)`.

---

## 4. Hashing & counting

**Idea.** A hash map/set gives expected `O(1)` membership, lookup, and frequency
counting — trading space for time. Codility's *Counting Elements* lesson is the
array-bounded version (use the value as an index when the range is small).

**Recognize it when:** "have I seen this?", "how many of each?", grouping by a
key, or de-duplication.

**Techniques & thinking.**
- *Complement lookup:* store what you've seen, query for the missing piece —
  *Two Sum* `0001`, *4Sum II* `0454` (pair-sum two halves).
- *Frequency tables* (`collections.Counter`): anagrams group by sorted/char-count
  key — *Group Anagrams* `0049`, *Valid Anagram* `0242`, *Top K Frequent*
  `0347`/`0692`, *First Unique Character* `0387`, *Ransom Note* `0383`.
- *Counting array* when values are a small bounded range (faster than a dict) —
  Codility *MissingInteger*, *PermCheck*, *MaxCounters*; *Counting Elements*
  `1426`.
- *Set for seen/cycle detection* — *Contains Duplicate* `0217`, *Happy Number*
  `0202`.

**Cost.** `O(n)` time, `O(n)` space; worst-case hashing is `O(n)` per op but
rarely matters here.

---

## 5. Sorting

**Idea.** Imposing order unlocks two pointers, binary search, greedy choices, and
duplicate grouping. Comparison sorts are `O(n log n)`; when keys are small
integers, **counting/radix sort** is `O(n + k)`. Codility *Sorting* and the
HackerRank *Sorting* track drill the mechanics.

**Recognize it when:** the answer depends on relative order, nearest values,
medians/extremes, or "after sorting, the structure is obvious".

**Techniques.**
- *Sort then sweep* — *Merge Intervals* `0056`, *Largest Perimeter Triangle*
  `0976`, Codility *Triangle*, *MaxProductOfThree* (watch negatives).
- *Custom comparators / key functions* — *Sort Characters By Frequency* `0451`,
  *Reorder Data in Log Files* `0937`, *K Closest Points* `0973`.
- *Counting sort* when the alphabet is tiny — HackerRank *Counting Sort 1/2*,
  *Sort Array By Parity* `0905`.
- *Index-as-hash placement* (use the value as its own slot) — *Find the
  Duplicate Number* `0287`, *Find All Duplicates in an Array* `0442`.
- Know the classics conceptually: insertion, quicksort partition, merge — they
  appear directly in HackerRank *Insertion Sort*, *Quicksort 1 - Partition*.

**Cost.** `O(n log n)` comparison, `O(n + k)` counting.

---

## 6. Binary search

**Idea.** Repeatedly halve a *monotonic* search space — `O(log n)`. The deep
insight: you're not just searching a sorted array, you're finding the boundary
of a **monotonic predicate** ("is `x` feasible?"), which lets you binary-search
over *answers*, not just indices.

**Recognize it when:** the array is sorted/rotated, you need a first/last
position, or you can phrase the answer as "smallest/largest value for which a
check passes" and the check is monotonic.

**Techniques.**
- *Classic / boundary search* — *Binary Search* `0704`, *Search Insert Position*
  `0035`, *First/Last Position* `0034`, *First Bad Version* `0278`, *Guess
  Number* `0374`.
- *Search in rotated / 2D structure* — *Search in Rotated Sorted Array* `0033`,
  *Find Minimum in Rotated* `0153`, *Search a 2D Matrix* `0074`/`0240`.
- *Binary search on the answer* / monotonic value — *Sqrt(x)* `0069`, *Valid
  Perfect Square* `0367`, *Find Peak Element* `0162` (search on slope), *Single
  Element in a Sorted Array* `0540` (parity boundary).

**Pitfalls.** Off-by-one in `lo`/`hi`/`mid` and loop termination — fix a template
(`while lo < hi`) and keep the invariant explicit.

**Cost.** `O(log n)` per search.

---

## 7. Strings

**Idea.** Strings are arrays of characters, so most array techniques transfer —
but immutability (in Python, build with lists/`"".join`) and the small, fixed
alphabet (enabling `O(1)` count arrays) shape the solutions. The HackerRank
*Strings* track is the playground here.

**Recognize it when:** parsing, transforming, matching, or comparing text.

**Techniques.**
- *Frequency/anagram reasoning* (see Hashing) — *Longest Palindrome* `0409`,
  *Valid Anagram* `0242`, HackerRank *Anagram*, *Pangrams*, *Funny String*.
- *Two-pointer on characters* — *Reverse String* `0344`, *Reverse Vowels*
  `0345`, *Backspace String Compare* `0844`, *Valid Palindrome* `0125`.
- *In-place / token manipulation* — *Reverse Words* `0151`/`0557`, *Length of
  Last Word* `0058`, *Caesar Cipher*, *CamelCase*.
- *Encoding/parsing* — *Roman to Integer* `0013`, *String to Integer (atoi)*
  `0008`, *Add Strings* `0415`, *Multiply Strings* `0043`.
- For pattern search beyond brute force, know that KMP/Rabin-Karp exist
  (*Implement strStr()* `0028`, *Repeated DNA Sequences* `0187`).

**Cost.** Typically `O(n)`; alphabet-bounded auxiliary space is `O(1)`.

---

## 8. Linked lists

**Idea.** Nodes chained by pointers: `O(1)` insert/delete given the node, but
`O(n)` access and no random indexing. Mastery is really about careful pointer
rewiring. HackerRank *Linked Lists* and many LeetCode problems cover it.

**Recognize it when:** the input *is* a list, or you need `O(1)` splice/reorder.

**Techniques & thinking.**
- *Dummy/sentinel head* to simplify edge cases at the front — *Remove Linked
  List Elements* `0203`, *Merge Two Sorted Lists* `0021`, *Remove Nth From End*
  `0019`.
- *Two pointers (fast/slow):* cycle detection and midpoint (Floyd's tortoise &
  hare) — *Linked List Cycle* `0141`/`0142`, *Middle of the Linked List* `0876`,
  *Palindrome Linked List* `0234`.
- *Iterative reversal* (track prev/curr/next) — *Reverse Linked List* `0206`,
  *Reverse Nodes in k-Group* `0025`, *Reorder List* `0143`.
- *Gap pointers* for nth-from-end and intersection — *Intersection of Two Lists*
  `0160`.
- Combine with a hash map / doubly linked list for `O(1)` LRU — *LRU Cache*
  `0146`.

**Cost.** Mostly `O(n)` time, `O(1)` space (recursion is `O(n)` stack).

---

## 9. Stacks & queues (and monotonic stacks)

**Idea.** LIFO stack and FIFO queue model *order of processing*. Codility's
*Stacks and Queues* lesson is the core; the advanced idea is the **monotonic
stack/deque**, which keeps elements in sorted order to answer "next greater/
smaller" in amortized `O(n)`.

**Recognize it when:** matching nested structure (brackets), evaluating
expressions, "undo/most-recent", nearest-greater/smaller, or BFS frontier.

**Techniques.**
- *Stack for matching/parsing* — *Valid Parentheses* `0020`, *Valid Parenthesis
  String* `0678`, *Min Remove to Make Valid* `1249`, *Evaluate Reverse Polish
  Notation* `0150`, *Basic Calculator II* `0227`, Codility *Brackets*,
  *Nesting*.
- *Augmented stack* carrying extra state — *Min Stack* `0155`.
- *Monotonic stack* for spans/areas/next-greater — *Trapping Rain Water* `0042`,
  *Remove K Digits* `0402`.
- *Two stacks ⇒ a queue* / *stack via queues* — *Implement Queue using Stacks*
  `0232`, HackerRank *Queue using Two Stacks*.
- *Monotonic deque* for sliding-window extremes — *Sliding Window Maximum*
  `0239`.

**Cost.** `O(n)` amortized; each element is pushed/popped at most once.

---

## 10. Heaps / priority queues

**Idea.** A binary heap gives the min (or max) in `O(1)` and insert/extract in
`O(log n)` — the right tool when you repeatedly need the current extreme without
fully sorting. HackerRank *Heap*; Python's `heapq` (a min-heap).

**Recognize it when:** "top-k / k-th largest", "merge k sorted", streaming
median, or repeatedly pulling the smallest/largest.

**Techniques.**
- *Size-k heap for top-k* (keep a heap of size k) — *Kth Largest Element* `0215`,
  *Top K Frequent* `0347`/`0692`, *K Closest Points* `0973`.
- *Two heaps* (max-heap of lower half + min-heap of upper half) for a running
  median — *Find Median from Data Stream* `0295`.
- *Greedy simulation* pulling extremes — *Last Stone Weight* `1046`, Codility
  *TieRopes* (greedy, heap-free but same "process largest/feasible" instinct).

**Cost.** Build `O(n)`; each push/pop `O(log n)`; top-k `O(n log k)`.

---

## 11. Trees & binary search trees

**Idea.** Hierarchical nodes with ≤2 children (binary) or many (n-ary). Almost
every tree problem is a **traversal** (DFS: pre/in/post-order; BFS: level-order)
plus a small amount of bookkeeping. A **BST** adds the invariant *left < node <
right*, making search/insert `O(h)` and giving sorted output via in-order.

**Recognize it when:** the input is a tree; you need depth/path/ancestor info, a
level-by-level view, or ordered operations on a BST.

**Techniques & thinking.**
- *DFS recursion* — define what the function returns for a subtree and combine
  children: *Maximum Depth* `0104`, *Diameter* `0543`, *Binary Tree Max Path
  Sum* `0124`, *Path Sum* `0112`/`0113`, *Invert* `0226`, *Same/Symmetric Tree*
  `0100`/`0101`.
- *Traversals, recursive and iterative (explicit stack)* — *Inorder/Preorder/
  Postorder* `0094`/`0144`/`0145`, *BST Iterator* `0173`.
- *BFS / level-order* with a queue — *Level Order* `0102`, *Zigzag* `0103`,
  *Right Side View* `0199`, *Cousins* `0993`.
- *BST invariant* — *Validate BST* `0098`, *Search/Insert/Delete in BST*
  `0700`/`0701`/`0450`, *Kth Smallest* `0230`, *LCA in a BST* `0235` (vs general
  *LCA* `0236`).
- *Construct / serialize* from traversals — `0105`/`0106`/`1008`, *Serialize and
  Deserialize* `0297`.

**Cost.** `O(n)` to visit; space `O(h)` for recursion (`O(n)` worst, `O(log n)`
balanced).

---

## 12. Graphs (BFS, DFS, union-find, topological order)

**Idea.** Nodes + edges; trees and grids are special cases. The two workhorses
are **DFS** (go deep, natural recursion, connectivity/components/cycles) and
**BFS** (expand by layers, gives *shortest path in unweighted graphs*).

**Recognize it when:** relationships/connections, reachability, shortest steps,
"regions" in a grid, dependencies/ordering.

**Techniques & thinking.**
- *Grid as implicit graph* (cell = node, 4/8-neighbors = edges):
  - DFS/BFS flood fill — *Number of Islands* `0200`, *Max Area of Island*
    `0695`, *Flood Fill* `0733`, *Surrounded Regions* `0130`, *Coloring a Border*
    `1034`, *Island Perimeter* `0463`.
  - *Multi-source BFS* (seed all sources at once) — *Rotting Oranges* `0994`,
    *01 Matrix* `0542`.
  - *Shortest path on a grid* — *Shortest Path in Binary Matrix* `1091`.
- *Explicit graph traversal* — *Clone Graph* `0133`, *Keys and Rooms* `0841`,
  *All Paths Source→Target* `0797`, *Number of Provinces* `0547` (connected
  components), *Find the Town Judge* `0997` (degree counting).
- *DAG / topological reasoning* — *Min Vertices to Reach All Nodes* `1557`
  (in-degree), *Longest Increasing Path in a Matrix* `0329` (DFS + memo on a
  DAG).
- *Union-Find (disjoint set)* is the alternative to DFS for connectivity/
  components — worth knowing for province/island-style merges.

**Cost.** `O(V + E)` for a full traversal.

---

## 13. Recursion & backtracking

**Idea.** Recursion solves a problem via smaller instances of itself (base case +
recursive case). **Backtracking** is systematic recursion over a decision tree:
*choose → explore → un-choose*, pruning branches that can't lead to a valid
answer. It's how you enumerate combinatorial spaces.

**Recognize it when:** "generate/return all ...", subsets, permutations,
combinations, partitions, or constraint puzzles (and `n` is small).

**Techniques & thinking.**
- *Subsets / power set* — *Subsets* `0078`/`0090`, *Letter Case Permutation*
  `0784`.
- *Permutations* (track used elements) — *Permutations* `0046`/`0047`.
- *Combinations with a `start` index* to avoid reorder duplicates — *Combinations*
  `0077`, *Combination Sum* `0039`/`0040`/`0216`.
- *Partition / build-up* — *Palindrome Partitioning* `0131`, *Generate
  Parentheses* `0022` (prune by open/close counts), *Letter Combinations* `0017`.
- *Grid backtracking with visited marking* — *Word Search* `0079`.
- Key habits: define the *state*, the *choices* at each step, the *base case*,
  and the *pruning* that keeps it from being pure brute force.

**Cost.** Exponential by nature: `O(2ⁿ)` subsets, `O(n!)` permutations — viable
only for small `n`.

---

## 14. Dynamic programming

**Idea.** When a problem has **optimal substructure** (the answer is built from
answers to subproblems) and **overlapping subproblems** (the same subproblems
recur), cache subproblem results so each is computed once. DP = recursion +
memoization, or its bottom-up table form. HackerRank *Dynamic Programming*.

**Recognize it when:** "count the number of ways", "min/max cost/length", "is it
possible to ...", and a greedy choice isn't safe because decisions interact.

**Ways of thinking.**
1. Define the **state** (what parameters identify a subproblem) and what the DP
   value *means*. 2. Write the **recurrence** (transition) from smaller states.
   3. Set **base cases**. 4. Choose top-down memo or bottom-up table. 5. Often
   **compress space** to a rolling row/variables.

**Families in this repo.**
- *1-D linear DP* — *Climbing Stairs* `0070`, *Fibonacci/Tribonacci*
  `0509`/`1137`, *House Robber* `0198`/`0213`, *Min Cost Climbing Stairs* `0746`,
  *Maximum Subarray* `0053` & *Maximum Product Subarray* `0152` (Kadane — track
  best ending here), *Best Sightseeing Pair* `1014`, *Decode Ways* `0091`,
  *Delete and Earn* `0740`.
- *Sequence / subsequence DP* — *Longest Increasing Subsequence* `0300`/`0673`,
  *Longest Common Subsequence* `1143`, *Edit Distance* `0072`, *Delete Operation
  for Two Strings* `0583`, *Word Break* `0139`.
- *Grid / 2-D DP* — *Unique Paths* `0062`, *Minimum Path Sum* `0064`, *Triangle*
  `0120`, *Maximal Square* `0221`.
- *Knapsack-style / unbounded* — *Coin Change* `0322`, *Integer Break* `0343`,
  *Arithmetic Slices* `0413`.
- *DP on trees / DAGs* — *Binary Tree Max Path Sum* `0124`, *Longest Increasing
  Path in a Matrix* `0329`.

**Cost.** Usually `O(states × transition)` time and `O(states)` space (often
reducible).

---

## 15. Greedy

**Idea.** Build the answer with the locally best choice at each step and never
reconsider. It's fast and simple *when a greedy choice is provably safe* — i.e.
a local optimum leads to a global optimum. The hard part is proving (or trusting)
that exchange argument. Codility *Greedy algorithms*, HackerRank *Greedy*.

**Recognize it when:** intervals/scheduling, "minimum number of ...", or a clear
sort-then-take-best structure — and DP feels like overkill.

**Techniques & thinking.**
- *Sort, then make the obvious choice* — *Non-overlapping Intervals* `0435`
  (keep earliest finish), *Partition Labels* `0763`, Codility *TieRopes*,
  *MaxNonoverlappingSegments*, HackerRank *Greedy Florist*, *Maximum Perimeter
  Triangle*.
- *Reach / jump frontier* — *Jump Game* `0055`, *Jump Game II* `0045`.
- *Stock / running-extreme greed* — *Best Time to Buy and Sell Stock*
  `0121`/`0122`, Codility *MaxProfit*.
- *Monotonic-stack greed* — *Remove K Digits* `0402`.
- Sanity check: if a counterexample breaks the greedy choice, fall back to DP.

**Cost.** Often `O(n log n)` (the sort) or `O(n)`.

---

## 16. Intervals

**Idea.** Pairs `[start, end]`; the recurring move is to **sort by start (or
end)** and then sweep, comparing each interval to the running frontier. A **sweep
line** / two-pointer merge handles overlaps.

**Recognize it when:** meetings/bookings, merging ranges, overlap counts, "max
concurrent".

**Techniques.**
- *Sort + merge* — *Merge Intervals* `0056`.
- *Greedy interval scheduling* — *Non-overlapping Intervals* `0435`.
- *Two-pointer intersection of two sorted interval lists* — *Interval List
  Intersections* `0986`.
- *Heap / sweep for concurrency* — *Meeting Rooms II* `0253` (min-heap of end
  times = rooms in use).
- *Geometry overlap test* — *Rectangle Overlap* `0836`.

**Cost.** `O(n log n)` from the sort, then `O(n)`.

---

## 17. Matrix / grid

**Idea.** 2-D arrays. Beyond grid-graph traversal (§12), many problems are about
**index arithmetic** and **in-place transformation** using `O(1)` extra space.

**Recognize it when:** rotations, transposes, layer-by-layer traversal,
simulation on a board, or treating cells as graph nodes.

**Techniques.**
- *Transpose + reflect* to rotate — *Rotate Image* `0048`, *Transpose Matrix*
  `0867`, *Flipping an Image* `0832`.
- *Boundary/layer walking* — *Spiral Matrix* `0054`/`0059`.
- *Encode state in place* to update simultaneously — *Game of Life* `0289`
  packs the next state into a spare bit so the board updates in `O(1)` space.
- *Reshape / diagonal indexing* — *Reshape the Matrix* `0566`, *Matrix Diagonal
  Sum* `1572`.
- Grid DP and grid BFS/DFS live in §14 and §12.

**Cost.** `O(m·n)` to touch every cell.

---

## 18. Bit manipulation

**Idea.** Integers are bit vectors; bitwise ops (`&`, `|`, `^`, `~`, `<<`, `>>`)
do set-like work in `O(1)`. The standout identity: **XOR** cancels pairs
(`x ^ x = 0`, `x ^ 0 = x`), so it isolates the odd one out. HackerRank *Bit
Manipulation*.

**Recognize it when:** "find the unique/missing number", powers of two, counting
bits, subset enumeration via bitmasks, or arithmetic without `+`.

**Techniques.**
- *XOR to cancel duplicates / find missing* — *Single Number* `0136`, *Missing
  Number* `0268`, Codility *OddOccurrencesInArray*, *Decode XORed Array* `1720`,
  *Hamming Distance* `0461`.
- *Power-of-two / mask tricks* — `n & (n-1)` clears the lowest set bit:
  *Number of 1 Bits* `0191`, *Power of Two* `0231`, *Counting Bits* `0338`.
- *Bit-by-bit construction* — *Reverse Bits* `0190`, *Complement* `0476`/`1009`,
  *Sum of Two Integers* `0371` (add via XOR + carry), *Convert to Hexadecimal*
  `0405`.
- *Bitmask state* — represent a small set of choices as an integer (subset DP,
  *Letter Case Permutation* `0784`).

**Cost.** `O(1)` per op, `O(#bits)` (≈32) for whole-word loops.

---

## 19. Math & number theory

**Idea.** Some problems are closed-form or rely on a numeric property; spotting
the math beats simulating it. Topics: digits, primes, GCD/LCM, modular
arithmetic, combinatorics, geometry.

**Recognize it when:** digit manipulation, divisibility/primality, counting
arrangements, or "huge input, formula-shaped answer".

**Techniques.**
- *Digit decomposition* — *Reverse Integer* `0007`, *Palindrome Number* `0009`,
  *Add Digits* `0258`, *Number of Steps to Reduce to Zero* `1342`.
- *Base conversion* — *Excel Sheet Column Number/Title* `0171`/`0168` (bijective
  base-26), *Roman to Integer* `0013`.
- *Primes & factors* — *Count Primes* `0204` (Sieve of Eratosthenes), *Factorial
  Trailing Zeroes* `0172` (count factors of 5), *Happy Number* `0202`.
- *Geometry* — *Max Points on a Line* `0149` (slopes), *Straight Line* `1232`,
  *Projection Area* `0883`.
- *Powers / fast checks* — *Power of Three/Four* `0326`/`0342`, *Perfect Square*
  `0367`.

**Cost.** Often `O(1)` or `O(log n)`; sieve is `O(n log log n)`.

---

## 20. Design (data-structure construction)

**Idea.** Instead of computing one answer, you *implement a type* whose
operations must each hit a target complexity. The skill is composing primitives
(arrays, hash maps, linked lists, heaps, trees) so every method is fast.

**Recognize it when:** the prompt says "Design a class that supports `op1`,
`op2` ... in `O(1)`/`O(log n)`".

**Techniques & thinking.**
- *Hash map + doubly linked list* for `O(1)` get/put with eviction — *LRU Cache*
  `0146`, *Design Linked List* `0707`.
- *Hash map + dynamic array* for `O(1)` insert/delete/getRandom — *Insert Delete
  GetRandom O(1)* `0380`.
- *Trie (prefix tree)* for prefix queries — *Implement Trie* `0208`, *Add and
  Search Words* `0211` (with `.` wildcard DFS).
- *Build the structure from scratch* — *Design HashMap/HashSet* `0706`/`0705`
  (buckets + chaining), *Min Stack* `0155`, *Queue using Stacks* `0232`.
- *Compose existing structures* — *Design Twitter* `0355` (hash maps + heap
  merge), *Browser History* `1472`, *Parking System* `1603`, *Encode/Decode
  TinyURL* `0535`.

**Cost.** Stated per operation; the whole point is meeting those targets.

---

## How to use this guide

1. **Classify first.** Map the problem to one or two topics above using the
   "recognize it when" cues — that narrows the toolset dramatically.
2. **Recall the pattern,** not the specific solution: the dummy head, the
   complement map, the choose/explore/un-choose loop, the state + recurrence.
3. **Estimate the target complexity** from the constraints and pick the technique
   that hits it.
4. **Find a sibling problem** in [INDEX.md](INDEX.md) and compare approaches —
   many solution files keep more than one (`Solution1`/`Solution2`) precisely to
   contrast techniques.

These topics overlap constantly — sliding window *is* two pointers, DP often
replaces backtracking, BFS rides on a queue, greedy is a disciplined heuristic.
Fluency comes from seeing the same few ideas recombined.
