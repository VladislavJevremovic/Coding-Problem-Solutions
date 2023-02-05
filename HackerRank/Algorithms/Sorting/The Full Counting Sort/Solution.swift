func countSort(arr: [[String]]) -> String {
    var r = [String](repeating: "", count: 100)
    for (i, rep) in arr.enumerated() {
        guard let x = Int(rep[0]) else { continue }
        r[x] += (i < arr.count / 2 ? "- " : rep[1] + " ")
    }

    return r.reduce("") { $0 + $1 }
} // too slow input



static void countSort(List<List<String>> arr) {        
    StringBuffer[] sb = new StringBuffer[100];
    for (int i = 0; i < sb.length; i++) {
        sb[i] = new StringBuffer();
    }

    int n = arr.size();
    for (int i = 0; i < n; i++) {
        List<String> rep = arr.get(i);
        int x = Integer.parseInt(rep.get(0));
        String s = (i < n / 2) ? "- " : rep.get(1) + " ";
        sb[x].append(s);
    }

    for (int i = 0; i < sb.length; i++) {
        System.out.print(sb[i]);
    }
} // java is faster