class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        def populate_rows_and_columns(grid: List[List[int]]) -> dict:
            # store rows and column arrays in a hashmap
            rows = {i:grid[i] for i in range(len(grid))}
            columns = {i:[] for i in range(len(grid))}

            for r in range(len(rows)):
                for c in range(len(columns)):
                    columns[r].append(rows[c][r])
            return {"rows": rows, "columns": columns}
        
        result = populate_rows_and_columns(grid)
        rows = result["rows"]
        columns = result["columns"]
        
        # Compare each row to each column array in the grid
        equal_pair = 0
        for i in range(len(rows)):
            for j in range(len(columns)):
                if rows[i] == columns[j]:
                    equal_pair += 1
        return equal_pair
                